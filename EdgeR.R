##EdgeR code
library(edgeR)
library(limma)
library(RColorBrewer)
library(mixOmics)
library(HTSFilter)
rawCountTable <- read.table("PZ_u_EF.csv", header=TRUE, sep=",", row.names=1)
sampleInfo <- read.table("PZ_u_2c_meta.csv", header=TRUE, sep=",", row.names=1)
all(rownames(sampleInfo) %in% colnames(rawCountTable))
all(rownames(sampleInfo) == colnames(rawCountTable))
dgeFull <- DGEList(rawCountTable, group=sampleInfo$condition)
pseudoCounts <- log2(dgeFull$counts+1)
sampleDists <- as.matrix(dist(t(pseudoCounts)))
dgeFull <- DGEList(dgeFull$counts[apply(dgeFull$counts, 1, sum) != 0, ],
                   group=dgeFull$samples$group)
dgeFull <- calcNormFactors(dgeFull, method="TMM")
eff.lib.size <- dgeFull$samples$lib.size*dgeFull$samples$norm.factors
normCounts <- cpm(dgeFull)
pseudoNormCounts <- log2(normCounts + 1)
dgeFull <- estimateCommonDisp(dgeFull)
dgeFull <- estimateTagwiseDisp(dgeFull)
dgeTest <- exactTest(dgeFull)
filtData <- HTSFilter(dgeFull)$filteredData
dgeTestFilt <- exactTest(filtData)
resNoFilt <- topTags(dgeTest, n=nrow(dgeTest$table))
resFilt <- topTags(dgeTestFilt, n=nrow(dgeTest$table))
sum(resNoFilt$table$FDR < 1)
sum(resFilt$table$FDR < 1)
sigDownReg <- resFilt$table[resFilt$table$FDR<10,]
sigDownReg <- sigDownReg[order(sigDownReg$logFC),]
write.csv(sigDownReg, file="sigReg_EF.csv")

#sigDownReg <- resFilt$table[resFilt$table$FDR<0.05,]

#venn diagram
library(limma)
###the table being read in is only FDR(0.05)-filtered
countTab<- read.table("pathways_venn.csv",header=T, sep=",")
par(mfrow=c(2,2))
##0.5849: 50% upregulated  ##-1: 50% downregulated
##0.3781: 30% upregulated  ##-0.5145: 30% downregulated
##0.3219: 25% upregulated  ##-0.4150: 25% downregulated
##this part filters the 3-way FC based on the percent FC
upfc<- 1
utitle<- "Pathways (20% up-/down-regulated genes)"
dpfc<- 
dtitle<-"50% downregulated"
AE <- (countTab$AE >= upfc)
AF <- (countTab$AF >= upfc)
EF <- (countTab$EF >= upfc)
AEF <- (countTab$AEF >= upfc)
c3 <- cbind(AE, AF, EF,AEF)
a <- vennCounts(c3)
vennDiagram(a,counts.col=c("red", "blue"),circle.col = c("red", "blue", "orange","green"), main=utitle)
AE <- (countTab$AE <= dpfc)
AF <- (countTab$AF <= dpfc)
EF <- (countTab$EF <= dpfc)
AEF <- (countTab$AEF <= dpfc)
c3 <- cbind(AE, AF, EF,AEF)
a <- vennCounts(c3)
vennDiagram(a,counts.col=c("red", "blue"),circle.col = c("red", "blue", "orange","green"), main=dtitle)

##heatmap w/o clustering
##the input files are pt#FCgenes_heatmap.csv with lgFC filter of either 25-,30-, or 50-percent fold change
library("tidyr")
library(reshape2)
countTab<- read.table("pvalgenes_melt.csv",header=T, sep=",")
table <- data.frame(y = c("AE", "AF","EF", "AEF"))
table$y <- factor(table$x, levels = c("AE", "AF","EF", "AEF"))
library(plotly)
plot_ly(x=countTab$GO,y=countTab$combo, z=countTab$pval,colors = colorRamp(c("orange","yellow","grey")), type = "heatmap")%>%
  layout(yaxis = list(categoryorder = "trace"))

library(gplots)
y<- as.matrix(read.table("pvalgenes_matrix.csv",header=T,row.names = 1, sep=","))
mycol <- colorpanel(40, "orange", "yellow","grey")
heatmap.2(y, col=mycol,scale="row", density.info="none", trace="none")


##heatmap w/ clustering
##the input file is the matrix generating the venn diagrams w/ all the missing 2-way entries eliminated
library(gplots)
y<- as.matrix(read.table("no0in3_nrepFCgenes_matrix.csv",header=T,row.names = 1, sep=","))
y<- as.matrix(read.table("ngsfcHeatmap.csv",header=T,row.names = 1, sep=","))
hc <- hclust(as.dist(1-cor(y, method="pearson")), method="complete")
mycol <- colorpanel(40, "blue", "black", "yellow")
heatmap.2(y,dendrogram="row",col=mycol,density.info="none", trace="none",key=F, cexRow = 0.45, cexCol=0.75,ylab = "combinations", xlab = "GI scores")
heatmap.2(y,  Colv=as.dendrogram(hc), col=mycol,scale="row", density.info="none", trace="none",key=F, cexRow = 0.45, cexCol=0.75,  key.xlab = "log2 fold change",key.title = "Color Scale",ylab = "combinations", xlab = "GI scores")
heatmap.2(y, dendrogram="row",  Colv=FALSE, col=mycol,scale="row", density.info="none", trace="none",key=F, cexRow = 0.45, cexCol=0.75,  key.xlab = "log2 fold change",key.title = "Color Scale",ylab = "combinations", xlab = "GI scores")

#histograms
par(mfrow=c(1,4))
y<- read.table("Azimuth2_FORECasT_inDelphi_Brunello.csv", header=T, sep=",")
plot(y$Azimuth,y$FORECasT, breaks=50,main="Brunello",ylab="FORECasT",xlab="Azimuth",cex=0.1)
y<- read.table("Azimuth2_FORECasT_inDelphi_Yusa.csv", header=T, sep=",")
plot(y$Azimuth,y$FORECasT, breaks=50,main="Yusa",ylab="FORECasT",xlab="Azimuth",cex=0.1)
y<- read.table("Azimuth2_FORECasT_inDelphi_Toronto.csv", header=T, sep=",")
plot(y$Azimuth,y$FORECasT, breaks=50,main="Toronto",ylab="FORECasT",xlab="Azimuth",cex=0.1)
y<- read.table("Azimuth2_FORECasT_inDelphi_Bassik.csv", header=T, sep=",")
plot(y$Azimuth,y$FORECasT, breaks=50,main="Bassik",ylab="FORECasT",xlab="Azimuth",cex=0.1)
h <- hist(y, breaks=300, plot=FALSE)
cuts <- cut(h$breaks, c(-Inf,-.20))
h$density = (h$counts/sum(h$counts))*100
plot(h, col=cuts, main="Observed-Expected FC ", xlab="GI scores", ylab="% of total (455)",freq=FALSE)


