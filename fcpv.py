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

import sys
outdir=sys.argv[2]
import os
os.mkdir(outdir)
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
 if cv < 1:
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
  if cv < 1:
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
  if cv < 1:
#  if pv > 1.301029995664 and cv < 0.8:
# if pv > 1.3 and fcf < -1:
   if a != b and b != c and a != c:
    abcl=[str(a),str(b),str(c)]
    all=list(permutations(abcl,3))
    coma=all[0][0]+"_"+all[0][1]+"_"+all[0][2]
    comb=all[1][0]+"_"+all[1][1]+"_"+all[1][2]
    comc=all[2][0]+"_"+all[2][1]+"_"+all[2][2]
    comd=all[3][0]+"_"+all[3][1]+"_"+all[3][2]
    come=all[4][0]+"_"+all[4][1]+"_"+all[4][2]
    comf=all[5][0]+"_"+all[5][1]+"_"+all[5][2]
    if coma not in threedict and comb not in threedict and comc not in threedict and comd not in threedict and come not in threedict and comf not in threedict:
     threedict[coma]=[[fc,sg]]
    if coma in threedict and comb not in threedict and comc not in threedict and comd not in threedict and come not in threedict and comf not in threedict: 
     threedict[coma].append([fc,sg])
    if coma not in threedict and comb in threedict and comc not in threedict and comd not in threedict and come not in threedict and comf not in threedict:
     threedict[comb].append([fc,sg])
    if coma not in threedict and comb not in threedict and comc in threedict and comd not in threedict and come not in threedict and comf not in threedict:
     threedict[comc].append([fc,sg])
    if coma not in threedict and comb not in threedict and comc not in threedict and comd in threedict and come not in threedict and comf not in threedict:
     threedict[comd].append([fc,sg])
    if coma not in threedict and comb not in threedict and comc not in threedict and comd not in threedict and come in threedict and comf not in threedict:
     threedict[come].append([fc,sg])
    if coma not in threedict and comb not in threedict and comc not in threedict and comd not in threedict and come not in threedict and comf in threedict:
     threedict[comf].append([fc,sg])
threefile.close()

#the above code generated onedict, twodict, and threedict from NwiseFCPV.csv
#each dictionary is converted from sgRNA level to gene level
#there are 455 combinations stored in threedict
#############################################################################
co=0
for key in threedict:
 vallist=threedict[key][1:]
 fincom=[key,vallist]
 gene=key.split("_")
 a= gene[0]
 b= gene[1]
 c= gene[2]
 one=[a,onedict[a]]
 two=[b,onedict[b]]
 three=[c,onedict[c]]
 ab=a+"_"+b
 ba=b+"_"+a
 bc=b+"_"+c
 cb=c+"_"+b
 ac=a+"_"+c
 ca=c+"_"+a
 if ab in twodict:
  onetwo=[ab, twodict[ab]]
 elif ba in twodict: 
  onetwo=[ba, twodict[ba]]
 if bc in twodict:
  twothree=[bc,twodict[bc]]
 elif cb in twodict:
  twothree=[cb,twodict[cb]]
 if ac in twodict:
  onethree=[ac,twodict[ac]]
 elif ca in twodict:
  onethree=[ca,twodict[ca]] 
 name=a+"_"+b+"_"+c+".csv"
 table=open(name,"w")
 for i in fincom[1]:
  row=("three-wise"+","+"one_two_three"+","+i[0]+"\r\n")
  table.write(row)
 for i in onetwo[1]:
  row=("two-wise"+","+"one_two"+","+i[0]+"\r\n")
  table.write(row)
 for i in twothree[1]:
  row=("two-wise"+","+"two_three"+","+i[0]+"\r\n")
  table.write(row)
 for i in onethree[1]:
  row=("two-wise"+","+"one_three"+","+i[0]+"\r\n")
  table.write(row)
 for i in one[1]:
  row=("one-wise"+","+"one"+","+i[0]+"\r\n")
  table.write(row)
 for i in two[1]:
  row=("one-wise"+","+"two"+","+i[0]+"\r\n")
  table.write(row)
 for i in three[1]:
  row=("one-wise"+","+"three"+","+i[0]+"\r\n")
  table.write(row)
 table.close()

