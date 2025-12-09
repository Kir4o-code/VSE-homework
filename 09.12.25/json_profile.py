import json
import os


def create_user_profile(filename="profile.json", **kwargs):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(kwargs, file, indent=4, ensure_ascii=False)
    print(f"Профилът е записан успешно в {filename}")


def average_size(*args):
    sizes = []

    for filename in args:
        if os.path.exists(filename):
            size_bytes = os.path.getsize(filename)
            sizes.append(size_bytes / 1024) 
        else:
            print(f"Файлът '{filename}' не съществува и се пропуска.")

    if not sizes:
        print("Няма валидни файлове.")
        return

    avg = sum(sizes) / len(sizes)
    print(f"Среден размер на файловете: {avg:.2f} KB")


create_user_profile(
    name="Ivan",
    age=25,
    email="ivan@example.com",
    city="Sofia"
)

average_size("json_profile.py" , "user.json")
