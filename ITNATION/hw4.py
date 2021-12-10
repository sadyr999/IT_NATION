print("---TASK 1---")
example = {'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15 / 2, False], 'fire': ['hot', 46, ['cha', 'ching'], 81.13],
           'earth': ['solid', 100, (13, 31, 1), 90.01, {'b': 'c'}]}
elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']


def func_task_1(list_input, dict_input):
    for element in list_input:
        if element in dict_input:
            total = 0
            for i in dict_input[element]:
                try:
                    total += i
                except:
                    continue
            print(f"{element} - {total}")
        else:
            print("Такого ключа в словаре не существует")


func_task_1(elements, example)

print("---TASK 2---")
names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 'fhjhafhdfa.txt']
import random


def create_random_text(names_list: list) -> None:
    filename = random.choice(names_list)
    print(f"The text file created: {filename}")
    f = open(filename, "w")
    f.close()


def find_and_write(names_list: list) -> None:
    for name in names_list:
        try:
            f = open(name, "r+")
            print(f"The text file opened and filled: {name}")
            f.write("SADYR PULEMET")
            f.close()
        except:
            continue


create_random_text(names)
find_and_write(names)

print("---TASK 3---")
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]


def average_montly_income_coef(income: list, spending: list):
    monthly_averages = []
    for month in range(12):
        if income[month] != 0:
            monthly_averages.append(spending[month] / income[month])
        else:
            monthly_averages.append(0)
        print(f"For month {month + 1} coefficient is equal to: {monthly_averages[month]}")
    annual_coef = sum(monthly_averages) / 12
    print(f"ANNUAL coefficient is equal to: {annual_coef}")


average_montly_income_coef(income, spendings)

print("---TASK 4---")
text = """Kyrgyzstan, country of Central Asia. It is bounded by Kazakhstan on the northwest and north, by China on the east and south, 
and by Tajikistan and Uzbekistan on the south and west. Most of Kyrgyzstan’s borders run along mountain crests. The capital is Bishkek 
(known from 1862 to 1926 as Pishpek and from 1926 to 1991 as Frunze)."""
print("--using WITH--")
with open("kyrgyzstan.txt", "w") as f:
    f.write(text)
with open("kyrgyzstan.txt", "r") as f:
    data = f.read()
    print(f"Quantity of symbols in file: {len(data)}")
print("--not using WITH--")
f = open("kyrgyzstan_1.txt", "w")
f.write(text)
f.close()
f = open("kyrgyzstan_1.txt", "r")
data = f.read()
print(f"Quantity of symbols in file: {len(data)}")
f.close()

print("---TASK 5---")
add_text = """The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 
17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. 
Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991."""
print("--using WITH--")
with open("wikipedia.txt", "w") as f:
    text_from_file = ""
    with open("kyrgyzstan.txt", "r") as raw:
        text_from_file = raw.read()
    f.write(text_from_file)
with open("wikipedia.txt", "a") as f:
    f.write(add_text)
with open("wikipedia.txt", "r") as f:
    data_new = f.read()
    print(data_new)
print("--not using WITH--")
f = open("wikipedia_1.txt", "w")
text_from_file = ""
raw = open("kyrgyzstan_1.txt", "r")
text_from_file = raw.read()
f.write(text_from_file)
f.close()
raw.close()
f = open("wikipedia_1.txt", "a")
f.write(add_text)
f.close()
f = open("wikipedia.txt", "r")
data_new = f.read()
print(data_new)
f.close()

print("---TASK 6---")
def tax(volume, year, year_current):
    age = year_current - year
    tax_amount = 0
    tax_rate = 0
    if age in (0,1,2,3,4):
        tax_rate = 0.9
    elif age in (5,6,7,8,9):
        tax_rate = 0.75
    elif age in (10,11,12,13,14):
        tax_rate = 0.60
    else:
        tax_rate = 0.45
    tax_amount = volume * tax_rate
    print(f"Car age is: {age} years, Tax rate is: {tax_rate} soms per cc")
    print(f"Amount to be paid in taxes: {tax_amount} soms")
def main():
    volume = 0
    year = 0
    year_current = 2021
    while True:
        try:
            volume = int(input("Enter engine volume: "))
            year = int(input("Enter production year: "))
            if year <= year_current:
                break
            else:
                print("Incorrect year input, try again")
                continue
        except:
            print("Incorrect input, try again")
            continue
    tax(volume, year, year_current)
if __name__ == "__main__":
    main()

