files <- list.files(pattern = "*.csv$")
files

for(i in 1:length(files)){
  counts <- read.table(file = files[i],sep=",")
  colnames(counts)<- c("combination","combinations","fold_change")
  library(ggplot2)
  df <- counts
  df$combinations <- as.factor(df$combinations)
  head(df)
  ggplot(df, aes(x=combinations, y=fold_change)) + 
    geom_dotplot(aes(fill = combinations), binaxis='y', stackdir='center')+
    scale_fill_manual(values = c("navajowhite3","seagreen","black","palegreen3","olivedrab","khaki","green"))
  namea= paste(files[i],"o5.png",sep="")
  ggsave(namea,width = 10, height = 10, units="in")
  mod1= lm(fold_change ~ combinations, data= df)
  summary(mod1)
  anova(mod1)
  confint(mod1)
  btwn <- aov(fold_change ~ combinations, data=df)
  summary(btwn)
  res <- TukeyHSD(btwn,"combinations", ordered = TRUE)
  turkey= as.data.frame(res$combinations)
  mod=data.frame(Fitted= fitted(mod1), Residuals= resid(mod1), Treatment= df$combinations)
  ggplot(mod, aes(Fitted, Residuals, color=Treatment))+geom_point()
  nameb=paste(files[i],"o5ad.png",sep="") 
  ggsave(nameb,width = 2.5, height = 2.5, units="in")
  reportname= paste("turkey",files[i],sep="")
  print(reportname)
  write.csv(turkey, file = reportname)}


files <- list.files(pattern = "*.csv$")
files
library(DescTools)
for(i in 1:length(files)){
  counts <- read.table(file = files[i],sep=",")
  colnames(counts)<- c("combination","combinations","fold_change")
  df <- counts
  df$combinations <- as.factor(df$combinations)
  mod1= lm(fold_change ~ combinations, data= df)
  summary(mod1)
  anova(mod1)
  confint(mod1)
  btwn <- aov(fold_change ~ combinations, data=df)
  summary(btwn)
  res<- DunnettTest(fold_change ~ combinations, data=df, control="one_two_three")
  dunnett= as.data.frame(res[["one_two_three"]])
  reportname= paste("Dunnett",files[i],sep="")
  print(reportname)
  write.csv(dunnett, file = reportname)}

files <- list.files(pattern = "*.csv$")
files
library(DescTools)
for(i in 1:length(files)){
  counts <- read.table(file = files[i],sep=",")
  colnames(counts)<- c("combination","combinations","fold_change")
  df <- counts
  df$combinations <- as.factor(df$combinations)
  res<-aggregate(df[, 3], list(df$combinations), mean)
  m= as.data.frame(res)
  reportname= paste("meanfc",files[i],sep="")
  print(reportname)
  write.csv(m, file = reportname)}
