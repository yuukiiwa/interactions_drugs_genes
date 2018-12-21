#3D heatmap of the phenotypic change
setwd("~/Downloads")
counts <- read.table("scale.csv", sep=",")
colnames(counts)<- c("xs","ys","sizes")
xs <-counts[,1]
ys <-counts[,2]
sizes<-counts[,3]
library(RColorBrewer)
library(plotly)
plot_ly(x = xs, y = ys, color = ys, size= sizes, colors = c("blue4","blue3","blue2","blue1","blue","honeydew","grey100","red"),marker= list(symbol = 'circle', sizemode = 'diameter'),sizes = c(2,10))
colnames(counts)<- c("first_gene","second_gene","third_gene","GI_score","sizes")
counts[0:5,]
first_gene <- counts[,1]
second_gene <- counts[,2]
third_gene <- counts[,3]
GI_score <- counts[,4]
sizes <- counts[,5]
library(RColorBrewer)
library(plotly)
plot_ly(type= "scatter3d", x= first_gene, y= second_gene, z=third_gene, mode="markers", size=5, marker= list(color= GI_score, showscale = TRUE))
plot_ly(type="scatter3d", x = first_gene, y = second_gene, z = third_gene,color = GI_score, size= sizes, colors = c("blue4","blue3","blue2","blue1","blue","honeydew","grey100","red"),marker= list(symbol = 'circle', sizemode = 'diameter'),sizes = c(2,10))

plotly_IMAGE(p, width = 500, height = 1500, format = "png", scale = 2,out_file = "~/desktop/gis.png")
#plot_ly(type= "scatter3d", x= first_gene, y= second_gene, z=third_gene, mode="markers", marker= list(color= GI_score, showscale = TRUE))


#scatter plot expected vs. observed sgRNA phenotypes
setwd("~/Downloads")
counts <- read.table("sgphenochange_table.csv", header=TRUE, sep=",")
colnames(counts)<- c("observed_phenotype","expected_phenotype","dummy_expected", "dummy_observed")
counts[0:5,]
observed_phenotype <- counts[,1]
expected_phenotype <- counts[,2]
dummy_expected <- counts[,3]
dummy_observed <- counts[,4]
plot(x=expected_phenotype, y= observed_phenotype,xlab= "expected phenotype", ylab= "observed phenotype",cex=0.1, col="black")%>%
 points(x=expected_phenotype, y= expected_phenotype, cex=0.1, col="navajowhite4")
library(plotly)
plot_ly(type="scatter", x = expected_phenotype, y = expected_phenotype)
plot_ly(type="scatter", x = expected_phenotype, y= observed_phenotype, name= "observed")%>%
  add_trace(y = expected_phenotype, name = 'expected',mode = 'markers')%>%
  add_trace(x = dummy_expected, y = dummy_observed, name = 'dummies',mode = 'markers')

setwd("~/Downloads")
counts <- read.table("maf15_dummy.csv", header=TRUE, sep=",")
colnames(counts)<- c("expected_phenotype", "observed_phenotype", "dummy_expected","dummy_observed", "expected_median","observed_median","expected_one", "observed_one", "exepected_two", "observed_two", "expected_three", "observed_three")
counts[0:5,]
expected_phenotype <- counts[,1]
observed_phenotype <- counts[,2]
dummy_expected <- counts[,3]
dummy_observed <- counts[,4]
expected_median <- counts[,5]
observed_median <- counts[,6]
expected_one <- counts[,7]
observed_one <- counts[,8]
expected_two <- counts[,9]
observed_two <- counts[,10]
expected_three <- counts[,11]
observed_three <- counts[,12]
library(plotly)

plot_ly(type="scatter", x = dummy_expected, y = dummy_observed , name = 'data',mode = 'markers')%>%
  add_trace(x = dummy_expected, y = dummy_observed, name = 'dummies',mode = 'markers')

# heatmap of the two-wise GI
setwd("~/Downloads")
counts <- read.table("GImap_onetwo_table.csv", header=TRUE, sep=",")
colnames(counts)<- c("first_gene","second_gene","GI_score")
counts[0:5,]
first_gene <- counts[,1]
second_gene <- counts[,2]
GI_score <- counts[,3]
library(plotly)
plot_ly(x= first_gene, y=second_gene, z = GI_score, type = "heatmap")

# heatmap of the three-wise GI
setwd("~/Downloads")
counts <- read.table("parts_GImap_table.csv", header=TRUE, sep=",")
colnames(counts)<- c("firstseond_genes","third_gene","GI_score")
counts[0:5,]
firstsecond_genes <- counts[,1]
third_gene <- counts[,2]
GI_score <- counts[,3]
library(plotly)
plot_ly(y= third_gene, x=firstsecond_genes, z = GI_score, type = "heatmap")

setwd("~/Downloads")
counts <- read.table("GImap_twothree_sorted_table.csv", sep=",")
temp <- data.matrix(counts)
head(temp)
heatmap(temp)

setwd("~/Downloads")
counts <- read.table("low_drug_size.csv", sep=",")
colnames(counts)<- c("A","B","C","di","s")
counts[0:5,]
A <- counts[,1]
B <- counts[,2]
C <- counts[,3]
di <- counts[,4]
s <- counts[,5]
library(RColorBrewer)
library(plotly)
plot_ly(type= "scatter3d", x= A, y= B, z= C, mode="markers", size=5, marker= list(color= di, showscale = TRUE))
plot_ly(type="scatter3d", x = A, y = B, z = C,size=s,color = di, colors = c("blue3","blue2","blue1","blue","black","yellow"),marker= list(symbol = 'circle', sizemode = 'diameter'),sizes = c(5,10))

# heatmap of the three-wise GI
setwd("~/Downloads")
counts <- read.table("GImap_capped_sorted_table.csv", header=TRUE, sep=",")
colnames(counts)<- c("firstseond_genes","third_gene","GI_score")
counts[0:48,]
firstsecond_genes <- counts[,1]
third_gene <- counts[,2]
GI_score <- counts[,3]
library(plotly)
plot_ly(x= third_gene, y=firstsecond_genes, z = GI_score, type = "heatmap")

setwd("~/Downloads")
counts <- read.table("pointone.csv", sep=",")
colnames(counts)<- c("combination","combinations","fold_change")
library(ggplot2)
df <- counts
df$combination <- as.factor(df$combination)
head(df)
p <- ggplot(df, aes(x=combination, y=fold_change)) + 
  geom_dotplot(aes(fill = combinations), binaxis='y', stackdir='center')+
  scale_fill_manual(values = c("navajowhite3","seagreen","black","palegreen3","olivedrab","khaki"))
p
mod1= lm(fold_change ~ combination, data= df)
summary(mod1)
anova(mod1)
confint(mod1)
mod=data.frame(Fitted= fitted(mod1), Residuals= resid(mod1), Treatment= df$combination)
ggplot(mod, aes(Fitted, Residuals, color=Treatment))+geom_point()
