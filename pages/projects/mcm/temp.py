# ctclsite - CTCL 2019 - 2024
# File: /ctclsite-config/pages/projects/mcm/temp.py
# Purpose: Temporary Python script to generate subpages
# Created: November 14, 2024
# Modified: November 14, 2024

import os
import json

# There's an alphabet constant somewhere in Python but I don't feel like looking it up
alphabet = "abcdefghijklmnopqrstuvwxyz"

for c in alphabet:
    if not os.path.exists(f"mcm_{c}"):
        os.mkdir(f"mcm_{c}")

    data = {
        "title": f"MediaCow Micro {c.upper()}",
        "theme": "gold",
        "startdate": "2021-07-18T00:00:00Z",
        "enddate": None,
        "dateprecision": "year",
        "desc": f"MediaCow Micro {c.upper()} portable media player device",
        "icon": "",
        "icontitle": "",
        "keywords": [],
        "cat": "",
        "favicon": "",
        "headerids": True,
        "shownavbar": True,
        "content": {
            "content": {
                "type": "content",
                "boxed": False,
                "title": "",
                "theme": "",
                "fitscreen": False,
                "content": f"mcm_{c}.md"
            }
        }
    }

    with open(f"mcm_{c}/page.json", "w") as f:
        f.write(json.dumps(data, indent = 4))

    content = """
# Hardware

# Software
"""

    with open(f"mcm_{c}/mcm_{c}.md", "w") as f:
        f.write(content)