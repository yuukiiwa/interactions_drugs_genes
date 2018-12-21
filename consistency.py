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

file=open("sgGIbub_table.csv","r")
hits=[(4,7,16),(16,4,8),(16,5,25),(25,6,15),(15,25,14),(16,14,25),(31,15,29),(32,16,30)]
dict={}
for ln in file:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 key=(int(ln[0]),int(ln[1]),int(ln[2]))
 val=ln[3]
 dict[key]=val
table=open("sgRNAconsistency.csv","w")
for hit in hits:
 a=hit[0]
 b=hit[1]
 c=hit[2]
 if (a,b,c) in dict:
  print (a,b,c), dict[(a,b,c)]
 if (b,a,c) in dict:
  print (b,a,c), dict[(b,a,c)]
 if (c,b,a) in dict:
  print (c,b,a), dict[(c,b,a)]
 if (b,c,a) in dict:
  print (b,c,a), dict[(b,c,a)]
 if (c,a,b) in dict:
  print (c,a,b), dict[(c,a,b)]
 if (a,c,b) in dict:
  print (a,c,b), dict[(a,c,b)]

 
