print("---TASK 1---")
import datetime
def find_age(date: str) -> str:
    now = 2021
    while True:
        try:
            year = int(date[-4:])
            print(now - year)
            break
        except:
            print("Incorrect input")
            continue
print(find_age("15.01.1995"))

print("---TASK 3---")
def write_greet(name:str) -> None:
    with open("greeting.txt", "w") as f:
        f.close()
    with open("greeting.txt", "a") as f:
        for _ in range (11):
            f.write(f"Greeting {name}\n")
        f.write(name)

write_greet("Sadyr Japarov")