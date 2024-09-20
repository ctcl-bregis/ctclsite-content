import os, json

with open("ctclsite-config/old/blog/config.json") as f: 
    data = dict(json.loads(f.read()))

data.pop("root")

#for (key, value) in data.items:
    