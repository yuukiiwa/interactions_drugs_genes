import sys
fn=sys.argv[1]
ofn=fn.split(".")[0]+"GI.csv"

def addsgRNA(sgRNA,FC,sgDict):
 if sgRNA not in sgDict:
  sgDict[sgRNA]=[FC]
 else:
  sgDict[sgRNA].append(FC)
 return sgDict

def addCombo(ln,FC,comDict):
 combo=ln[0]+"-"+ln[1]
 revco=ln[1]+"-"+ln[0]
 if combo not in comDict and revco not in comDict:
  comDict[combo]=[FC]
 if combo in comDict:
  comDict[combo].append(FC)
 if revco in comDict:
  comDict[revco].append(FC)
 return comDict

def openFile(fn):
 sgDict, comDict={},{}
 file=open(fn,"r")
 header=file.readline().strip("\r\n").split(",")
 for ln in file:
  ln=ln.strip("\r\n").split(",")
  FC=float(ln[-1])
  #0->2; 1->3
  if ln[0] =="dummyguide" and ln[1] !="dummyguide":
   addsgRNA(ln[1],FC,sgDict)
  if ln[1] =="dummyguide" and ln[0] !="dummyguide":
   addsgRNA(ln[0],FC,sgDict)
  if ln[1] !="dummyguide" and ln[0] !="dummyguide":
   if ln[1] != ln[0]:
    addCombo(ln,FC,comDict)
 for sgRNA in sgDict:
  sgDict[sgRNA].append(sum(sgDict[sgRNA])/len(sgDict[sgRNA]))
 for combo in comDict:
  comDict[combo].append(sum(comDict[combo])/len(comDict[combo]))
 return (sgDict,comDict)
op=openFile(fn)
sgDict,comDict=op[0],op[1]  #the last item is the mean FC

def calcGI(sgDict,comDict):
 giDict={}
 for combo in comDict:
  sgs=combo.split("-")
  obs=comDict[combo][-1]
  exp=0
  for sg in sgs:
   if sg in sgDict:
    exp+=sgDict[sg][-1]
  GI=obs-exp
  giDict[combo]=(exp,obs,GI)
 return giDict
giDict=calcGI(sgDict,comDict)

def outFile(giDict,ofn):
 outfile=open(ofn,"w")
 outfile.write("gene combo,expected,observed,GI"+"\r\n")
 for combo in giDict:
  row=combo
  for i in giDict[combo]:
   row+=","+str(i)
  outfile.write(row+"\r\n")
 outfile.close()
outFile(giDict,ofn)
