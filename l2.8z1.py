import os
import json
import csv
import pickle

def recursive(dir):
  files = []
  for file in os.listdir(dir):
    path = os.path.join(dir, file)
    if os.path.isfile(path):
      files.append({
        "name": file,
        "size": os.path.getsize(path),
        "parent_directory": dir,
        "type": "file"
      })
    elif os.path.isdir(path):
      files.extend(recursive(path))
  return files
def save_to_json(files, filename):
  with open(filename, "w") as f:
    json.dump(files, f, indent=4)

def save_to_csv(files, filename):
  with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "size", "parent_directory", "type"])
    for file in files:
      writer.writerow([file["name"], file["size"], file["parent_directory"], file["type"]])
def save_to_pickle(files, filename):
  with open(filename, "wb") as f:
    pickle.dump(files, f)
if __name__ == "__main__":
  dir = "/path/to/directory"
  files = recursive(dir)
  save_to_json(files, "files.json")
  save_to_csv(files, "files.csv")
  save_to_pickle(files, "files.pickle")