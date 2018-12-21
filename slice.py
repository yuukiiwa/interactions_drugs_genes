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

table=open("GIgene_slice_4c_table.csv","w")
file=open("genelvgi_table.csv","r")
for ln in file:
 size=ln[3]
 if size<0:
  size=-size
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 if ln[2]=="4":
  row=(ln[0]+","+ln[1]+","+ln[2]+","+str(ln[3])+","+str(size)+"\r\n")
  table.write(row)
table.close()

table=open("GIgene_slice_8c_table.csv","w")
file=open("genelvgi_table.csv","r")
for ln in file:
 size=ln[3]
 if size<0:
  size=-size
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 if ln[2]=="8":
  row=(ln[0]+","+ln[1]+","+ln[2]+","+str(ln[3])+","+str(size)+"\r\n")
  table.write(row)
table.close()

table=open("GIgene_slice_13c_table.csv","w")
file=open("genelvgi_table.csv","r")
for ln in file:
 size=ln[3]
 if size<0:
  size=-size
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 if ln[2]=="13":
  row=(ln[0]+","+ln[1]+","+ln[2]+","+str(ln[3])+","+str(size)+"\r\n")
  table.write(row)
table.close()

table=open("GIgene_slice_7c_table.csv","w")
file=open("genelvgi_table.csv","r")
for ln in file:
 size=ln[3]
 if size<0:
  size=-size
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 if ln[2]=="7":
  row=(ln[0]+","+ln[1]+","+ln[2]+","+str(ln[3])+","+str(size)+"\r\n")
  table.write(row)
table.close()

table=open("GIgene_slice_15c_table.csv","w")
file=open("genelvgi_table.csv","r")
for ln in file:
 size=ln[3]
 if size<0:
  size=-size
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 if ln[2]=="15":
  row=(ln[0]+","+ln[1]+","+ln[2]+","+str(ln[3])+","+str(size)+"\r\n")
  table.write(row)
table.close()
