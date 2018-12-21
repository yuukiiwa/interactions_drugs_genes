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

import glob
path="./meanfc*.csv"
files=glob.glob(path)
tablea=open("m.csv","w")
d={}
for name in files:
 with open(name) as f:
  ln=f.readline()
  dict={}
  n=name.strip("./meanfc")
  n=n.strip(".csv")
  d[n]=[]
  for l in f:
   l=l.split(",")
   w=l[1].strip('"')
   m=l[2].strip("\r\n")
   dict[w]=m
  d[n].append(dict)

li= open("t.csv","r")
list=[]
for ln in li:
 ln=ln.strip("\r\n")
 list.append(ln)

a="one"
b="two"
c="three"
ab="one_two"
ac="one_three"
bc="two_three"
abc="one_two_three"

j=0
for n in list:
  rowa=(n+","+d[n][0][a]+","+d[n][0][b]+","+d[n][0][c]+","+d[n][0][ab]+","+d[n][j][ac]+","+d[n][j][bc]+","+d[n][j][abc]+"\r\n")
  tablea.write(rowa)
tablea.close()

   
   
