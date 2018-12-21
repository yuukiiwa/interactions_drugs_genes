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

import math
firl=[]
sedl=[]
trdl=[]
earlyl=[]    #set A
latel=[]     #set B
changeavgl=[]
dumchel=[]
dumchll=[]
count=0
keys=[]
adict={}
bdict={}
odict={}
fp= open("newNGS_wCV.csv", "r")
for ln in fp:
 if "LOW" not in ln:
  if "#" not in ln:
   ln=ln.strip("\r\n")
   ln=ln.split(",")
   if "" not in ln: 
    fir=ln[0].strip('"')
    fird=int(fir)
    firl.append(fir)
    sed=ln[1]
    sedd=int(sed)
    sedl.append(sed)
    trd=ln[2].strip('"')
    trdd=int(trd)	
    trdl.append(trd)
    if float(ln[7])<0.5: 
     count+=1
     key=str(fir)+","+str(sed)+","+str(trd)
     dumch=fird+sedd+trdd
     earlych=((float(ln[4])/float(ln[3]))/1.30750177884)
     earlyl.append(earlych)
     latech=((float(ln[6])/float(ln[5]))/1.47627785284)
     latel.append(latech)
     changeavg=(earlych+latech)/2
     changeavgl.append(changeavg)
     if key not in adict:
       adict[key]=[earlych]
     else:
       adict[key].append(earlych)
     if key not in bdict:
       bdict[key]=[latech]
     else:
       bdict[key].append(latech)
     if dumch<5:
      dumchel.append(earlych)
      dumchll.append(latech)
     elif fir==1 and sed==2 and trd==2:
       dumchel.append(earlych)
       dumchll.append(latech)
     elif fir==2 and sed==2 and trd==1:
       dumchel.append(earlych)
       dumchll.append(latech)
     elif fir==2 and sed==1 and trd==2:
       dumchel.append(earlych)
       dumchll.append(latech)
     elif fir==2 and sed==2 and trd==2:
       dumchel.append(earlych)
       dumchll.append(latech)

ABmean=(sum(earlyl)+sum(latel))/(len(earlyl)+len(latel))
sa=[]
sb=[]
for a in earlyl:
 a=(a-ABmean)*(a-ABmean)
 sa.append(a)
for b in latel:
 b=(b-ABmean)*(b-ABmean)
 sb.append(b)
stddevi=math.sqrt((sum(sa)+sum(sb))/(len(sa)+len(sb)))
for k in adict:
  averagea=sum(adict[k])/len(adict[k])
  averageb=sum(bdict[k])/len(bdict[k])
  abavg=averagea+averageb/2
  cva=stddevi/averagea
  cvb=stddevi/averageb
  diff=cva-cvb
  if diff < 0:
    diff=(-1)*diff 
#  if diff < 0.5:
    odict[k]=[cva,cvb,abavg]

#table= open("2wise_nofilt__table.csv","w")
#for k in odict:
# l=k.split(",")
# if l[0]=="1":
#  x=str(odict[k][0])
#  y=str(odict[k][1])
#  z=str(odict[k][2])
#  row= (l[0]+","+l[1]+","+l[2]+","+z+"\r\n")
#  table.write(row)
#table.close()

table=open("newNGS_table.csv","w")
for x in range(0,count):
 row=(firl[x]+","+sedl[x]+","+trdl[x]+","+str(changeavgl[x])+","+str(earlyl[x])+","+str(latel[x])+"\r\n")
 table.write(row)
table.close()
 
