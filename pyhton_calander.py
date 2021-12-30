# creating a python calendar
import time
days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print('this is a january 2022 calendar only ')
date = int(input('enter a date will show the day and any event on that day : '))

if date == 1:
    print(days[5],'2022 begins wishing you a very happy new year ')
    event = input("need some entertainment today press 'y' : ")
    if event == 'y':
        print('watch today kabadi match on hotstar ')
        print('telugu titans vs  bengaluru bulls ')
        print('time 8:30 live on hotstar mana telugu lo ')
    horoscope1 = input("want to know day details by horoscope press 'y':")
    if horoscope1 == 'y':
        time.sleep(2)
        print('please wait we are getting the details for .....')
        time.sleep(2)
        print('.....................')
        time.sleep(2)
        print("margasheeram")
        print("b.thrayodhasi. 07:17")
        print("chaturdhasi. 03:41 + ")
        print("jaista 19:18")
        print("bad time. 06:36 - 07:20"
              "07:21 -08:05")
        print("va. 2:20(+) - 3:44 +")
elif date == 2:
    print(days[6])
    horoscope2 = input("want to know day details by horoscope press 'y':")
    if horoscope2 == 'y':
        time.sleep(2)
        print('please wait we are getting the details for .....')
        time.sleep(2)
        print('.....................')
        time.sleep(2)
        print("margasheeram")
        print("amavasya. 00:02 + mula. 16:23")
        print("bad time. 16:17 - 17:02")
        print("va. 14:59 - 16:23 "
              "00:51 (+) -02:16 +")
elif date == 3:
    print(days[0])
    telugu2 = input("today our team telugu titans having match press 'y' to know the details:")
    if telugu2 == 'y':
        print('telugu titans vs   patna pirates')
        print('watch live on hotstar at 8:30 pm  mana telugu lo  ')
    horoscope3 = input("want to know today horoscope press 'y' ")
    if horoscope3 == 'y':
        time.sleep(2)
        print('please wait we are getting the details for .....')
        time.sleep(2)
        print('.....................')
        time.sleep(2)
        print("pushyami ")
        print("amavasya. 00:02 + mula. 16:23")
        print("bad time. 16:17 - 17:02")
        print("va. 14:59 - 16:23 "
              "00:51 (+) -02:16 +")

elif date == 4:
    print(days[1])
elif date == 5:
    print(days[2])
elif date == 6:
    print(days[3])
elif date == 7:
    print(days[4])
elif date == 8:
    print(days[5])
elif date == 9:
    print(days[6])
elif date == 10:
    print(days[0])
elif date == 11:
    print(days[1])
    telugu3 = input("today we have our telugu titans match press 'y' to know the details:")
    if telugu3 == 'y':
        print('today match details')
        print('telugu titans vs   gujarath gaints ')
        print('watch live on hotstar at 8:30 pm mana telugu lo ')
        predict = input("tell me who will win on today match  if telugu titans press 't' or 'g' for gujarat:[1")
        if predict == 't':
            print('ya always cheer for our telugu team')
        elif predict == 'g':
            print('will se hope is there on telugu titans')
elif date == 12:
    print(days[2])
elif date == 13:
    print(days[3])
elif date == 14:
    print(days[4])
    print(' wishing you a happy pongal to you and your family ')
elif date == 15:
    print(days[5])
    telugu3 = input("today out telugu titans match press 'y' to know the details:" )
    if telugu3 == 'y':
        print('today match details')
        print('telugu titans vs u.p yoddha')
        print('watch live on hotstar at 7:30 pm in mana telugu lo ')
elif date == 16:
    print(days[6])
elif date == 17:
    print(days[0])
elif date == 18:
    print(days[1])
elif date == 19:
    print(days[2])
elif date == 20:
    print(days[3])
elif date == 21:
    print(days[4])
elif date == 22:
    print(days[5])
elif date == 23:
    print(days[6])
elif date == 24:
    print(days[0])
elif date == 25:
    print(days[1])
elif date == 26:
    print(days[2])
    print('happy republic day')
elif date == 27:
    print(days[3])
elif date == 28:
    print(days[4])
elif date == 29:
    print(days[5])
elif date == 30:
    print(days[6])
elif date == 31:
    print(days[0])
else:
    print('  but january 2022 having 31 days only')
