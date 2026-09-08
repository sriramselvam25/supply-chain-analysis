# Data Dictionary

## FactInventory
- `InventoryRecordID` — unique synthetic inventory observation
- `Date` — observation date
- `ProductID`, `WarehouseID`, `SupplierID` — dimension keys
- `StockOnHand` — available units
- `ReorderPoint` — replenishment trigger
- `SafetyStock` — buffer inventory
- `LeadTimeDays` — observed replenishment lead time
- `PurchaseQty` — purchase/replenishment quantity
- `DemandQty` — demand units
- `StockoutFlag` — critical shortage indicator
- `InventoryValueINR` — on-hand stock value
- `SupplierOTIF` — supplier on-time-in-full rate
- `FillRate` — fulfilled demand / demand
- `SlowMovingFlag` — days of inventory >75
- `ExcessStockFlag` — stock above defined excess threshold
- `ExcessStockValueINR` — value of units above the excess threshold
- `BackorderQty` — unfulfilled demand units
- `DaysOfInventory` — stock on hand / average daily demand

## Dimensions
`DimProduct`: product and category attributes.  
`DimWarehouse`: warehouse, region and state.  
`DimSupplier`: supplier, country and baseline service characteristics.  
`DimDate`: calendar hierarchy for 2024–2025.
