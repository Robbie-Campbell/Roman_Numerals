# This is code that i have self written without any tutorial, although i did watch a video
# by Computerphile on this topic about a week ago
import math

roman = ""

user = int(input("Please enter a integer value: "))
strUser = str(user)
listnum = [int(i) for i in strUser]
bigguns = listnum[0]


def tens_converter():
    global roman
    global user
    if 5 <= user < 9:
        roman = str(roman + "V")
        while 5 < user < 9:
            user = user - 1
            roman = str(roman + 'I')
    elif user == 4:
        roman = str(roman + "IV")
    elif user < 4:
        while user > 0:
            user = user - 1
            roman = str(roman + 'I')
    elif user == 9:
        roman = str(roman + "IX")
    elif 10 < user < 101:
        hundreds_converter()
        user = listnum[1]
        int(user)
        tens_converter()
    elif 1000 > user > 100:
        thousands_converter()
        user = int(listnum[1])
        user = user * 10
        hundreds_converter()
        user = listnum[2]
        int(user)
        tens_converter()
    elif user >= 1000:
        ten_thousands_converter()
        print(user)
        user = int(listnum[1])
        user = user * 100
        print(user)
        thousands_converter()
        user = int(listnum[2])
        user = user * 10
        print(user)
        hundreds_converter()
        print(user)
        user = int(listnum[3])
        tens_converter()
        print(user)

def hundreds_converter():
    global user
    global roman
    i = 0
    if 10 <= user < 40:
        while i < user:
            i = i + 10
            roman = str(roman + 'X')
    elif 40 <= user < 50:
        roman = str(roman + "XL")
    elif 50 <= user < 90:
        roman = str(roman + "L")
        while i < (user - 50):
            i = i + 10
            roman = str(roman + 'X')
    if user == 100:
        roman = str(roman + 'C')
    elif 90 <= user < 100:
        roman = str(roman + "XC")


def thousands_converter():
    global roman
    global user
    i = 100
    if user == 500:
        roman = str(roman + 'D')
    elif 500 >= user >= 400:
        roman = str(roman + 'CD')
    elif 100 < user < 500:
        while i < user:
            i = i + 100
            roman = str(roman + 'C')
    elif 500 < user < 900:
        roman = str(roman + 'D')
        while i <= (user - 500):
            i = i + 100
            roman = str(roman + 'C')
    elif 900 <= user <= 999:
        roman = str(roman + 'CM')


def ten_thousands_converter():
    global roman
    i = 0
    while i < (bigguns * 1000):
        i = i + 1000
        roman = str(roman + 'M')


tens_converter()
print(roman)

