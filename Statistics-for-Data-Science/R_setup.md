Download R & Studio from https://cran.r-project.org/ & https://posit.co/download/rstudio-desktop/ 

# 3 Popular R packages for statistical methods are:

1. dplyr, which provides a set of commands to more easily manipulate data and databases;

2. ggplot2, which provides a set of commands for data visualization; and

3. forecast, which provides a set of commands to generate forecasts using time-series methods.

```r
# Example R code
install.packages("dplyr")
library(dplyr)
data <- read.csv("data.csv")
summary(data)
```

# R variable types and Data types

*Numeric—values are numerical (e.g., 3, −1.5, 4,000),

Character—values are character strings (text) (e.g., “frost”, “rain”),

Logical—true or false values, and

Date—values represent calendar dates (e.g., 1978-12-16)*

Data of these variable types can then be stored in one of the following data objects:

*Vector—an ordered sequence of values of the same type (e.g., numeric, character, logical),

Factor—vector of values to be treated as nominal variables (unordered categories),

Ordered—vector of values to be treated as ordinal variables (ordered categories),

List—ordered collection of objects of possibly different types, and

Data frame—a two-dimensional array consisting of rows and columns; different columns can have different variable types.*

