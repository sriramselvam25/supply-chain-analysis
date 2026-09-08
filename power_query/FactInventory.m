let
    Source = Csv.Document(File.Contents(ParameterFactInventoryPath),[Delimiter=",",Encoding=65001,QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Headers,{
        {"InventoryRecordID",type text},{"Date",type date},{"ProductID",type text},{"WarehouseID",type text},{"SupplierID",type text},
        {"StockOnHand",Int64.Type},{"ReorderPoint",Int64.Type},{"SafetyStock",Int64.Type},{"LeadTimeDays",Int64.Type},
        {"PurchaseQty",Int64.Type},{"DemandQty",Int64.Type},{"StockoutFlag",Int64.Type},{"InventoryValueINR",Currency.Type},
        {"SupplierOTIF",Percentage.Type},{"FillRate",Percentage.Type},{"SlowMovingFlag",Int64.Type},{"ExcessStockFlag",Int64.Type},
        {"ExcessStockValueINR",Currency.Type},{"BackorderQty",Int64.Type},{"DaysOfInventory",type number}
    }),
    StockHealth = Table.AddColumn(Typed,"StockHealth", each if [StockoutFlag]=1 then "Stockout Risk" else if [ExcessStockFlag]=1 then "Excess" else if [SlowMovingFlag]=1 then "Slow Moving" else "Healthy", type text)
in
    StockHealth
