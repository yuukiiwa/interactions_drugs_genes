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
path="./turkey*.csv"
files=glob.glob(path)
tablea=open("tukey_additive.csv","w")
for name in files:
 with open(name) as f:
  ln=f.readline()
  dict={}
  for l in f:
   n=name.strip("./turkeyadditive")
   n=n.strip(".csv")
   print n
   l=l.split(",")
   com=l[0].strip('"')
   diff=l[1]
   lwr=l[2]
   upr=l[3]
   padj=l[4].strip("\r\n")
   r=[diff,lwr,upr,padj]
   dict[com]=r
  a="one-two"
  b="two-three"
  c="one-three"
  if a not in dict:
   a="two-one"
  if b not in dict:
   b="three-two"
  if c not in dict:
   c="three-one"
  rowa=(n+","+dict[a][0]+","+dict[a][1]+","+dict[a][2]+","+dict[a][3]+","+dict[b][0]+","+dict[b][1]+","+dict[b][2]+","+dict[b][3]+","+dict[c][0]+","+dict[c][1]+","+dict[c][2]+","+dict[c][3]+"\r\n")
  tablea.write(rowa)
tablea.close()

