-- Executive inventory KPIs
SELECT SUM(InventoryValueINR) InventoryValue,
       AVG(CAST(StockoutFlag AS decimal(10,4))) StockoutRate,
       AVG(SupplierOTIF) SupplierOTIF,
       AVG(FillRate) FillRate,
       SUM(ExcessStockValueINR) ExcessStockValue,
       AVG(CAST(LeadTimeDays AS decimal(18,2))) AvgLeadTimeDays
FROM FactInventory;

-- Warehouse stockout exposure
SELECT w.Warehouse,
       AVG(CAST(f.StockoutFlag AS decimal(10,4))) StockoutRate,
       SUM(f.InventoryValueINR) InventoryValue,
       SUM(f.BackorderQty) BackorderQty
FROM FactInventory f JOIN DimWarehouse w ON f.WarehouseID=w.WarehouseID
GROUP BY w.Warehouse ORDER BY StockoutRate DESC;

-- Supplier performance
SELECT s.Supplier,
       AVG(f.SupplierOTIF) OTIF,
       AVG(CAST(f.LeadTimeDays AS decimal(18,2))) AvgLeadTimeDays,
       AVG(f.FillRate) FillRate
FROM FactInventory f JOIN DimSupplier s ON f.SupplierID=s.SupplierID
GROUP BY s.Supplier ORDER BY OTIF ASC;

-- Excess / slow-moving inventory
SELECT p.Category,
       SUM(f.ExcessStockValueINR) ExcessStockValue,
       AVG(CAST(f.SlowMovingFlag AS decimal(10,4))) SlowMovingRate,
       SUM(f.InventoryValueINR) InventoryValue
FROM FactInventory f JOIN DimProduct p ON f.ProductID=p.ProductID
GROUP BY p.Category ORDER BY ExcessStockValue DESC;

-- Monthly demand and purchase trend
SELECT FORMAT([Date],'yyyy-MM') YearMonth,
       SUM(DemandQty) DemandQty,SUM(PurchaseQty) PurchaseQty,
       SUM(BackorderQty) BackorderQty
FROM FactInventory GROUP BY FORMAT([Date],'yyyy-MM') ORDER BY YearMonth;
