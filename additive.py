##under MIT license## 
#Copyright (c) 2018 Yuk Kei Wan
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

####Additive effect####################################################
#What is different in this program is the generation of the threedict #
#Instead of finding combinations without a repeating sgRNA            #
#This threedict only contains combinations that have 3 same sgRNA     #
#######################################################################
#if pv > 1.3 is to screen out the points below 0.05
from itertools import permutations
#generate a dictionary storing the fc values for the one-wise combinations
onefile=open("1wiseFCPVCVn2.csv","r")
onefile.readline()
onedict={}
for ln in onefile:
  ln=ln.strip("\r\n")
  ln=ln.split(",")
  sa=ln[0].strip('"')
  a= int(sa)-int(sa)/2
  a=str(a)
  sb=ln[1]
  b=int(ln[1])-int(ln[1])/2
  b=str(b)
  sc=ln[2].strip('"')
  c=int(sc)-int(sc)/2
  c=str(c)
  fc=ln[3]
  pv=float(ln[4])
  cv=float(ln[5])
  sg=sa+"_"+sb+"_"+sc
# if cv < 1:
# if pv > 1.3:
  if a != "1":
   if a not in onedict:
    onedict[a]=[[fc,sg]]
   else:
    onedict[a].append([fc,sg])
  if b != "1":
   if b not in onedict:
    onedict[b]=[[fc,sg]]
   else:
    onedict[b].append([fc,sg])
  if c != "1":
   if c not in onedict:
    onedict[c]=[[fc,sg]]
   else:
    onedict[c].append([fc,sg])
onefile.close()

#generate a dictionary storing the fc values of the two-wise combinations
twofile=open("2wiseFCPVCVn2.csv","r")
twofile.readline()
twodict={}
for ln in twofile:
 if "#V" not in ln:
   ln= ln.strip("\r\n")
   ln=ln.split(",")
   sa= ln[0].strip('"')
   a=int(sa)-int(sa)/2
   sb=ln[1]
   b= int(ln[1])-int(ln[1])/2
   sc= ln[2].strip('"')
   c= int(sc)-int(sc)/2
   fc= ln[3]
   pv= float(ln[4])
   cv= float(ln[5])
   sg=sa+"_"+sb+"_"+sc
#  if cv < 1:
# if pv > 1.3:
   ab= str(a)+"_"+str(b)
   ba= str(b)+"_"+str(a)
   bc= str(b)+"_"+str(c)
   cb= str(c)+"_"+str(b)
   ac= str(a)+"_"+str(c)
   ca= str(c)+"_"+str(a)
   if a == 1:
    if bc not in twodict and cb not in twodict:
     twodict[bc]=[[fc,sg]]
    elif cb in twodict:
     twodict[cb].append([fc,sg])
    elif bc in twodict:
     twodict[bc].append([fc,sg])
   if b == 1:
    if ac not in twodict and ca not in twodict:
     twodict[ac]=[[fc,sg]]
    elif ca in twodict:
     twodict[ca].append([fc,sg])
    elif ac in twodict:
     twodict[ac].append([fc,sg])
   if c == 1:
    if ab not in twodict and ba not in twodict:
     twodict[ab]=[[fc,sg]]
    elif ba in twodict:
     twodict[ba].append([fc,sg])
    elif ab in twodict:
     twodict[ab].append([fc,sg])
twofile.close()

#generate a dictionary storing the fc value of the three-wise combinations 
threefile=open("3wiseFCPVCVn2.csv","r")
threefile.readline()
threedict={}
for ln in threefile:
 if "#V" not in ln:
   ln=ln.strip("\r\n")
   ln=ln.split(",")
   sa=ln[0].strip('"')
   a= int(sa)-int(sa)/2
   sb=ln[1]
   b=int(ln[1])-int(ln[1])/2
   sc=ln[2].strip('"')
   c=int(sc)-int(sc)/2
   fc=ln[3]
   fcf=float(fc)
   pv= float(ln[4])
   cv= float(ln[5])
   sg=sa+"_"+sb+"_"+sc
#  if cv < 1:
#  if pv > 1.301029995664 and cv < 0.8:
# if pv > 1.3 and fcf < -1:
   if a == b and b == c and a == c:
    com=str(a)+"_"+str(b)+"_"+str(c)
    if com not in threedict:
     threedict[com]=[[fc,sg]]
    else:
     threedict[com].append([fc,sg])
threefile.close()
print threedict

for k in range(2,17):
 name="additive"+str(k)+".csv"
 table=open(name,"w")
 onek=str(k)
 twok=str(k)+"_"+str(k)
 thrk=str(k)+"_"+str(k)+"_"+str(k)
 for i in onedict[onek]:
  row=(i[1]+","+"one"+","+i[0]+"\r\n")
  table.write(row)
 for i in twodict[twok]:
  row=(i[1]+","+"two"+","+i[0]+"\r\n")
  table.write(row)
 for i in threedict[thrk]:
  row=(i[1]+","+"three"+","+i[0]+"\r\n")
  table.write(row)
 table.close()
