
import os
import json

dirs = os.listdir(".")

for page in dirs:
    print("                {")
    print("                    \"type\": \"full\",")
    print(f"                    \"page\": \"/projects/{page}/\"")
    print("                },")