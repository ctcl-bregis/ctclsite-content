# ctclsite-rust - CTCL 2020-2024
# Single-use script kept for reference

import os, json

with open("../../old/blog/config.json") as f: 
    data = dict(json.loads(f.read()))

data.pop("root")

links = []
for (key, value) in data.items():
    pagecfg = {
        "title": value["title"],
        "theme": value["theme"],
        "startdate": value["startdate"],
        "enddate": "",
        "desc": value["desc"],
        "icon": value["icon"],
        "icontitle": value["icontitle"],
        "keywords": [],
        "cat": value["cat"],
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
                "content": value["content"].split("/")[-1]
            }
        },
    }    
    
    try:
        enddate = value["enddate"]
    except:
        enddate = ""

    links.append({
        "type": "full",
        "link": f"/blog/{key}/",
        "theme": value["theme"],
        "startdate": value["startdate"],
        "enddate": enddate,
        "title": value["title"],
        "desc": value["desc"],
        "icon": f"/static/pages/blog/{key}/" + value["icon"].split("/")[-1],
        "icontitle": value["icontitle"],
        "cat": value["cat"]
    })
    
    with open(f"{key}/page.json", "w") as f:
        f.write(json.dumps(pagecfg, indent = 4))

rootcfg = {
    "title": "Blog Posts",
    "theme": "gold",
    "startdate": "",
    "enddate": "",
    "desc": "Current blog posts",
    "icon": "",
    "icontitle": "",
    "keywords": [],
    "cat": "",
    "favicon": "",
    "headerids": True,
    "shownavbar": True,
    "content": {
        "blog": {
            "type": "linklist",
            "boxed": False,
            "title": "",
            "theme": "",
            "fitscreen": False,
            "links": links
        },
    }
}

with open(f"page.json", "w") as f:
        f.write(json.dumps(rootcfg, indent = 4))