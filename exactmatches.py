import sys
def conSeq(seq):
 newseq=""
 for i in reversed(range(len(seq))):
  if seq[i] == "A":
   newseq+="T"
  if seq[i] == "T":
   newseq+="A"
  if seq[i] == "C":
   newseq+="G"
  if seq[i] == "G":
   newseq+="C"
 return newseq

fn="GCF_000001405.39_GRCh38.p13_genomic.fna"
def openFile(filename):
 file=open(filename,"r") #read the file
 everything=""
 dict={}
 for ln in file:
  if ln.startswith(">"):
   everything+=ln
  else:
   everything+=ln.strip("\n")
 everything=everything.split(">")
 for i in everything:
  i=i.split("\n")
  if len(i) == 2:
   header, seq=i[0], i[1]
   ref=header.split("(")[0].split(" ")[0]
   if ref.startswith("NC"):
    dict[ref]=(seq,conSeq(seq))
 return dict
dict=openFile(fn)
filename=sys.argv[1]
file=open(filename,"r")
ofn=filenames.split(".")[0]+"out.csv"
outfile=open(ofn,"w")
row="name,sgRNA"
for i in dict:
 row+=","+i
outfile.write(row+"\r\n")
for ln in file:
 ln=ln.strip("\r\n").split(",")
 row=ln[0]+","+ln[1]
 for a in dict:
  j=dict[a][0].count(ln[1])+dict[a][1].count(ln[1])
  row+=","+str(j)
 outfile.write(row+"\r\n")
outfile.close()
