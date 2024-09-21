# ctclsite-rust - CTCL 2020-2024
# Single-use script kept for reference

import os, json

files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
# Filter file names
files = [f[:-3] for f in files if f.endswith(".md")]

print(files)

for file in files: 
    os.mkdir(file)
    os.rename(f"{file}.md", f"{file}/{file}.md")
    pagecfg = {
        "title": "",
        "theme": "mct2",
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
                "content": f"{file}.md"
            }
        }
    }
    with open(f"{file}/page.json", "w") as f:
        f.write(json.dumps(pagecfg, indent = 4))