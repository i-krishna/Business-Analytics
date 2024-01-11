# Example R code

install.packages("dplyr")
library(dplyr)
data <- read.csv("data.csv")
summary(data)
str(data)
View(data)
write.csv(data, "data.cav", row.names=FALSE)