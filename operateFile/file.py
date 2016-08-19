import sys

f = open("./tmp.txt", "w")
f.write("i love yanqiu very much~")
print f.tell()
f.seek(5)
f.write("haha\n")
f.close()
f = open("./tmp.txt", "r")
print f.read()
f.close()

f = open("./tmp.txt")
for i in range(3):
	print str(i) + " : " + f.readline()

f.seek(1)
list = f.readlines()
print list
print "The line number of this file is: " + str(len(list))
f.close()
