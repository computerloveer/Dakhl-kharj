#!/usr/bin/python
#coded by poorya samimi
#year 1395
#month 11 OR BAHMAN
#day 06
# coded in 1395/11/06

import time
import platform
import os
# write the function

def kharj(text, date, Name, kar):
	if platform.system() == "Windows":
		os.system("color b")
	print ("The amount spent was recorded in a file called kharj!")
	write = "name : "+Name+"\n"+"date : "+date+"\n"+"mizan kharj : "+text+"\n"+"dar kare : "+kar
	file = open("kharj.txt", "w")
	file.write(write)
	time.sleep(30)

def dakhl(text, date, Name, kar):
	if platform.system() == "Windows":
		os.system("color a")
	print("Amount received was recorded in the file dakhl!")
	write = "name : "+Name+"\n"+"date : "+date+"\n"+"mizan Dakhl : "+text+"\n"+"dar kare : "+kar
	file = open("Dakhl.txt", "w")
	file.write(write)
	time.sleep(100)

def sood(text, text2):
	if platform.system() == "Windows":
		os.system("color e")
	sood_emrooz = int(text) - int(text2)
	print("soode shoma dar emrooz : ", sood_emrooz)
	time.sleep(30)

def About_schools_HAFEZ(n):
	if platform.system() == "Windows":
		os.system("color a")
	print('''

		school name : Hafez
		city name : Nikshahr, sistan & baloochestan, Iran
		Manager name : Parviz Arbabi
		Teacher name : Aslam Baloochjamaki
		Phone Number : -
		Phone Number coder : +989389339201
		school Adress : Nikshahr, khiyaban Moalem
		coder name : poorya samimi
		email coder : pooryasamimi@gmail.com

		''')
	time.sleep(30)
# end write function

# banner for application

banner ='''
		[++++++++++++++++++++++++++++++++++]
		[+]   dakhl & kharj for pepole   [+]
		[++++++++++++++++++++++++++++++++++]
'''
print(banner)
# start coded application

print ('''
			1. write Dakhl
			2. write Kharj
			3. read Dakhl
			4. read Kharj
			5. sood shoma
			6. About school
	''')
code = raw_input(">>> ")
#start if
if platform.system() == "Windows":
		os.system("color a")

if code == "1":
	text = raw_input("Value received : ")
	date = raw_input("What day : ")
	Name = raw_input("Your name : ")
	kar = raw_input("What practical : ")
	dakhl(text, date, Name, kar)

elif code == "2":
	text = raw_input("The amount spent : ")
	date = raw_input("dar che roozi : ")
	Name = raw_input("Your name : ")
	kar = raw_input("What practical : ")
	kharj(text, date, Name, kar)

elif code == "3":
	file = open("Dakhl.txt", "r")
	lines1 = file.readline()
	lines2 = file.readline()
	lines3 = file.readline()
	lines4 = file.readline()
	lines = lines1+lines2+lines3+lines4
	print(lines)
	time.sleep(30)

elif code == "4":
	file = open("Kharj.txt", "r")
	lines1 = file.readline()
	lines2 = file.readline()
	lines3 = file.readline()
	lines4 = file.readline()
	lines = lines1+lines2+lines3+lines4
	print(lines)
	time.sleep(30)
elif code == "5":
	dakhl_pool = raw_input("The amount you receive today : ")
	kharj_pool = raw_input("The amount spent today : ")
	sood(dakhl_pool, kharj_pool)
elif code == "6":
	About_schools_HAFEZ(code)
#end if
print(">>>>>>>>>>>>>>>>Good by<<<<<<<<<<<<<<<<<<")
