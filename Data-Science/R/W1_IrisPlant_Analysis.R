# Week 1 Assignment - Krishna Damarla

# Step 1: Describe the Data

str(iris) # structure of the data 
summary(iris) # summary of the data
head(iris) # first six records of the data

# Step 2: Box-Whisker Plot

boxplot(Sepal.Length ~ Species, data = iris, main = "Krishna's Box-Whisker Plot of Species and Sepal Length", notch = TRUE, col = "lightpink")

# Step 3: Histogram

hist(iris$Sepal.Length, breaks = 8, main = "Histogram of Sepal Length", xlab = "Sepal Length", ylab = "Frequency", col = "lightgrey")
lines(density(iris$Sepal.Length), col = "red") # Add density line on top of histogram
legend("topright", legend = c("Histogram", "Density"), fill = c("lightgrey", "red"), title = "Sepal Length") # Add legend

# Step 4: Scatter Plot

plot(iris$Sepal.Length, iris$Sepal.Width, col = iris$Species, pch = 16, main = "Scatter Plot of Sepal Length vs Sepal Width", xlab = "Sepal Length", ylab = "Sepal Width")
legend("topright", legend = levels(iris$Species), col = 1:length(unique(iris$Species)), pch = 16, title = "Species") # Add legend

# Step 5: Simple Math

Sepal_Length_Mean <- mean(iris$Sepal.Length)
Sepal_Length_Median <- median(iris$Sepal.Length)
Sepal_Length_Min <- min(iris$Sepal.Length)
Sepal_Length_Max <- max(iris$Sepal.Length)
Sepal_Length_SD <- sd(iris$Sepal.Length)
stats <- aggregate(Sepal.Length ~ Species, data = iris, FUN = median)
stats <- stats[order(stats$Sepal.Length, decreasing = TRUE), ] # Sort by median Sepal Length in descending order

# Print variables in a new line
cat( 
  "Statistics of Sepal Length",
  "\n",
  "Mean:", Sepal_Length_Mean,  "\n",
  "Median:", Sepal_Length_Median, "\n",
  "Min:", Sepal_Length_Min, "\n",
  "Max:", Sepal_Length_Max, "\n",
  "Standard Deviation:", Sepal_Length_SD, "\n"
)

cat("Median Sepal Length for each species in descending order")
print(stats)

#if(FALSE) {}
