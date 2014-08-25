# KAOS contract generator
# By Vikram Ravindran 
#
# Release history:
# 1998        Original release (runs under Python 1.4)
#

import regex
import whrandom

studentlist=[]
numbered=[]
contracts={}

rand=whrandom.whrandom()

# This pattern was created to parse lines of the form:
# <tr><td><img align=middle src="RS-small.gif"><a href="JDOE.htm">John Doe</a></
td><td><a href="Boar.htm">Boarder</a></td></tr>
# from the school's website

namepat='<tr>.*>\([A-Za-z]+ [A-Za-z]+\)<'
prog=regex.compile(namepat)

fp=open('Grade12.HTM','r')

while 1:
    line = fp.readline()
    if line=="": break
    if prog.search(line)!=-1:
        studentlist.append(prog.group(1))

fp.close()
while 1:
    if len(studentlist)==0: break
    randnum = rand.randint(0,len(studentlist)-1)
    numbered.append(studentlist[randnum])
    del(studentlist[randnum])


for index in range(0,len(numbered)-1):
    contracts[numbered[index]]=numbered[index+1]

contracts[numbered[len(numbered)-1]] = numbered[0]

eliminators = contracts.keys()
eliminators.sort()


fp=open('contract.txt','w')

for index in eliminators:
    fp.write("%s will eliminate %s\n" % (index,contracts[index]))

fp.close()

