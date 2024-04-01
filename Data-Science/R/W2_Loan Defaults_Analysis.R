# Week 2 Assignment - Krishna Damarla

## Step 1: Read in the Data

setwd("/Users/krishnadamarla/Library/CloudStorage/OneDrive-TrineUniversity/Trine/Terms/Spring Term 2 - Data Science & Big Data/W2/HMEQ_WK02/")
data <- read.csv("HMEQ_Loss.csv", header = TRUE) # Read the data into R
str(data) # structure of the data 
summary(data) # summary of the data
head(data) # first six records of the data

#if(FALSE) {

## Step 2: Box-Whisker Plot
  
# Load necessary libraries
library(readr)
library(ggplot2)

# Plot box plots for numeric variables split by the grouping variable
numeric_vars <- sapply(data, is.numeric)
numeric_vars <- names(numeric_vars[numeric_vars])

for (var in numeric_vars) {
  # Create the plot
  p <- ggplot(data, aes(x = as.factor(TARGET_BAD_FLAG), y = .data[[var]], fill = as.factor(TARGET_BAD_FLAG))) +
    geom_boxplot() +
    labs(title = "Krishna's Box-Whisker Plot", x = "TARGET_BAD_FLAG", y = var) +
    theme_minimal() +
    scale_fill_manual(values = c("blue", "red")) +
    theme(legend.position = "none")
  
  # Print the plot based on user input
  cat("Press Enter to view box plot for variable", var, ": ")
  input <- readline()
  print(p)
}


## Step 3: Histogram

# Plotting histogram with density line for Loan variable
ggplot(data, aes(x = LOAN)) +
  geom_histogram(binwidth = 1000, color = "skyblue", color = "black", bins = 30) +
  geom_density(aes(y = ..count.. * 1000), alpha = 0.2, fill = "orange") +
  labs(title = "Histogram of LOAN",
       x = "LOAN",
       y = "Frequency") +
  theme_minimal()

## Step 4 (Method-1): Impute Missing Values with Median

# Load the required libraries
library(dplyr) # for data manipulation

# For numeric variables, Impute missing values with median
# Define a function for imputation and flagging missing values
impute_and_flag <- function(data, var_name) {
  median_val <- median(data[[var_name]], na.rm = TRUE)  # Calculate median for imputation
  
  # Impute and flag missing values
  data <- data %>%
    mutate(
      !!paste0("IMP_", var_name) := ifelse(is.na(.data[[var_name]]), median_val, .data[[var_name]]),
      !!paste0("M_", var_name) := ifelse(is.na(.data[[var_name]]), 1, 0)
    ) %>%
    select(-var_name)  # Delete original variable after imputation
  
  return(data)
}

# List of numeric variables with missing values (excluding TARGET_BAD_FLAG & TARGET_LOSS_AMT)
numeric_vars <- names(data)[sapply(data, is.numeric) & colSums(is.na(data)) > 0 & names(data) != "TARGET_BAD_FLAG" & names(data) != "TARGET_LOSS_AMT"]

# Impute and flag missing values for numeric variables
for (var in numeric_vars) {
  data <- impute_and_flag(data, var)
}

# For the Target variables, set the missing values to zero
data$TARGET_BAD_FLAG[is.na(data$TARGET_BAD_FLAG)] <- 0
data$TARGET_LOSS_AMT[is.na(data$TARGET_LOSS_AMT)] <- 0
#data$TARGET_LOSS_AMT[data$TARGET_LOSS_AMT == ""] <- 0
#data$TARGET_BAD_FLAG[data$TARGET_BAD_FLAG == ""] <- 0

# Summary to prove that all the variables have been imputed
summary(data)

# Compute a sum for all the M_ variables to prove that the number of flags is equal to the number of missing values
m_flags_sum <- colSums(data[, grepl("^M_", names(data))])
m_flags_sum

# Write the final result to a CSV file
write.csv(data, "Cleaned_numerical_result.csv", row.names = FALSE)

## Step 4 (Method-2: Complex imputation): Impute Missing Values with Random forest

# Load the required libraries
library(missForest)

# Load the dataset
data <- read.csv("HMEQ_Loss.csv")

# Set missing values of target variables to zero
data$TARGET_BAD_FLAG[is.na(data$TARGET_BAD_FLAG)] <- 0
data$TARGET_LOSS_AMT[is.na(data$TARGET_LOSS_AMT)] <- 0

# Impute missing values for remaining numeric variables using random forest imputation
# Select numeric variables with missing values
numeric_vars <- names(data)[sapply(data, is.numeric) & colSums(is.na(data)) > 0 & names(data) != "TARGET_BAD_FLAG" & names(data) != "TARGET_LOSS_AMT"]

# Perform random forest imputation
imputed_data <- missForest(data[numeric_vars], verbose = TRUE)

# Extract the imputed data
imputed_numeric <- imputed_data$ximp

# Create flags for imputed values
for (var in numeric_vars) {
  imp_var <- paste0("IMP_", var)
  m_var <- paste0("M_", var)
  data[[imp_var]] <- imputed_numeric[[var]]
  data[[m_var]] <- ifelse(is.na(data[[var]]), 1, 0)
  data[[var]][is.na(data[[var]])] <- imputed_numeric[[var]]
}

# Remove original numeric variables
data <- data[ , !names(data) %in% numeric_vars]

# Run a summary to prove that all variables have been imputed
summary(data)

# Compute a sum for all the M_ variables to prove the number of flags equals the number of missing values
m_flags_sum <- colSums(data[, grepl("^M_", names(data))])
m_flags_sum

#}

## Step 5: One Hot Encoding

# Load necessary libraries
library(dplyr)

# Read the data
data <- read.csv("HMEQ_Loss.csv", header = TRUE)

# Identify character/category variables
char_vars <- names(data)[sapply(data, is.character)]

# Perform one-hot encoding
for (var in char_vars) {
  encoded_vars <- model.matrix(~ data[[var]] - 1)  # Perform one-hot encoding
  colnames(encoded_vars) <- paste(var, colnames(encoded_vars), sep = "_")  # Rename columns
  data <- cbind(data, encoded_vars)  # Add encoded variables to the dataset
}

# Delete original character/category variables
data <- data %>%
  select(-one_of(char_vars))

# Run a summary
summary(data)

# Write the final result to a CSV file
write.csv(data, "Cleaned_categorical_result.csv", row.names = FALSE)
