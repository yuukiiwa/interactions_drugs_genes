#DeSeq2
library("DESeq2")
library("BiocParallel")
name<-"PZ_u_1a.csv"
metaname<-"PZ_u_1a_meta.csv"
outname<-"PZ_u_1a_stats.csv"
countTab<- as.matrix(read.csv(name,header=T, sep=",",row.names=1))
sampInfo<-read.csv(metaname,row.names=1)
all(rownames(sampInfo) %in% colnames(countTab))
all(rownames(sampInfo) == colnames(countTab))
dds <- DESeqDataSetFromMatrix(countData = countTab,colData = sampInfo,design = ~ condition)
dds <- DESeq(dds)
res <- results(dds)
register(MulticoreParam(4))
resOrdered <- res[order(res$pvalue),]
write.csv(as.data.frame(resOrdered), file=outname)

#Volcano plot
library(calibrate)
par(mfrow=c(2,4))
res <- read.table("PZ_u_1c_stats.csv", header=TRUE,sep=",")
with(res, plot(log2FoldChange, -log(padj), pch=20, main="no-drug (PZ1/8) vs 1c"))
with(subset(res, padj<.01 & abs(log2FoldChange)> 2), points(log2FoldChange, -log(padj), pch=20, col="green"))
abline(v=-2,h=-log(.05))
abline(v= 2,h=-log(.05))
with(res, plot(log2FoldChange, -log(padj), pch=20, main="no-drug vs 3-wise (PZ8/16)", xlim=c(-10,0),ylim=c(0,40)))
with(subset(res, padj<.05 & log2FoldChange< -1), points(log2FoldChange, -log(padj), pch=20, col="green"))
with(subset(res, padj<.05 & log2FoldChange< -1), textxy(log2FoldChange, -log10(pvalue), labs=gene, cex=.8))


