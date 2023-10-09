
#Textfile with current Timeatamp

import datetime;
file1 = open("D7textfile.txt","w")
file1.write("For this, we will use the DateTime module. First, import the module and then get the current time with date now() object.""\n")
file1.write("Now convert it into a string and then create a file with the file object like a regular file is created using file handling concepts in Python.")
file1.close()

time = datetime.datetime.now()
ts = time.timestamp()
print("Date and Time:- ",time)
print("Timestamp:- ",ts)

#print the text file in the console:

file2 = open("D7textfile.txt","r")
print(file2.read())
file2.close()