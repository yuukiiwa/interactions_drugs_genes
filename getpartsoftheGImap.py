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

file=open("GImap_twothree_sorted_table.csv","r")
list=[]
dict={}
nickkeys=["4,7,16","16,4,8","25,6,15","16,5,25","16,14,25","15,25,14","31,15,29","32,16,30"]
for ln in file:
 ln=ln.split(",")
 com=ln[0].split("+")
 if com[0]=="15" and com[1]=="25":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="16" and com[1]=="5":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="16" and com[1]=="4":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="16" and com[1]=="14":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="4" and com[1]=="7":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="31" and com[1]=="15":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="32"and com[1]=="16":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
 if com[0]=="25" and com[1]=="6":
  row=(ln[0]+","+ln[1]+","+ln[2]+"\r\n")
  list.append(row)
  key=com[0]+","+com[1]+","+ln[1]
  dict[key]=ln[2]
table=open("parts_GImap_table.csv","w")
for row in list:
 table.write(row)
table.close()
for k in nickkeys:
 print k, dict[k]
  
