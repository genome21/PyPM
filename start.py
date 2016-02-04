import getpass
import datetime

with open('updates.txt', 'r') as morningstart:
    morningstart.read()
    linelist = morningstart.readline()
    operstamp = getpass.getuser()
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')

with open('updates.txt', 'a') as dailyupdates:
    print('This is your last update: ')
    print (linelist)
    print('What are your updates?')
    typedupdates = input()
    nline = "\n"
    iline = " -- "
    dailyupdates.write(operstamp)
    dailyupdates.write(iline)
    dailyupdates.write(timestamp)
    dailyupdates.write(nline)
    dailyupdates.write(typedupdates)
    ender = "\nEOF-------------------------------------------EOF\n\n"
    dailyupdates.write(ender)
