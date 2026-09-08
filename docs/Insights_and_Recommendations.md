# Illustrative Insights & Recommendations

All findings come from the synthetic portfolio scenario.

## Validated Findings
- Portfolio-wide stockout rate is **6.83%**; **Kolkata DC** has the highest stockout exposure.
- Average supplier OTIF is **82.89%**; **EastBridge Manufacturing** is the weakest supplier by OTIF.
- Average fill rate is **93.55%**; service loss is concentrated in stockout-risk observations.
- Average lead time is **16.56 days**, with selected import suppliers deliberately modeled as slower and less reliable.
- **Office** carries the highest excess inventory value, highlighting working capital tied up in overstock.
- Slow-moving stock uses a >75 days-of-inventory rule to surface potential obsolescence.
- Demand is intentionally stronger in Q4, creating realistic replenishment and service-level pressure.

## Recommendations
1. Reset reorder points and safety stock for warehouse/category combinations with repeated stockout risk.
2. Create supplier corrective-action plans for weak OTIF suppliers and diversify critical SKUs where lead-time variability is high.
3. Reduce new purchase orders for categories with high excess and slow-moving inventory until stock cover normalizes.
4. Use ABC/XYZ-style segmentation for differentiated service-level and inventory policies.
5. Pre-build Q4 inventory selectively for fast movers, not across all categories.
6. Add exception alerts for low fill rate, high backorders and stock below reorder point.
