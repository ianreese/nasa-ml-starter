#!/usr/bin/env python
"""
Fetch NeoWs (Near Earth Object Web Service) data for a short date range (<= 7 days).
Saves the raw JSON to disk.
"""
import os, json, argparse, datetime as dt
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True, help="YYYY-MM-DD (inclusive)")
    parser.add_argument("--end", required=True, help="YYYY-MM-DD (inclusive, <= 7 days from start)")
    parser.add_argument("--out", required=True, help="Output JSON path")
    args = parser.parse_args()

    api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {"start_date": args.start, "end_date": args.end, "api_key": api_key}

    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(resp.json(), f, indent=2)
    print(f"Saved raw NeoWs JSON → {args.out}")

if __name__ == "__main__":
    main()
