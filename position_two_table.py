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

file= open("twowise_table.csv","r")
list=[]
dict={}
for ln in file:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 if "(1" in ln or "(2" in ln:
  ln=ln[1:]
 elif "1)" in ln or "2)" in ln:
  del ln[2]
 elif "1" in ln or "2" in ln:
  del ln[1]
 key=ln[0]+","+ln[1]
 val=float(ln[3])
 if key not in dict:
  dict[key]=[val]
 else:
  dict[key].append(val)
avgdict={}
for k in dict:
 avg=sum(dict[k])/len(dict[k])
 avgdict[k]=avg

acdict={}
bcdict={}
abdict={}
for co in avgdict:
 if "(" in co and ")" in co:
  c=co.split(",")
  a=c[0].strip("(")
  b=c[1].strip(")")
  k=a+","+b
  alk=b+","+a
  if k not in acdict and alk not in acdict:
   acdict[k]=[avgdict[co]]
  elif alk in acdict and k not in acdict:
   acdict[alk].append(avgdict[co])
 elif "(" not in co and ")" in co:
  c=co.split(",")
  a=c[0]
  b=c[1].strip(")")
  k=a+","+b
  alk=b+","+a
  if k not in bcdict and alk not in bcdict:
   bcdict[k]=[avgdict[co]]
  elif alk in bcdict and k not in bcdict:
   bcdict[alk].append(avgdict[co])
 elif "(" in co and ")" not in co:
  c=co.split(",")
  a=c[0].strip("(")
  b=c[1]
  k=a+","+b
  alk=b+","+a
  if k not in abdict and alk not in abdict:
   abdict[k]=[avgdict[co]]
  elif alk in abdict and k not in abdict:
   abdict[alk].append(avgdict[co])

table=open("abPHEposition_table.csv","w")
for k in abdict:
 if len(abdict[k])==2:
  row=(k+","+str(abdict[k][0])+","+str(abdict[k][1])+"\r\n")
  table.write(row)
table.close()

table=open("bcPHEposition_table.csv","w")
for k in bcdict:
 if len(bcdict[k])==2:
  row=(k+","+str(bcdict[k][0])+","+str(bcdict[k][1])+"\r\n")
  table.write(row)
table.close()

table=open("acPHEposition_table.csv","w")
for k in acdict:
 if len(acdict[k])==2:
  row=(k+","+str(acdict[k][0])+","+str(acdict[k][1])+"\r\n")
  table.write(row)
table.close()
