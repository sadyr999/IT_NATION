# while / if, else
# == >= <= < > !=
# and, or, not

while True:
    age = int(input("skoka let???: "))
    if age < 18:
        print("bye")
    elif 18 <= age <= 60:
        print("your age ot 18 do 60")
        break
    else:
        print("Incorrect")

number = int(input("chislo: "))
if number != 45:
    print("111")

user_list = ['Sadyr', 'Sooronbay', 'Almaz']
print(len(user_list))

if len(user_list) >= 4:
    print("tuta bolwe chetyreh")
else:
    print("aaaa tut menwe chetyreh")

text = "Sadyr Pulemet"
numbers_tuple = (1, 2, 3, 4, 5)
print(len(text))
print(len(numbers_tuple))

if not 3 == 4 and 5 > 3:
    print("hello")