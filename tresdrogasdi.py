##under GNU license## 
##drug interaction calculation described in Cokol et al. (2017)

import sys
IC=sys.argv[1]
fname=sys.argv[2]
outfile=sys.argv[3]
file=open(fname,"r")
one={}
two=[]
three=[]
dosl=[]
dcalc={}
l=file.readline()
l=l.strip("\r\n")
l=l.split(",")
nodrugadded=[l[0],float(l[1])]
cb=l[0].split("+")
combo=cb[0][0]+cb[1][0]+cb[2][0]
sec=cb[1][0]
secone=cb[1][0]+"1"
firtwo=cb[0][0]+"2"
thrtwo=cb[2][0]+"2"
dcom=l[0].split("+")
for d in dcom:
 one[d[0]]=[[int(d[1]),float(l[1])]]
for ln in file:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 com=ln[0].split("+")
 o= ln[0].count("0")
 n= ln[0].count("1")
 p= ln[0].count("2")
 if o==2:
  for d in com:
   if "0" not in d:
     one[d[0]].append([int(d[1]),float(ln[1])])
 if o==1:
  for d in com:
   if "0" in d:
    com.remove(d)
  two.append([com[0], com[1], ln[1]])
 if o==0:
  three.append([com[0],com[1],com[2],ln[1]])
 if fname != "rtf.csv" and fname !="afe.csv":
  if n==3:
   tresunas=[ln[0],float(ln[1])]
  if p==2 and o==1:
   for d in com:
    if "0" in d:
     com.remove(d)
   dosl.append([com[0],com[1],float(ln[1])])   
 else:
  if n==2 and "2" in com[1]:
   tresunas=[ln[0],float(ln[1])]
  if o==1:
   if p==2:
    dosl.append([com[0],com[1]])
    for d in com:
     if sec in d:
      na=com[0][0]+com[1][0]
      dcalc[na].append(float(ln[1]))
      num=dcalc[na][0]+dcalc[na][1]
      dosl[-1].append(num)
     else:
      dosl[-1].append(float(ln[1]))
   if p==1 and n==1:
    for d in com:
     if secone == d:
      na=com[0][0]+com[1][0]
      dcalc[na]=[float(ln[1])]

#############################################
#expected ic location on scale 0-3
#############################################
onedrugic={}
IC=float(IC)
leftsur=1.00-(IC/100.0)
expectedic=0
bli=[]
for d in one:
 li=[]
 mthan=[]
 lthan=[]
 li.append(d)
 for ec in one[d]:
  li.append(ec[1])
  if ec[1] < leftsur:
   lthan.append(ec)
  elif ec[1] > leftsur:
   mthan.append(ec)
  elif ec[1]==leftsur:
   indvic=ec[0]
 bli.append(li)
 if len(mthan)>0 and len(lthan)>0:
  m= (mthan[-1][1]-lthan[0][1])/1
  y= mthan[-1][1]-leftsur
  startstep=mthan[-1][0]
  indvic=(y/m)+startstep
  onedrugic[d]=indvic
 elif len(mthan)==0 or len(lthan)==0:
  onedrugic[d]=indvic

for d in onedrugic:
 expectedic+=onedrugic[d]
expectedic=expectedic/3
#print ("expected ic: "+str(expectedic))
#two-wise expected ICs
dosexpic=[]
k=onedrugic.keys()
dosexpic=[]
deic=((onedrugic[k[0]]+onedrugic[k[1]])/2)
dosexpic.append([k[0],k[1],deic])
deic=((onedrugic[k[1]]+onedrugic[k[2]])/2)
dosexpic.append([k[1],k[2],deic])
deic=((onedrugic[k[0]]+onedrugic[k[2]])/2)
dosexpic.append([k[0],k[2],deic])

###############################################
#observed ic of 3-wise combination on scale 0-3
###############################################
uno=1-(((nodrugadded[1]-tresunas[1])/3)*1)
dos=1-(((nodrugadded[1]-tresunas[1])/3)*2)
obs=[]
obs.append(nodrugadded[1])
obs.append(uno)
obs.append(dos)
obs.append(tresunas[1])
mthan=[]
lthan=[]
c=0
for ec in obs:
 if ec < leftsur:
  lthan.append([c,ec])
 if ec > leftsur:
  mthan.append([c,ec])
 if ec== leftsur:
  obsic=ec
 c+=1
if len(mthan)>0 and len(lthan)>0:
 m= (mthan[-1][1]-lthan[0][1])/1
 y= mthan[-1][1]-leftsur
 startstep=mthan[-1][0]
 obsic= (y/m)+startstep
elif len(mthan)==0 or len(lthan)==0:
 obsic=leftsur

################################################
#observed ic of 2-wise combinations in scale 0-3
################################################
dosdict={}
for com in dosl:
 dob=[]
 yyamo=com[0][0]+com[1][0]
 dosdos=com[2]
 uno=1-(((nodrugadded[1]-dosdos)/3)*1)
 dos=1-(((nodrugadded[1]-dosdos)/3)*2)
 dob.append(nodrugadded[1])
 dob.append(uno)
 dob.append(dos)
 dob.append(dosdos)
 dosdict[yyamo]=[dob]
for k in dosdict:
 mthan=[]
 lthan=[]
 c=0
 for ec in dosdict[k][0]:
  if ec < leftsur:
   lthan.append([c,ec])
  if ec > leftsur:
   mthan.append([c,ec])
  if ec == leftsur:
   print ec
   obic= ec
  c+=1
 if len(mthan)>0 and len(lthan)>0:
  m= (mthan[-1][1]-lthan[0][1])/1
  y= mthan[-1][1]-leftsur
  startstep=mthan[-1][0]
  obic=(y/m)+startstep
  dosdict[k].append(obic)
 elif len(mthan)==0 or len(lthan)==0:
  dosdict[k].append(leftsur)
for l in dosexpic:
 llamo=l[0]+l[1]
 if llamo in dosdict:
  dosdict[llamo].append(l[2])
 if llamo not in dosdict:
  llamo=l[1]+l[0]
  dosdict[llamo].append(l[2])

###########################################
table=open(outfile,"w")
for i in bli:
 p=str(i[1:])
 p=p.strip("[")
 p=p.strip("]")
 row= (i[0]+","+p+"\r\n")
 table.write(row)
for k in dosdict:
 p=str(dosdict[k][0])
 p=p.strip("[")
 p=p.strip("]")
 row=(k+","+p+"\r\n")
 table.write(row)
p=str(obs)
p=p.strip("[")
p=p.strip("]")
row= (combo+","+ p+"\r\n")
table.write(row)
for d in onedrugic:
 row=(d+" individual IC"+str(int(IC))+","+str(onedrugic[d])+"\r\n")
 table.write(row)
for k in dosdict:
 row=(k+" expected IC"+str(int(IC))+","+str(dosdict[k][2])+"\r\n")
 table.write(row)
 row=(k+" observed IC"+str(int(IC))+","+str(dosdict[k][1])+"\r\n")
 table.write(row)
row=(combo+" expected IC"+str(int(IC))+","+str(expectedic)+"\r\n")
table.write(row)
row=(combo+" observed IC"+str(int(IC))+","+str(obsic)+"\r\n")
table.write(row)
table.close()
