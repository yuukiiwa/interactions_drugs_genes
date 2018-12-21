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

###############################################################
#generate a two-wise heatmap
###############################################################
file=open("GIscore_one_table.csv","r")
gionedict={}
checklist=[]
for ln in file:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 chk="("+ln[0]+","+ln[1]+","+ln[2]+")"
 checklist.append(chk)
 val=float(ln[3])
 ln=ln[0:3]
 ln.append(val)
 for i in ln:
  if type(i)!=float and  i != "1" and i != "2":
   k=i
 if k not in gionedict:
  gionedict[k]=[ln[3]]
 else:
  gionedict[k].append(ln[3])
gionemeandict={}
for k in gionedict:
 gionemean=sum(gionedict[k])/len(gionedict[k])
 gionemeandict[k]=gionemean

file=open("GIscore_two_table.csv","r")
twovalsdict={}
twomeandict={}
for ln in file:
 ln=ln.split(",")
 key=ln[0]+","+ln[1]+","+ln[2]
 val=ln[3].strip("\r\n")
 if "E" in val:
  val="0.0"
 val=float(val)
 if val != "-":
  key=key.split(",")
  if "(1" in key or "(2" in key:
   ak=key[1]+","+key[2].strip(")")
   bk=key[2].strip(")")+","+key[1]
  elif "1)" in key or "2)" in key:
   ak=key[0].strip("(")+","+key[1]
   bk=key[1]+","+key[0].strip("(")
  elif "1" in key[1] or "2" in key[2]:
   ak=key[0].strip("(")+","+key[2].strip(")")
   bk=key[2].strip(")")+","+key[0].strip("(")
   if ak not in twovalsdict:
    twovalsdict[ak]=[val]
   else: 
    twovalsdict[ak].append(val)
   if bk not in twovalsdict:
    twovalsdict[bk]=[val]
   else:
    twovalsdict[bk].append(val)
for k in twovalsdict:
 kl=k.split(",")
 normgi=(sum(twovalsdict[k])/len(twovalsdict[k]))-gionemeandict[kl[0]]
 twomeandict[k]=[kl[0],kl[1],normgi]
#table=open("GImap_onetwo_table.csv","w")
#for k in twomeandict:
# row=(twomeandict[k][0]+","+twomeandict[k][1]+","+str(twomeandict[k][2])+"\r\n")
# table.write(row)
#table.close()

################################################################
#Generate a three-wise heatmap
################################################################
#file=open("GIscore_three_table.csv","r")
file=open("cappedcom_table.csv","r")
threedict={}
for ln in file:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 a=ln[0].strip("(")
 b=ln[1]
 c=ln[2].strip(")")
 abk=a+"+"+b+","+c
 bak=b+"+"+a+","+c
 bck=b+"+"+c+","+a
 cbk=c+"+"+b+","+a
 cak=c+"+"+a+","+b
 ack=a+"+"+c+","+b
 val=ln[3]
 if val != "-":
  if "E" in val:
   val="0.0"
  val=float(val)
  if abk not in threedict:
   threedict[abk]=[val]
  else:
   threedict[abk].append(val)
  if bak not in threedict:
   threedict[bak]=[val]
  else:
   threedict[bak].append(val)
  if bck not in threedict:
   threedict[bck]=[val]
  else:
   threedict[bck].append(val)
  if cbk not in threedict:
   threedict[cbk]=[val]
  else:
   threedict[cbk].append(val)
  if cak not in threedict:
   threedict[cak]=[val]
  else:
   threedict[cak].append(val)
  if ack not in threedict:
   threedict[ack]=[val]
  else:
   threedict[ack].append(val)

file=open("GImap_onetwo_table.csv","r")
gibcdict={}
for ln in file:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 key=ln[0]+"+"+ln[1]
 val=float(ln[2])
 gibcdict[key]=val
bchl=[]
for k in threedict:
 nk=k.split(",")
 if nk[0] in gibcdict:
  a=nk[0].split("+")
  a=int(a[0])
  normgi=(sum(threedict[k])/len(threedict[k]))-gibcdict[nk[0]]
  bchl.append((a,nk[0],nk[1],normgi))
def takeFirst(elem):
 return elem[0]
bchl.sort(key=takeFirst)
print bchl
#table=open("GImap_twothree_sorted_table.csv","w")
table=open("GImap_capped_sorted_table.csv","w")
for k in bchl:
 row=(k[1]+","+k[2]+","+str(k[3])+"\r\n")
 table.write(row)
table.close()
