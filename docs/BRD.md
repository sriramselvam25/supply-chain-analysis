# Business Requirements Document — Supply Chain & Inventory Intelligence

## Business Context
A multi-warehouse retailer faces stock-outs, excess inventory, inconsistent supplier performance, delayed replenishment and working capital tied up in slow-moving stock.

## Objective
Create an executive Power BI solution that helps operations and supply-chain leadership balance availability, supplier reliability and inventory efficiency.

## Stakeholders
COO, Head of Supply Chain, Inventory Manager, Procurement Manager, Warehouse Managers, Finance Controller, BI Analyst.

## Business Questions
1. Where are stock-outs and backorders concentrated?
2. Which warehouses carry excess or slow-moving inventory?
3. Which suppliers have weak OTIF and long lead times?
4. Are purchase quantities aligned to demand?
5. Which categories tie up the most working capital?
6. Where should reorder points or safety stock be reviewed?

## Functional Requirements
- Track inventory value, stockout rate, fill rate and supplier OTIF.
- Slice by date, category, warehouse, region and supplier.
- Highlight reorder risk, excess stock and slow-moving inventory.
- Compare supplier OTIF and lead time.
- Analyze demand, purchases and backorders over time.
- Enable product and warehouse drill-down.

## Non-Functional Requirements
Star schema, central DAX measures, synthetic public-safe data, desktop-responsive 16:9 design and explicit KPI definitions.

## Acceptance Criteria
Power BI KPIs reconcile to SQL; filters propagate correctly; stockout/slow/excess rules are reproducible; no real employer data is used.
