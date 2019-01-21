onefile= open("di1wise.csv","r")
onedict={}
for ln in onefile:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 conc=float(ln[0])
 comb=ln[1]
 inhi=float(ln[2])
 if comb not in onedict:
  onedict[comb]=[[inhi,conc]]
 else:
  onedict[comb].append([inhi,conc])
twofile= open("di2wise.csv","r")
twodict={}
for ln in twofile:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 conc=float(ln[0])
 comb=ln[1]
 inhi=float(ln[2])
 if comb not in twodict:
  twodict[comb]=[[inhi,conc]]
 else:
  twodict[comb].append([inhi,conc])
thrfile=open("di3wise.csv","r")
thrdict={}
for ln in thrfile:
 ln=ln.strip("\r\n")
 ln=ln.split(",")
 conc=float(ln[0])
 comb=ln[1]
 inhi=float(ln[2])
 if comb not in thrdict:
  thrdict[comb]=[[inhi,conc]]
 else:
  thrdict[comb].append([inhi,conc])

#find where the one-wise IC locates
ic= float(43)
oneic={}
for k in onedict:
 lthan=[]
 mthan=[]
 for c in onedict[k]:
  if c[0] < ic:
   lthan.append(c)
  else:
   mthan.append(c)
 startstep=lthan[-1][1]
 endstep=mthan[0][1]
 stepsize=endstep-startstep
 stepdiff=mthan[0][0]-lthan[-1][0]
 dvfromic=ic-lthan[-1][0]
 obsic=startstep+((dvfromic/stepdiff)*stepsize)
 oneic[k]=obsic #the location of the ic
########################################
twoics={}
for k in twodict:
 kl=k.split("_")
 ica=oneic[kl[0]]
 icb=oneic[kl[1]]
 expic=(ica+icb)/2.0
 lthan=[]
 mthan=[]
 for c in twodict[k]:
  if c[0]<43.0:
   lthan.append(c)
  else:
   mthan.append(c)
 startstep=lthan[-1][1]
 endstep=mthan[0][1]
 stepsize=endstep-startstep
 stepdiff=mthan[0][0]-lthan[-1][0]
 dvfromic= 43.0-lthan[-1][0]
 obsic=startstep+((dvfromic/stepdiff)*stepsize)
 fic=obsic/expic
 twoics[k]=[obsic,expic,fic]
##############################################
thrics={}
for k in thrdict:
 kl=k.split("_")
 ica=oneic[kl[0]]
 icb=oneic[kl[1]]
 icc=oneic[kl[2]]
 expic=(ica+icb+icc)/3.0
 mthan=[]
 lthan=[]
 for c in thrdict[k]:
  if c[0]<43.0:
   lthan.append(c)
  else:
   mthan.append(c)
 startstep=lthan[-1][1]
 endstep=mthan[0][1]
 stepsize=endstep-startstep
 stepdiff=mthan[0][0]-lthan[-1][0]
 dvfromic=43.0-lthan[-1][0]
 obsic=startstep+((dvfromic/stepdiff)*stepsize)
 fic=obsic/expic
 thrics[k]=[obsic,expic,fic]
###############################################
table=open("fullresults.csv","w")
row=("combo"+","+"FIC"+","+"exp ic"+","+"obs ic"+"\r\n")
for k in thrics:
 row= (k+","+str(thrics[k][2])+","+str(thrics[k][1])+","+str(thrics[k][0])+"\r\n")
 table.write(row)
 kl=k.split("_")
 ca=kl[0]+"_"+kl[1]
 cb=kl[1]+"_"+kl[2]
 cc=kl[0]+"_"+kl[2]
 if ca not in twoics:
  ca=kl[1]+"_"+kl[0]
 if cb not in twoics:
  cb=kl[2]+"_"+kl[1]
 if cc not in twoics:
  cc=kl[2]+"_"+kl[0]
 row=(ca+","+str(twoics[ca][2])+","+str(twoics[ca][1])+","+str(twoics[ca][0])+"\r\n")
 table.write(row)
 row=(cb+","+str(twoics[cb][2])+","+str(twoics[cb][1])+","+str(twoics[cb][0])+"\r\n")
 table.write(row)
 row=(cc+","+str(twoics[cc][2])+","+str(twoics[cc][1])+","+str(twoics[cc][0])+"\r\n")
 table.write(row)
 row=(kl[0]+","+"_"+","+"_"+","+str(oneic[kl[0]])+"\r\n")
 table.write(row)
 row=(kl[1]+","+"_"+","+"_"+","+str(oneic[kl[1]])+"\r\n")
 table.write(row)
 row=(kl[2]+","+"_"+","+"_"+","+str(oneic[kl[2]])+"\r\n")
 table.write(row)
table.close()
