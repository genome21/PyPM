import os
import getpass
import datetime

morningstart = open('updates.txt', 'r')
morningstart.read()
linelist = morningstart.readline()
morningstart.close()
operstamp = getpass.getuser()
timestamp = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
dailyupdates = open('updates.txt', 'a')
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
dailyupdates.close()
