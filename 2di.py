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

import sys
outfile=open(sys.argv[2],"w")
#Extract data from the input file
udict={}
one={}   
two=[]
rtwo={}
obsdict={}
with open(sys.argv[1],"r") as f:
 file= f.readlines()
for ln in file:
 if ln.startswith(">"):
  ln=ln.strip(">")
  ln=ln.strip("\r\n")
  ln= ln.split(",")
  if ln[0] not in udict:
   co=1
   udict[ln[0]]=[[float(ln[1]),co]]
  else:
   co+=1
   udict[ln[0]].append([float(ln[1]),co])
 else:
  ln=ln.strip("\r\n")
  ln=ln.split(",")
  i=ln[0].count("0")
  j=ln[0].count("1")
  k=ln[0].count("2")
  l=ln[0].count("3")
  coml=ln[0].split("+")
  coml.append(float(ln[1]))
  if i == 2:
   one["B"]=[[int(coml[1].strip("B")),coml[2]]]
   one["A"]=[[int(coml[0].strip("A")),coml[2]]]
   rtwo[0]=0
   obsdict[0]=coml[2]
  if i == 1:
   if "A0" in coml:
    one["B"].append([int(coml[1].strip("B")),coml[2]]) 
   if "B0" in coml:
    one["A"].append([int(coml[0].strip("A")),coml[2]])
  if i == 0:
   two.append(coml)
   if j == 2:
    rtwo[1]=coml[2]
   if k == 2:
    rtwo[2]=coml[2]
   if l == 2:
    rtwo[3]= coml[2]
print one    

#calculate the calculation of the IC uses the formula:
#(y2-y1)=m(x2-x1)-> find where the %survival locate in the fragment
#each fragment has a step size of 1, and x2 is always 0.
#point2/starting: (0,0.96); point1: (?,%survival)
#find the position of the fragment: 
#	(start_y-%survival)=((start_y-end_y)/1)*(0-?)
#Therefore, ?=(start_y-%survival)/(start_y-end_y) 
onedrugic={}
IC=sys.argv[3]
leftsur=1.0-(float(IC)/100.0)
expectedic=0
for d in one:
 lthan=[]
 mthan=[]
 for ec in one[d]:
  if ec[1] < leftsur:
   lthan.append(ec)
  else:
   mthan.append(ec)
 m= (mthan[-1][1]-lthan[0][1])/1
 y= mthan[-1][1]-leftsur
 startstep=mthan[-1][0]
 indvic=(y/m)+startstep
 onedrugic[d]=indvic
for d in onedrugic:
 expectedic+=onedrugic[d]
expectedic=expectedic/2
outfile.write("expected IC"+IC+","+str(expectedic)+"\r\n")

obsdict[2]=rtwo[1]
obsdict[1]=obsdict[0]-((obsdict[0]-obsdict[2])*0.5)
obsdict[3]=rtwo[2]-((rtwo[2]-rtwo[1])*0.5)
lthan=[]
mthan=[]
for d in obsdict:
 if obsdict[d] < leftsur: 
  lthan.append([d,obsdict[d]])
 else:
  mthan.append([d,obsdict[d]])
if len(mthan)>0:
 checkm=mthan[-1][1]-leftsur
 if checkm==0.0:
  obsic=mthan[-1][0]
if len(mthan) == 0:
 checkm=1.0
if len(lthan)>0:
 checkl=lthan[0][1]-leftsur
 if checkl==0.0:
  obsic=lthan[0][0]

if len(lthan)==0:
 checkl=1.0

if checkm != 0.0 and checkl != 0.0:
  y=mthan[-1][1]-leftsur
  m=(mthan[-1][1]-lthan[0][1])/1
  startstep=mthan[-1][0]
  obsic=(y/m)+startstep
outfile.write("observed IC"+IC+","+str(obsic)+"\r\n")
outfile.close()
