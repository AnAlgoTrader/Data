import os, json;

files = [s for s in os.listdir("./") if s.endswith('.csv')]
with open("./files.json", 'w') as f:
    json.dump(files, f)