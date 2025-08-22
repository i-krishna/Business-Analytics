-- OLTP Tables (Normalized)
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Address VARCHAR(200)
);

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

CREATE TABLE [Order] (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    Status VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE OrderItem (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES [Order](OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- OLAP Tables (Star Schema)
CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    Date DATE,
    Month INT,
    Quarter INT,
    Year INT
);

CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Region VARCHAR(50)
);

CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    Category VARCHAR(50)
);

CREATE TABLE DimRegion (
    RegionID INT PRIMARY KEY,
    RegionName VARCHAR(50)
);

CREATE TABLE FactSales (
    SalesID INT PRIMARY KEY,
    DateID INT,
    CustomerID INT,
    ProductID INT,
    RegionID INT,
    SalesAmount DECIMAL(12,2),
    Quantity INT,
    FOREIGN KEY (DateID) REFERENCES DimDate(DateID),
    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID),
    FOREIGN KEY (RegionID) REFERENCES DimRegion(RegionID)
);
