import os
import json

dirs = [x[0][2:] for x in os.walk(".") if x[0] != "."]

for page in dirs:

    pagecfg = {
        "title": "",
        "theme": "gold",
        "startdate": "",
        "enddate": "",
        "desc": "",
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
                "content": f"{page}.md"
            }
        }
    }

    with open(f"{page}/page.json", "w") as f:
        f.write(json.dumps(pagecfg, indent = 4))

print(dirs)