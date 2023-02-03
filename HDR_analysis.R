# https://www.datanovia.com/en/fr/lessons/test-de-wilcoxon-dans-r/


library(tidyverse)
library(rstatix)
library(ggpubr)
setwd('/work/shared/ptbc/CNN_Pancreas_V2/Exome_TCGA/scripts/')

mut_cna<-read.csv('mut_cna.csv')
mutSig<-read.csv('mutSig.csv')
ch_data<-read.csv('ch_data.csv')


#----------------> wilcoxon 

# mut_cna
library(gtsummary)
tbl_summary(
  mut_cna[-1],
  by=pred_dicho,
  missing = 'no',
) %>%
  add_n() %>%
  add_p() %>%
  modify_header(label = "**Variable**") %>%
  bold_labels()

# mutSig
tbl_summary(
  mutSig[-1],
  by=pred_dicho,
  missing = 'no',
) %>%
  add_n() %>%
  add_p() %>%
  modify_header(label = "**Variable**") %>%
  bold_labels()



# ch_data
tbl_summary(
  ch_data[-1],
  by=pred_dicho,
  missing = 'no',
) %>%
  add_n() %>%
  add_p() %>%
  modify_header(label = "**Variable**") %>%
  bold_labels()


#----------------> boxplot

library(ggplot2)

#mut_cna
#mutSig
#ch_data

p <- ggplot(mutSig , aes(x=pred_dicho, y=mutSig21, fill=pred_dicho)) + 
   geom_boxplot(notch=T,outlier.colour="red", outlier.shape=8,outlier.size=4)+
   stat_summary(fun.y=mean, geom="point", shape=23, size=4)+
   geom_jitter(shape=16, position=position_jitter(0.2))+
   scale_color_brewer(palette="Dark2")+
   theme(legend.position="bottom") +
   ylim(0,0.10)
   
p

median()
wilcox.test(mutSig$mutSig21~mutSig$pred_dicho)

















