# 90-Second Interview Walkthrough

> “I built a Supply Chain & Inventory Intelligence portfolio solution using a fully synthetic 36,000-row inventory and replenishment dataset. The business problem was to reduce stock-outs, excess inventory, supplier delays and working capital tied up in stock.
>
> I modeled the solution as FactInventory with Date, Product, Warehouse and Supplier dimensions. SQL queries reconcile service-level, stockout, supplier and inventory-value KPIs. Power Query standardizes the data and derives stock-health classifications, while DAX centralizes measures such as Inventory Value, Stockout Rate, Supplier OTIF, Fill Rate, Excess Stock Value, Average Lead Time and Days of Inventory.
>
> The synthetic data deliberately contains Q4 demand pressure, selected unreliable suppliers, warehouse risk pockets and categories with excess stock. The validated scenario produces a 6.83% stockout rate, 82.89% supplier OTIF and 93.55% fill rate, which gives me realistic business trade-offs to explain around replenishment, supplier management and working capital.”

## Interview Follow-ups
- How would you choose safety stock and reorder points?
- How do OTIF and fill rate differ?
- How would you identify slow-moving and excess stock?
- How would you scale the model to daily SKU-location inventory snapshots?
- Which alerts would you operationalize first?
