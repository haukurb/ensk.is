#!/usr/bin/env python3

import time
import random

import requests

from db import EnskDatabase


def main() -> int:
    # Read all lines from missing.txt
    with open("missing.txt", "r") as f:
        words = f.readlines()

    random.shuffle(words)

    for w in words:
        word = w.strip()
        url = f"https://idord.arnastofnun.is/d/api/es/agg/dictionaries/?ord={word}"
        response = requests.get(url)

        r: dict = response.json()
        if not r.get("results") or len(r["results"]) == 0:
            continue

        print(url)

        # Sleep for 1 second to avoid overloading the server
        time.sleep(1)

    return 0


if __name__ == "__main__":
    exit(main())