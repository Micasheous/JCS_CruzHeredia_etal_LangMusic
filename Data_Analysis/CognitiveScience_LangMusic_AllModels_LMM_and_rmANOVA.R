##################################################
##################################################
### Analysis script for manuscript entitled:
### "Bidirectional interaction between language and music in a dual task experiment without syntactic violations"
##################################################
##################################################

#############################################
rm(list=ls()) #clear memory of any variables
cat("\f")# clear the console

################################################################
## Example of how to install packages: install.packages("lme4")

################
## Load packages

library(lme4)
library(nlme)
library(emmeans)
library(car)
library("rio")
library(afex)
library(rstatix)
library(ggpubr)

#########################
## Set working directory

# setwd("C:/path/to/folder")

setwd("C:/Users/Micaceous/Desktop/Research/LangMusic/Manuscript/CognitiveScience_resubmission_04-30-24/Publication_filesharing/Data_Analysis")

####################################
######## Multicore setup ###########
## optional for binomial models (DV=LangACC) to increase speed (if not used in binomial models, remove the following arguments from each model function call: cl=cl,control=glmerControl(optCtrl=list(maxfun=100000))

require(parallel)
##(nc <- detectCores()) ## find total number of cores
nc <- 6
cl <- makeCluster(rep("localhost",nc)) ## make cluster
cl <- makeCluster(rep("localhost", nc), outfile = "cl.log.txt") # to keep track of what the function is doindg redirect output to outfile:





##################################################################################
##  Model 1: Task Type (Language, Dual) X Sentence Structure (SE, SRC1, SRC2, ORC)
##################################################################################

### Importing data ####
data2<-import("R_data2_LangACC_DualandLang_new.csv")

#################
### LME model ###

### Run binomial model (testing full model)
model1.TTxSS <- mixed(Lang_ACC ~ 1+TaskType*SentStruct + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=glmerControl(optCtrl=list(maxfun=100000)), family=binomial, expand_re=TRUE)

### Output summaries
summary(model1.TTxSS)
anova(model1.TTxSS)

### Run nonbinomial model (in order to obtain condition means and pairwise tests)
model1.TTxSSnb <- mixed(Lang_ACC ~ 1+TaskType*SentStruct + (1|subj),data=data2,progress=TRUE,method="S",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)),expand_re=TRUE)

### Output summaries
summary(model1.TTxSSnb)
anova(model1.TTxSSnb)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(model1.TTxSSnb, pairwise ~ TaskType*SentStruct)

#### Complex Contrasts (testing differences between simple main effects)
emms2 <- emmeans(model1.TTxSSnb, pairwise ~ TaskType | SentStruct)
pairs(emms2[[2]], by=NULL)


#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_LangACC_DualandLang_new.csv")

## Run model
model1.aov <- aov_ez("subj", "Lang_ACC", within = c("TaskType", "SentStruct"), fun_aggregate = mean, data2)

## Print model results
model1.aov

## Pairwise comparisons ##
model1.emm <- emmeans(model1.aov, pairwise ~ TaskType|SentStruct)
pairs(model1.emm, by=NULL)

## Complex contrasts ##
model1.emm <- emmeans(model1.aov, pairwise ~ TaskType|SentStruct)
pairs(model1.emm[[2]], by=NULL)




##################################################################################
##  Model 2a: Task Type (Language, Dual) X Music Structure (Return, Stay)
##################################################################################

### Importing data ####
data2<-import("R_data2_MusicResp_DualandMusic_new.csv")

#################
### LME model ###

### Run model
final.TTxRS <- mixed(Music_resp ~ 1+TaskType*ReturnStay + PivotPlace + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)),REML=FALSE, expand_re=TRUE)

### Output summaries
summary(final.TTxRS)
anova(final.TTxRS)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(final.TTxRS, pairwise ~ TaskType*ReturnStay)




#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_MusicResp_DualandMusic_new.csv")

## Run model
model2a.aov <- aov_ez("subj", "Music_resp", within = c("TaskType", "ReturnStay"), fun_aggregate = mean, data2)

## Print model results
model2a.aov

## Pairwise comparisons ##
model2a.emm <- emmeans(model2a.aov, pairwise ~ TaskType|ReturnStay)
pairs(model2a.emm, by=NULL)




##################################################################################
##  Model 2b: Task Type (Language, Dual) X Music SynWM (Pivot-Return Distance)
##################################################################################

### Importing data ####
data2<-import("R_data2_MusicResp_DualandMusic_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Demean the covariate used in interaction ##
data2$PivRetDist <- scale(data2$PivRetDist, center = TRUE, scale = FALSE)

#################
### LME model ###

### Run model
final.TTxPivRetDist <- mixed(Music_resp ~ 1+TaskType*PivRetDist + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)),REML=FALSE, expand_re=TRUE)

### Output summaries
summary(final.TTxPivRetDist)
anova(final.TTxPivRetDist)

### Pairwise tests (for slopes for each condition)
model2b.emt <- emtrends(final.TTxPivRetDist, ~ TaskType, var="PivRetDist")
model2b.emt

## Compare slopes ##
pairs(model2b.emt, by=NULL)



######################################################
### Alternative rmANOVA using lm #####################
## In order to get simple main effects of slopes (since emtrends did not work with the aov model object)

### Importing data ####
data2<-import("R_data2_MusicResp_DualandMusic_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Demean the covariate used in interaction ##
data2$PivRetDist <- scale(data2$PivRetDist, center = TRUE, scale = FALSE)

## Run model
model2b.lm <- lm(Music_resp ~ TaskType*PivRetDist, data2)

### Output summaries
summary(model2b.lm)
anova(model2b.lm)

### Pairwise tests (for slopes for each condition)
emtrends(model2b.lm, ~ TaskType, var="PivRetDist")

### Pairwise tests (for slopes for each condition)
model2b.lm.emt <- emtrends(model2b.lm, ~ TaskType, var="PivRetDist")
model2b.lm.emt

## Compare slopes ##
pairs(model2b.lm.emt, by=NULL)

#####################
### rmANOVA model ###
## Ignore: could not get simple main effects of slopes using emtrends on the aov object

### Importing data ####
#data2<-import("R_data2_MusicResp_DualandMusic_new.csv")
#exclRS<-data.frame(ReturnStay=c("stay"))
#data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Run model
#model2b.aov <- aov_ez("subj", "Music_resp", within = c("TaskType", "PivRetDist"), fun_aggregate = mean, data2)

## Print model results
#model2b.aov








##################################################################################
##  Model 3a: Sentence Structure (SE, SRC1, SRC2, ORC) X Music Structure (Return, Stay)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

#################
### LME model ###

### Run model
final.SSxRS <- mixed(Lang_ACC ~ 1+SentStruct*ReturnStay + PivotPlace + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=glmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE, family=binomial, nAGQ=0)

### Output summaries
summary(final.SSxRS)
anova(final.SSxRS)

### Run nonbinomial model (in order to obtain condition means andd pairwise tests)
final.SSxRSnb <- mixed(Lang_ACC ~ 1+SentStruct*ReturnStay + PivotPlace + (1|subj),data=data2,progress=TRUE,method="S",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE)

### Output summaries
summary(final.SSxRSnb)
anova(final.SSxRSnb)

### Pairwise tests (for condition means and pairwise tests)

## collapsing over RS (since interaction and main effect was not significant)
emm_options(pbkrtest.limit=10000)
emmeans(final.SSxRSnb, pairwise ~ SentStruct)


#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

## Run model
model3a.aov <- aov_ez("subj", "Lang_ACC", within = c("SentStruct", "ReturnStay"), fun_aggregate = mean, data2)

## Print model results
model3a.aov

## Pairwise comparisons  (for condition means and pairwise tests) ##

## collapsing over RS (since main effect was not significant)
emmeans(model3a.aov, pairwise ~ SentStruct)








##################################################################################
##  Model 3b: Sentence Structure (SE, SRC1, SRC2, ORC) X Music Structure (Return, Stay)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

#################
### LME model ###

### Run model
final.SSxRS <- mixed(Music_resp ~ 1+SentStruct*ReturnStay + PivotPlace + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE, REML=FALSE)

### Output summaries
summary(final.SSxRS)
anova(final.SSxRS)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(final.SSxRS, pairwise ~ SentStruct*ReturnStay)

#### Complex Contrasts (testing differences between simple main effects)
emms3b <- emmeans(final.SSxRS, pairwise ~ ReturnStay | SentStruct)
pairs(emms3b[[2]], by=NULL)





#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

## Run model
model3b.aov <- aov_ez("subj", "Music_resp", within = c("SentStruct", "ReturnStay"), fun_aggregate = mean, data2)

## Print model results
model3b.aov

## Pairwise comparisons ##
model3b.emm <- emmeans(model3b.aov, pairwise ~ SentStruct|ReturnStay)
pairs(model3b.emm, by=NULL)

## Complex contrasts ##
model3b.emm <- emmeans(model3b.aov, revpairwise ~ ReturnStay|SentStruct)
pairs(model3b.emm[[2]], by=NULL)



##################################################################################
##  Model 4a: Sentence Structure (SE, SRC1, SRC2, ORC) X Music SynWM (Pivot-Return Distance)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Demean the covariate used in interaction ##
data2$PivRetDist <- scale(data2$PivRetDist, center = TRUE, scale = FALSE)

#################
### LME model ###

### Run model
final.SSxPivRetDist <- mixed(Lang_ACC ~ 1+SentStruct*PivRetDist + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), family=binomial, expand_re=TRUE, nAGQ=0)

### Output summaries
summary(final.SSxPivRetDist)
anova(final.SSxPivRetDist)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emtrends(final.SSxPivRetDist, ~ SentStruct, var="PivRetDist")

#### Complex Contrasts (testing differences between simple main effects)
emms2 <- emtrends(final.SSxPivRetDist, "SentStruct", var="PivRetDist")
  ## or do revpairwise to reverse the subtraction terms
pairs(emms2, by=NULL)



######################################################
### Alternative rmANOVA using lm #####################
## In order to get simple main effects of slopes (since emtrends did not work with the aov model object)

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Run model
model4a.lm <- lm(Lang_ACC ~ SentStruct*PivRetDist, data2)

### Output summaries
summary(model4a.lm)
anova(model4a.lm)

### Pairwise tests (for slopes for each condition)
emtrends(model4a.lm, ~ SentStruct, var="PivRetDist")

#### Complex Contrasts (testing differences between simple main effects)
emms2 <- emtrends(model4a.lm, "SentStruct", var="PivRetDist")
## or do revpairwise to reverse the subtraction terms
pairs(emms2, by=NULL)






##################################################################################
##  Model 4b: Sentence Structure (SE, SRC1, SRC2, ORC) X Music SynWM (Pivot-Return Distance)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

#################
### LME model ###

### Run model
final.SSxPivRetDist <- mixed(Music_resp ~ 1+SentStruct*PivRetDist + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), REML=FALSE, expand_re=TRUE)

### Output summaries
summary(final.SSxPivRetDist)
anova(final.SSxPivRetDist)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emtrends(final.SSxPivRetDist, ~ SentStruct, var="PivRetDist")

#### Complex Contrasts (testing differences between simple main effects)
emms2 <- emtrends(final.SSxPivRetDist, "SentStruct", var="PivRetDist")
## or do revpairwise to reverse the subtraction terms
pairs(emms2, by=NULL)




######################################################
### Alternative rmANOVA using lm #####################
## In order to get simple main effects of slopes (since emtrends did not work with the aov model object)

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Run model
model4b.lm <- lm(Music_resp ~ SentStruct*PivRetDist, data2)

### Output summaries
summary(model4b.lm)
anova(model4b.lm)

### Pairwise tests (for slopes for each condition)
emtrends(model4b.lm, ~ SentStruct, var="PivRetDist")

#### Complex Contrasts (testing differences between simple main effects)
emms2 <- emtrends(model4b.lm, "SentStruct", var="PivRetDist")
## or do revpairwise to reverse the subtraction terms
pairs(emms2, by=NULL)





##################################################################################
##  Model 5a: Sentence Structure (SE, SRC2, ORC) X Pivot Place (P2, P3, P4)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

#################
### LME model ###

### Run model
final.SSxPivPlace <- mixed(Lang_ACC ~ 1+SentStruct*PivotPlace + ReturnStay + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=glmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE, family=binomial, nAGQ=0)

### Output summaries
summary(final.SSxPivPlace)
anova(final.SSxPivPlace)

### Run nonbinomial model (in order to obtain condition means andd pairwise tests)
final.SSxPivPlacenb <- mixed(Lang_ACC ~ 1+SentStruct*PivotPlace + ReturnStay + (1|subj),data=data2,progress=TRUE,method="S",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), REML=FALSE, expand_re=TRUE)

### Output summaries
summary(final.SSxPivPlacenb)
anova(final.SSxPivPlacenb)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(final.SSxPivPlacenb, pairwise ~ SentStruct*PivotPlace)



#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

## Run model
model5a.aov <- aov_ez("subj", "Lang_ACC", within = c("SentStruct", "PivotPlace"), fun_aggregate = mean, data2)

## Print model results
model5a.aov

## Pairwise comparisons and complex contrasts ##
model5a.emm <- emmeans(model5a.aov, pairwise ~ SentStruct*PivotPlace)
pairs(model5a.emm, by=NULL)





##################################################################################
##  Model 5b: Sentence Structure (SE, SRC2, ORC) X Pivot Place (P2, P3, P4)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

#################
### LME model ###

### Run model
final.SSxPivPlace <- mixed(Music_resp ~ 1+SentStruct*PivotPlace + ReturnStay + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE)

### Output summaries
summary(final.SSxPivPlace)
anova(final.SSxPivPlace)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(final.SSxPivPlace, pairwise ~ SentStruct*PivotPlace)



#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")

## Run model
model5b.aov <- aov_ez("subj", "Music_resp", within = c("SentStruct", "PivotPlace"), fun_aggregate = mean, data2)

## Print model results
model5b.aov

## Pairwise comparisons and complex contrasts ##
model5b.emm <- emmeans(model5b.aov, pairwise ~ SentStruct*PivotPlace)
pairs(model5b.emm, by=NULL)





##################################################################################
##  Model 6a: Sentence Structure (SRC1, SRC2, ORC) X Return Place (R6, R7, R8)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

#################
### LME model ###

### Run model
final.SSxRetPlace <- mixed(Lang_ACC ~ 1+SentStruct*ReturnPlace + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=glmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE, family=binomial, nAGQ=0)

### Output summaries
summary(final.SSxRetPlace)
anova(final.SSxRetPlace)

### Run nonbinomial model (in order to obtain condition means andd pairwise tests)
final.SSxRetPlacenb <- mixed(Lang_ACC ~ 1+SentStruct*ReturnPlace + (1|subj),data=data2,progress=TRUE,method="S",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), expand_re=TRUE)

### Output summaries
summary(final.SSxRetPlacenb)
anova(final.SSxRetPlacenb)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(final.SSxRetPlacenb, pairwise ~ SentStruct*ReturnPlace)





#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Run model
model6a.aov <- aov_ez("subj", "Lang_ACC", within = c("SentStruct", "ReturnPlace"), fun_aggregate = mean, data2)

## Print model results
model6a.aov

## Pairwise comparisons and complex contrasts ##
model6a.emm <- emmeans(model6a.aov, pairwise ~ SentStruct*ReturnPlace)
pairs(model6a.emm, by=NULL)




##################################################################################
##  Model 6b: Sentence Structure (SRC1, SRC2, ORC) X Return Place (R6, R7, R8)
##################################################################################

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

#################
### LME model ###

### Run model
final.SSxRetPlace <- mixed(Music_resp ~ 1+SentStruct*ReturnPlace + (1|subj),data=data2,progress=TRUE,method="LRT",cl=cl,control=lmerControl(optCtrl=list(maxfun=100000)), REML=FALSE, expand_re=TRUE)

### Output summaries
summary(final.SSxRetPlace)
anova(final.SSxRetPlace)

### Pairwise tests (for condition means and pairwise tests)
emm_options(pbkrtest.limit=10000)
emmeans(final.SSxRetPlace, pairwise ~ SentStruct*ReturnPlace)


#####################
### rmANOVA model ###

### Importing data ####
data2<-import("R_data2_bothDVs_Dual_new.csv")
exclRS<-data.frame(ReturnStay=c("stay"))
data2<-data2[!(data2$ReturnStay %in% exclRS$ReturnStay),]

## Run model
model6b.aov <- aov_ez("subj", "Music_resp", within = c("SentStruct", "ReturnPlace"), fun_aggregate = mean, data2)

## Print model results
model6b.aov

## Pairwise comparisons and complex contrasts ##
model6b.emm <- emmeans(model6b.aov, pairwise ~ SentStruct*ReturnPlace)
pairs(model6b.emm, by=NULL)





















