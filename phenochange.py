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
import collections
#worktable.csv is from worktable.py
#sgRNA_table.csv is from Nick's request
#[0][1][2] are the gene combinations
#[3] is the phenotypic change
#[4][5] are the phenotypes before and after respectively
file= open("newNGS_table.csv","r")
keydict={}   #stores all phenochange for all combinations
obsumdict={}   #stores the sum of the phenochange for all combinations
#note: obsumdict is also the OBSERVED 1/2/3-wise phenotypic change
for ln in file:
 ln=ln.split(",")
 pheno= float(ln[3])
 key="("+ln[0]+","+ln[1]+","+ln[2]+")"
 if key not in keydict:
  keydict[key]=[pheno]
 else:
  keydict[key].append(pheno)
for key in keydict:
 v=sum(keydict[key])
 if v < 0:     #if the v value is negative, turn all of them to be positive
  v=-v
  v=math.log(v,2)  #so that they can turn into their  log2 form 
  obsumdict[key]=-v  #put them into the dict with a negative sign
 else:
  obsumdict[key]=math.log(v,2)  #just log2 the positive ones 

indgenedict={}
for key in obsumdict:
 if '(1,1,' in key or ',1,1)' in key:
  ksplit=key.split(",")
  if "1)" not in ksplit[2]:
   genecona=ksplit[2].strip(")")
   if genecona not in indgenedict:
    indgenedict[genecona]=[obsumdict[key]]
   else:
    indgenedict[genecona].append(obsumdict[key])
  else:  
   geneconb=ksplit[0].strip("(")
   if geneconb not in indgenedict:
    indgenedict[geneconb]=[obsumdict[key]]
   else:
    indgenedict[geneconb].append(obsumdict[key])
 if '(2,2,' in key or ',2,2)' in key:
  ksplit=key.split(",")
  if "2)" not in ksplit[2]:
   genecona=ksplit[2].strip(")")
   if genecona not in indgenedict:
    indgenedict[genecona]=[obsumdict[key]]
   else:
    indgenedict[genecona].append(obsumdict[key])
  else:
   geneconb=ksplit[0].strip("(")
   if geneconb not in indgenedict:
    indgenedict[geneconb]=[obsumdict[key]]
   else:
    indgenedict[geneconb].append(obsumdict[key])
 if '(1,' in key and ',1)' in key:
  ksplit=key.split(",")
  if '1' not in ksplit[1]:
   geneconc=ksplit[1]
   if geneconc not in indgenedict:
    indgenedict[geneconc]=[obsumdict[key]]
   else:
    indgenedict[geneconc].append(obsumdict[key])
 if '(2,' in key and ',2)' in key:
  ksplit=key.split(",")
  if '2' not in ksplit[1]:
   geneconc=ksplit[1]
   if geneconc not in indgenedict:
    indgenedict[geneconc]=[obsumdict[key]]
   else:
    indgenedict[geneconc].append(obsumdict[key])

#the following calculations ignore the positional effect
indgenemeandict={}  #get the mean of the effect each individual genes bring
for key in indgenedict:
 meaneffect= sum(indgenedict[key])/len(indgenedict[key])
 indgenemeandict[key]= meaneffect
exsumdict={}
for a in indgenemeandict:
 va=indgenemeandict[a]
 for b in indgenemeandict:
  vb=indgenemeandict[b]
  for c in indgenemeandict:
   vc=indgenemeandict[c]
   key="({0},{1},{2})".format(a,b,c)
   exsum=va+vb+vc
   exsumdict[key]=exsum

##the median of dummy expected value is -0.23
##generate a 1-wise table
##one-wise data is normalized with -(-0.079)-(-0.079)
onedict={}
for key in obsumdict:
 normobsone=float(obsumdict[key])+0.079+0.079
 normexpone=float(exsumdict[key])+0.079+0.079
 if '(1,1,' in key or ',1,1)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(1,' in key and ',1)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(2,2,' in key or ',2,2)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(2,' in key and ',2)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(1,2,' in key or ',2,1)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(2,1,' in key or ',1,2)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(1,' in key and ',2)' in key:
  onedict[key]=[normobsone,normexpone]
 if '(2,' in key and ',1)' in key:
  onedict[key]=[normobsone,normexpone]
gionedict={}
for key in onedict:
 gione=onedict[key][0]-onedict[key][1]
 gionedict[key]=gione

##generate a two-wise table
twodict={}
for key in obsumdict:
 normobstwo=float(obsumdict[key])+0.079
 normexptwo=float(exsumdict[key])+0.079
 if '(1,1' not in key or ',1,1)' not in key:
  if '(2,2,' not in key or ',2,2)' not in key:
   if '(1,2,' not in key or ',2,1)' not in key:
    if '(2,1,' not in key or ',1,2)' not in key:
     if '(1,' in key or '(2,' in key:
      twodict[key]=[normobstwo,normexptwo]
     elif ',1)' in key or ',2)' in key:
      twodict[key]=[normobstwo,normexptwo]
     elif ',1,' in key or ',2,' in key:
      twodict[key]=[normobstwo,normexptwo]
gitwodict={}
for key in twodict:
 gitwo=twodict[key][0]-twodict[key][1]
 gitwodict[key]=gitwo

##generate three-wise table
threedict={}
for key in obsumdict:
 if key not in onedict:
  if key not in twodict:
   threedict[key]=[obsumdict[key],exsumdict[key]]
githreedict={}
for key in threedict:
 githree=threedict[key][0]-threedict[key][1]
 githreedict[key]=githree

##build a GI score dictionary
giscoredict={}
for key in gionedict:
 nkey=key.strip("(")
 nkey=nkey.strip(")")
 giscoredict[nkey]=gionedict[key]
for key in gitwodict:
 nkey=key.strip("(")
 nkey=nkey.strip(")")
 giscoredict[nkey]=gitwodict[key]
for key in githreedict:
 nkey=key.strip("(")
 nkey=nkey.strip(")")
 giscoredict[nkey]=githreedict[key]

combil=[]
for k in giscoredict:
 kl=k.split(",")
 combi=(kl[0],kl[1],kl[2],giscoredict[k])
 combil.append(combi)
def getZ(elem):
 return elem[2]
combil.sort(key=getZ)
#table=open("GIcube_slice30_table.csv","w")
#for i in combil:
# size=i[3]
# if size<0:
#  size=-size
# if i[2]=="30":
#  row=(i[0]+","+i[1]+","+i[2]+","+str(i[3])+","+str(size)+"\r\n")
#  table.write(row)
#table.close()

table=open("newsgGIbub_cvfil_table.csv","w")
for k in giscoredict:
 size=giscoredict[k]
 if size <0:
  size=-size
 row=(str(k)+","+str(giscoredict[k])+","+str(size)+"\r\n")
 table.write(row)
table.close()

#this writes the table for sgRNA phenotypic change
#table=open("phenocube_slice30_table.csv","w")
#for k in exsumdict:
# if k in obsumdict:
#  expvalue=exsumdict[k]
#  obsvalue=obsumdict[k]
#  key=k.strip("(")
#  key=key.strip(")")
#  i=key.split(",")
#  size=obsvalue
#  if size <0:
#   size=-obsvalue
#  if i[2]=="30":
#   row=(key+","+str(obsvalue)+","+str(size)+"\r\n")
#   table.write(row)
#table.close()

##writing a one-wise table
table=open('newonewise_table.csv','w')
for key in onedict:
 row=(str(key)+","+str(onedict[key][1])+","+str(onedict[key][0])+"\r\n")
 table.write(row)
table.close()
##writing a two-wise table
table=open("newtwowise_table.csv","w")
for key in twodict:
 row=(str(key)+","+str(twodict[key][1])+","+str(twodict[key][0])+"\r\n")
 table.write(row)
table.close()
##writing a three-wise table
table=open("newthreewise_table.csv","w")
for key in threedict:
 row=(str(key)+","+str(exsumdict[key])+","+str(obsumdict[key])+"\r\n")
 table.write(row)
table.close()

##sorting each phenotype into bin
#sortexpdict={} #[0] is the expected value, [1] is the observed value
#for k in exsumdict:
# if k in obsumdict:
#  sortexpdict[exsumdict[k]]=[obsumdict[k],k]
#od= collections.OrderedDict(sorted(sortexpdict.items()))
#table=open("sortbin_table.csv","w")
#for k, v in od.iteritems():
# row=(str(k)+","+str(v[0])+"\r\n")
# table.write(row)
#table.close()
#sorted_file=open("sortbin_table.csv","r")
#binlist=[]
#ebinlist=[]
#bin=[]
#ebin=[]
#sort_count=0
#for ln in sorted_file:
# ln=ln.strip("\r\n")
# ln=ln.split(",")
# sort_count+=1
# if sort_count < 101:
#  ebin.append(float(ln[0]))
#  bin.append(float(ln[1]))
# else:
#  sort_count=0
#  ebinlist.append(ebin)
#  binlist.append(bin)
#  ebin=[]
#  bin=[]
#medianlist=[]
#for bin in binlist:
# bin= sorted(bin)
# median=(bin[5]+bin[6])/2
# medianlist.append(median)
#table=open("obsmedian_list.csv","w")
#for i in medianlist:
# row=(str(i)+"\r\n")
# table.write(row)
#table.close()
#emedianlist=[]
#for ebin in ebinlist:
# ebin=sorted(ebin)
# emedian=(ebin[5]+ebin[6])/2
# emedianlist.append(emedian)
#table=open("expmedian_list.csv","w")
#for i in emedianlist:
# row=(str(i)+"\r\n")
# table.write(row)
#table.close()

##getting all the values for the dummies out
##dummydict[d][1]=expected, dummydict[d][0]=observed
#dummydict={}
#dummydict["(1,1,1)"]=[obsumdict["(1,1,1)"],exsumdict["(1,1,1)"]]
#dummydict["(1,2,2)"]=[obsumdict["(1,2,2)"],exsumdict["(1,2,2)"]]
#dummydict["(1,2,1)"]=[obsumdict["(1,2,1)"],exsumdict["(1,2,1)"]]
#dummydict["(1,1,2)"]=[obsumdict["(1,1,2)"],exsumdict["(1,1,2)"]]
#dummydict["(2,1,1)"]=[obsumdict["(2,1,1)"],exsumdict["(2,1,1)"]]
#dummydict["(2,2,1)"]=[obsumdict["(2,2,1)"],exsumdict["(2,2,1)"]]
#dummydict["(2,1,2)"]=[obsumdict["(2,1,2)"],exsumdict["(2,1,2)"]]
#dummydict["(2,2,2)"]=[obsumdict["(2,2,2)"],exsumdict["(2,2,2)"]]

#table=open("newGIdummy_table.csv","w")
#for d in dummydict:
# normexpdummy= float(dummydict[d][1])-0.2379
# normobsdummy= float(dummydict[d][0])-0.2379
# gidummy=normobsdummy-normexpdummy
# nd=d.strip("(")
# nd=nd.strip(")")
# row=(str(nd)+","+str(gidummy)+"\r\n")
# table.write(row)
#table.close()
