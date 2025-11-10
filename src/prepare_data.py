#!/usr/bin/env python
"""
Convert NeoWs JSON → tidy CSV for modeling.
Each close-approach becomes one row with numeric features + target label.
"""
import os, json, argparse, csv

def flatten_neows(neows):
    rows = []
    near_earth_objects = neows.get("near_earth_objects", {})
    for date, objs in near_earth_objects.items():
        for obj in objs:
            is_hazard = bool(obj.get("is_potentially_hazardous_asteroid", False))
            abs_mag = obj.get("absolute_magnitude_h", None)
            est = obj.get("estimated_diameter", {}).get("kilometers", {})
            d_min = est.get("estimated_diameter_min", None)
            d_max = est.get("estimated_diameter_max", None)

            approaches = obj.get("close_approach_data", [])
            for ca in approaches:
                rel_vel = ca.get("relative_velocity", {}).get("kilometers_per_second", None)
                miss_km = ca.get("miss_distance", {}).get("kilometers", None)
                approach_date = ca.get("close_approach_date", None)

                def to_float(x):
                    try:
                        return float(x)
                    except Exception:
                        return None

                rows.append({
                    "approach_date": approach_date,
                    "absolute_magnitude_h": to_float(abs_mag),
                    "diameter_km_min": to_float(d_min),
                    "diameter_km_max": to_float(d_max),
                    "rel_velocity_km_s": to_float(rel_vel),
                    "miss_distance_km": to_float(miss_km),
                    "is_hazardous": int(is_hazard),
                })
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True, help="Input NeoWs JSON path")
    parser.add_argument("--out", required=True, help="Output CSV path")
    args = parser.parse_args()

    with open(args.inp, "r") as f:
        data = json.load(f)

    rows = flatten_neows(data)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    cols = ["approach_date","absolute_magnitude_h","diameter_km_min","diameter_km_max","rel_velocity_km_s","miss_distance_km","is_hazardous"]
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    print(f"Wrote {len(rows)} rows → {args.out}")

if __name__ == "__main__":
    main()
