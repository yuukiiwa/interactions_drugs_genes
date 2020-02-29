import sys, regex
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

def twoMismatches(sgRNA,seq):
 restring='('+sgRNA+'){e<=4}'
 m=regex.findall(restring,seq,overlapped=True)
 tot=str(len(m))
 return tot

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
   if ref.startswith("NC_00"):
    dict[ref]=seq.strip("N")
 return dict
dict=openFile(fn)

filename=sys.argv[1]
file=open(filename,"r")
for ln in file:
 ln=ln.strip("\r\n").split(",")
 header=ln[0]+","+ln[1]
 print(header)
 for a in dict:
  sense=twoMismatches(ln[1],dict[a])
  anti=twoMismatches(conSeq(ln[1]),dict[a])
  line=a+","+sense+"_"+anti
  print(line)
