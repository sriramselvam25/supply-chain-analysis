CREATE TABLE DimDate ([Date] date PRIMARY KEY,[Year] int,Quarter varchar(2),MonthNumber int,Month varchar(3),YearMonth char(7),Weekday varchar(10));
CREATE TABLE DimProduct (ProductID varchar(10) PRIMARY KEY,Product varchar(150),Category varchar(100),UnitCostINR decimal(18,2));
CREATE TABLE DimWarehouse (WarehouseID varchar(10) PRIMARY KEY,Warehouse varchar(100),Region varchar(50),State varchar(100),CapacityFactor decimal(10,4));
CREATE TABLE DimSupplier (SupplierID varchar(10) PRIMARY KEY,Supplier varchar(150),Country varchar(100),BaseLeadTimeDays int,BaseOTIF decimal(10,4));
CREATE TABLE FactInventory (
 InventoryRecordID varchar(30) PRIMARY KEY,[Date] date,ProductID varchar(10),WarehouseID varchar(10),SupplierID varchar(10),
 StockOnHand int,ReorderPoint int,SafetyStock int,LeadTimeDays int,PurchaseQty int,DemandQty int,StockoutFlag bit,
 InventoryValueINR decimal(18,2),SupplierOTIF decimal(10,4),FillRate decimal(10,4),SlowMovingFlag bit,ExcessStockFlag bit,
 ExcessStockValueINR decimal(18,2),BackorderQty int,DaysOfInventory decimal(18,2)
);
