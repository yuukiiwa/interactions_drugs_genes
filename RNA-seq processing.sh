trimmomatic
java -jar trimmomatic-0.39.jar PE -phred33 PZ-RNAseq-6_1.fastq.gz PZ-RNAseq-6_2.fastq.gz PZ_6_1_paired.fq.gz PZ_6_1_unpaired.fq.gz PZ_6_2_paired.fq.gz PZ_6_2_unpaired.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

STAR
./STAR --runThreadN 4 --runMode genomeGenerate --genomeDir /Users/awlab/Downloads/genome --genomeFastaFiles GRCh38.primary_assembly.genome.fa --sidbGTFfile gencode.v30.primary_assembly.annotation.gtf --sjdbOverhang 150
