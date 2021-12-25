# creating a movie tickets booking code

import time
theatres = ('spandana','multiplex')
seats = (75,80)
tickets = (100,150)

booking = input('please choose the theatre: ')

if booking == 'spandana':
    time.sleep(2)
    print('please wait while we checking the seats in that theatre')
    time.sleep(2)
    print('spandana having ',seats[0],'left')
    time.sleep(3)
    print(f'the price of the seat in spandan_theatre is {tickets[0]} ')
    time.sleep(2)
    print('your seat was booked on spandana theate seat number 55A and the show time is 2:30pm')
    print('thnks for booking on spandana have a great day ')

elif booking == 'multiplex':
    time.sleep(3)
    print('please wait while we checking the seats in that theatre')
    time.sleep(3)
    print('multiplex theatre having  ',seats[1],'left')
    time.sleep(3)
    print(f'the price of the seat in multiplex_theatre is {tickets[1]} ')
    time.sleep(2)
    print('your seat was booked on multiplex theate seat number 101A and the show time is 1:30pm')
    print('thnks for booking on multiplex have a great day ')
else:
    print('sorry the counter was colsed please come after some time ')
    
    



