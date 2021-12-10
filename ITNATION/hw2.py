#TASK 1
text = '''Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.

But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'''

nums = 0
numt = 0
for a in text:
    if a == 's' or a == 'S':
        nums = nums + 1
    elif a == 't' or a == 'T':
        numt = numt + 1
print("-------------")
print("TASK 1 PART A")
print(f'number of "S" letters: {nums}')
print(f'number of "T" letters: {numt}')

text2 = ""
word2 = ""
list2 = []

i = 0
while i < len(text):
    if text[i].isalpha():
        word2 = word2 + text[i]
    else:
        list2.append(word2)
        list2.append(text[i])
        word2 = ""
    i = i + 1

for aa in list2:
    advertword = False
    if len(aa) >= 5 and (aa[0] == 'a' or aa[0] == 'A') and aa[1] == 'd' and aa[2] == 'v' and aa[3] == 'e' and aa[4] == 'r' and aa[5] == 't':
        bb = aa.upper()
        text2 = text2 + bb
    else:
        text2 = text2 + aa
print("-------------")
print("TASK 1 PART B")
print(text2)

#TASK 2
print("-------------")
print("TASK 2")
stroka = input("Input string, odd in length: ")
while True:
    if len(stroka) % 2 == 0:
        stroka = input("String length is not odd, retype it: ")
    else:
        break
i = int((len(stroka)-1)/2)
print(stroka[i-1] + stroka[i] + stroka[i+1])

#TASK 3
print("-------------")
print("TASK 3")
ss1 = "Aidana"
ss2 = "Adilet"
a1 = 0
a2 = 0
out = ""
while a1 < (len(ss1)) and a2 < (len(ss2)):
    out = out + ss1[a1] + ss2[a2]
    a1 = a1 + 1
    a2 = a2 + 1
print(out)

#TASK 4
print("-------------")
print("TASK 4")
i = 0
word3 = ""
list3 = []
while i < len(text):
    if text[i].isalpha():
        word3 = word3 + text[i].lower()
    else:
        if word3 != '':
            list3.append(word3)
        word3 = ""
    i = i + 1
list4 = list(set(list3))
list4.sort()
print(list4)

#TASK 5
print("-------------")
print("TASK 5")
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
dd = aTuple[1][1]
print(f"type: {type(dd)} value: {dd}")

#TASK 6
print("-------------")
print("TASK 6")
number = 3456
numst = str(number)
sum1 = int(numst[0]) + int(numst[1]) + int(numst[2]) + int(numst[3])
print(f"Sum is equal to: {sum1}")

#TASK 7
print("-------------")
print("TASK 7")
i = 0
word5 = ""
list5 = []
while i < len(text):
    if text[i].isalpha():
        word5 = word5 + text[i].lower()
    else:
        if word5 != '':
            list5.append(word5)
        word5 = ""
    i = i + 1
chastoe = ""
qchastoe = 0
dlinnoe = ""
qdlinnoe = 0
for aa in list5:
    q = 0
    for bb in list5:
        if aa == bb:
            q = q + 1
    if q > qchastoe:
        chastoe = aa
        qchastoe = q
    if len(aa) > qdlinnoe:
        qdlinnoe = len(aa)
        dlinnoe = aa
print(f"Most often used word: <<{chastoe}>>. Repeated {qchastoe} times")
print(f"The longest word: <<{dlinnoe}>>. Its length is {qdlinnoe} letters")