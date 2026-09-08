# Data Model

Central fact: `FactInventory`.

Relationships (1:*):
- `DimDate[Date]` → `FactInventory[Date]`
- `DimProduct[ProductID]` → `FactInventory[ProductID]`
- `DimWarehouse[WarehouseID]` → `FactInventory[WarehouseID]`
- `DimSupplier[SupplierID]` → `FactInventory[SupplierID]`

Use single-direction filtering from dimensions to fact and mark `DimDate` as the model date table.

**Grain:** one synthetic inventory/replenishment observation for a product, warehouse, supplier and date.
