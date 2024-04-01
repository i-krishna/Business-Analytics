# Week 3 Assignment - Krishna Damarla

## Step 1: Read in the Data

setwd("/Users/krishnadamarla/Library/CloudStorage/OneDrive-TrineUniversity/Trine/Terms/Spring Term 2 - Data Science & Big Data/W3/HMEQ_Scrubbed/")
data <- read.csv("HMEQ_Scrubbed.csv", header = TRUE) # Read the data into R
str(data) # structure of the data 
summary(data) # summary of the data
head(data) # first six records of the data

## Step 2: Classification Decision Tree

# Load required libraries
library(rpart)
library(rpart.plot)
library(pROC)
library(ggplot2)

# Ensure that the TARGET_LOSS_AMT variable is not used for prediction
data <- subset(data, select = -c(TARGET_LOSS_AMT))

# Build decision trees using Gini and Entropy criteria

# Using Gini
tree_gini <- rpart(TARGET_BAD_FLAG ~ ., data = data, method = "class", parms = list(split = "gini"))

# Using Entropy
tree_entropy <- rpart(TARGET_BAD_FLAG ~ ., data = data, method = "class", parms = list(split = "information"))

# Plot the decision trees

# Plotting Gini tree
rpart.plot(tree_gini)
# Plotting Entropy tree
rpart.plot(tree_entropy)


# List important variables for both trees

# Gini tree
important_vars_gini <- tree_gini$variable.importance
print("Important variables for Gini tree:")
print(important_vars_gini)

# Entropy tree
important_vars_entropy <- tree_entropy$variable.importance
print("Important variables for Entropy tree:")
print(important_vars_entropy)

# Create ROC curves for both trees

# Using Gini
roc_gini <- roc(predictor = predict(tree_gini, type = "prob")[,2], response = data$TARGET_BAD_FLAG)

# Using Entropy
roc_entropy <- roc(predictor = predict(tree_entropy, type = "prob")[,2], response = data$TARGET_BAD_FLAG)

# Plot ROC curves for both trees
plot(roc_gini, col = "blue", main = "ROC Curves for Gini and Entropy Decision Trees")
lines(roc_entropy, col = "red")
legend("bottomright", legend = c("Gini", "Entropy"), col = c("blue", "red"), lty = 1)

# Summarize classification decision trees
summary(tree_gini)
summary(tree_entropy)

## Step 3: Regression Decision Tree

# Load required libraries
library(rpart)
library(caret)

data <- read.csv("HMEQ_Scrubbed.csv", header = TRUE) # Read the data into R

# Ensure that the TARGET_BAD_FLAG variable is not used for prediction
data <- subset(data, select = -c(TARGET_BAD_FLAG))

# Set the maximum depth for the trees
max_depth <- 5

# Build regression decision trees with specified maximum depth
tree_anova <- rpart(TARGET_LOSS_AMT ~ ., data = data, method = "anova", control = rpart.control(maxdepth = max_depth))
tree_poisson <- rpart(TARGET_LOSS_AMT ~ ., data = data, method = "poisson", control = rpart.control(maxdepth = max_depth))
#tree_anova <- rpart(TARGET_LOSS_AMT ~ ., data = data, method = "anova")
#tree_poisson <- rpart(TARGET_LOSS_AMT ~ ., data = data, method = "poisson")

# Plot decision trees
rpart.plot(tree_anova)
rpart.plot(tree_poisson)

# List important variables
important_vars_anova <- tree_anova$variable.importance
print(important_vars_anova)
important_vars_poisson <- tree_poisson$variable.importance
print(important_vars_poisson)

# Calculate Root Mean Square Error (RMSE)
predicted_anova <- predict(tree_anova, data)
predicted_poisson <- predict(tree_poisson, data)
rmse_anova <- sqrt(mean((predicted_anova - data$TARGET_LOSS_AMT)^2))
print(rmse_anova)
rmse_poisson <- sqrt(mean((predicted_poisson - data$TARGET_LOSS_AMT)^2))
print(rmse_poisson)

# Summarize regression decision trees
summary(tree_anova)
summary(tree_poisson)

## Step 4: Probability / Severity Model Decision Tree

data <- read.csv("HMEQ_Scrubbed.csv", header = TRUE) # Read the data into R

data_wo_amt <- subset(data, select = -c(TARGET_LOSS_AMT))

# Predict TARGET_BAD_FLAG
tree_bad_flag <- rpart(TARGET_BAD_FLAG ~ ., data = data_wo_amt, method = "class")

# Filter data for defaulted records
defaulted_data <- subset(data, TARGET_BAD_FLAG == 1)

# Predict TARGET_LOSS_AMT for defaulted records
tree_loss_amt <- rpart(TARGET_LOSS_AMT ~ ., data = defaulted_data, method = "anova")

# Plot decision trees
rpart.plot(tree_bad_flag)
rpart.plot(tree_loss_amt)

# List important variables for both trees
important_vars_bad_flag <- tree_bad_flag$variable.importance
print(important_vars_bad_flag)
important_vars_loss_amt <- tree_loss_amt$variable.importance
print(important_vars_loss_amt)

# Predict probability of default
prob_default <- predict(tree_bad_flag, type = "prob")

# Predict loss given default
loss_given_default <- predict(tree_loss_amt)

# Multiply probability of default and loss given default
probability_severity <- prob_default * loss_given_default

# Calculate RMSE for Probability / Severity model
actual_loss <- defaulted_data$TARGET_LOSS_AMT
RMSE <- sqrt(mean((probability_severity - actual_loss)^2))

print(RMSE)


if(FALSE) {}
