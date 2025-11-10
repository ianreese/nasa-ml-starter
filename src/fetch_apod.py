#!/usr/bin/env python
"""
Fetch Astronomy Picture of the Day (APOD) for a given date.
"""
import os, argparse, requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--out", required=True, help="Output image path")
    args = parser.parse_args()

    api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
    url = "https://api.nasa.gov/planetary/apod"
    params = {"date": args.date, "api_key": api_key}
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    data = r.json()

    img_url = data.get("url")
    if not img_url or not img_url.lower().endswith((".jpg",".jpeg",".png")):
        raise SystemExit("APOD for this date is not a static image; pick another date.")

    img = requests.get(img_url, timeout=60)
    img.raise_for_status()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(img.content)
    print(f"Saved APOD image → {args.out}")

if __name__ == "__main__":
    main()
