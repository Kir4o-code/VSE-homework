import os
import time
import json
from datetime import datetime, timedelta


def write_output(name, mtime):
    with open("modified.log", "a", encoding="utf-8") as f:
        f.write(json.dumps({"filename": name, "modified_time": mtime}) + "\n")


def main(directory):
    while True:
        limit = datetime.now() - timedelta(minutes=30)

        for file in os.listdir(directory):
            path = os.path.join(directory, file)

            if os.path.isfile(path):
                mtime = datetime.fromtimestamp(os.path.getmtime(path))
                if mtime >= limit:
                    write_output(file, mtime.strftime("%Y-%m-%d %H:%M:%S"))

        time.sleep(10)   # проверява на всеки 10 секунди


if __name__ == "__main__":
    dir_path = input("Directory: ")
    main(dir_path)
