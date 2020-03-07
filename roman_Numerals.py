# This is code that i have self written without any tutorial, although i did watch a video
# by Computerphile on this topic about a week ago
import math

roman = ""

user = int(input("Please enter a integer value: "))
strUser = str(user)
listnum = [int(i) for i in strUser]


def tens_converter():
    global roman
    global user
    if user >= 5 and user < 9:
        roman = str(roman + "V")
        while user > 5 and user < 9:
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
    else:
        hundreds_converter()
        user = listnum[1]
        int(user)
        tens_converter()


def hundreds_converter():
    global user
    global roman
    tens = listnum[0]
    i = 0
    if user >= 10 and user <=40:
        while i < tens:
            i = i + 1
            roman = str(roman + 'X')
    elif user > 40 and user < 50:
        roman = str(roman + "XL")
    elif user >= 50 and user < 90:
        roman = str(roman + "L")
        while i < (tens - 5):
            i = i + 1
            roman = str(roman + 'X')
    if user == 100:
        roman = str(roman + 'C')
    elif user >= 90:
        roman = str(roman + "XC")



tens_converter()
hundreds_converter()
print(roman)
