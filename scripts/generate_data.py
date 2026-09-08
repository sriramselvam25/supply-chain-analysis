"""Generate the 36,000-row synthetic Supply Chain & Inventory Intelligence dataset."""
from pathlib import Path
from datetime import date, timedelta
import csv, random
import numpy as np

SEED=73
ROWS=36000
random.seed(SEED)
np.random.seed(SEED)
OUT=Path("generated")
OUT.mkdir(exist_ok=True)

categories=["Electronics","Home & Kitchen","Personal Care","Office","Grocery","Apparel"]
products=[]
for i in range(60):
    cat=categories[i%len(categories)]
    products.append([f"P{i+1:03d}",f"{cat} Product {i+1:02d}",cat,round(random.uniform(90,5500),2)])
warehouses=[
["W01","Chennai DC","South","Tamil Nadu",1.00],["W02","Bengaluru DC","South","Karnataka",1.05],
["W03","Mumbai DC","West","Maharashtra",1.10],["W04","Delhi NCR DC","North","Delhi NCR",1.12],
["W05","Kolkata DC","East","West Bengal",0.92],["W06","Hyderabad DC","South","Telangana",0.98],
["W07","Pune DC","West","Maharashtra",1.02],["W08","Ahmedabad DC","West","Gujarat",0.95]]
suppliers=[
["S01","Apex Components","India",8,.94],["S02","Nova Supply Co","India",10,.91],["S03","Pacific Source","Singapore",16,.88],
["S04","GlobalLink Trading","China",22,.82],["S05","Vertex Industries","India",12,.93],["S06","Prime Distribution","UAE",18,.86],
["S07","Reliable Goods","India",9,.96],["S08","EastBridge Manufacturing","Vietnam",24,.80],["S09","Metro Wholesale","India",11,.92],
["S10","NorthStar Imports","Thailand",20,.84]]

month_demand={1:.94,2:.92,3:.98,4:1.00,5:1.03,6:1.05,7:1.02,8:1.04,9:1.08,10:1.18,11:1.28,12:1.34}
supplier_delay={"S04":1.32,"S08":1.38,"S10":1.22}
cat_excess={"Office":1.28,"Apparel":1.18}
warehouse_risk={"W05":1.18,"W08":1.15}

dates=[]; d=date(2024,1,1)
while d<=date(2025,12,31):
    dates.append(d); d+=timedelta(days=1)
weights=np.array([month_demand[d.month] for d in dates],float); weights/=weights.sum()

# dimensions
for filename,headers,rows in [
("DimProduct.csv",["ProductID","Product","Category","UnitCostINR"],products),
("DimWarehouse.csv",["WarehouseID","Warehouse","Region","State","CapacityFactor"],warehouses),
("DimSupplier.csv",["SupplierID","Supplier","Country","BaseLeadTimeDays","BaseOTIF"],suppliers)]:
    with open(OUT/filename,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
with open(OUT/"DimDate.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["Date","Year","Quarter","MonthNumber","Month","YearMonth","Weekday"])
    for dt in dates: w.writerow([dt,dt.year,f"Q{(dt.month-1)//3+1}",dt.month,dt.strftime("%b"),dt.strftime("%Y-%m"),dt.strftime("%A")])

with open(OUT/"FactInventory.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["InventoryRecordID","Date","ProductID","WarehouseID","SupplierID","StockOnHand","ReorderPoint","SafetyStock","LeadTimeDays","PurchaseQty","DemandQty","StockoutFlag","InventoryValueINR","SupplierOTIF","FillRate","SlowMovingFlag","ExcessStockFlag","ExcessStockValueINR","BackorderQty","DaysOfInventory"])
    for i in range(ROWS):
        dt=dates[int(np.random.choice(len(dates),p=weights))]
        p=random.choice(products); wh=random.choice(warehouses); sup=random.choice(suppliers)
        demand=max(2,int(np.random.gamma(3.2,14)*month_demand[dt.month]*wh[4]*random.uniform(.82,1.18)))
        safety=max(5,int(demand*random.uniform(.35,.65)))
        reorder=safety+max(5,int(demand*random.uniform(.65,1.15)))
        delay=supplier_delay.get(sup[0],1.0)
        lead=max(3,int(np.random.normal(sup[3]*delay,2.4)))
        otif=max(.55,min(.995,np.random.normal(sup[4]/delay,.045)))
        stock_factor=random.uniform(.60,1.60)
        if p[2] in cat_excess: stock_factor*=cat_excess[p[2]]
        if wh[0] in warehouse_risk: stock_factor/=warehouse_risk[wh[0]]
        stock=max(0,int(reorder*stock_factor-demand*random.uniform(.30,.90)))
        stockout=int(stock<max(1,int(demand*.25)))
        backorder=max(0,demand-stock) if stockout else max(0,int((demand-stock)*.05))
        fill=max(0,min(1,(demand-backorder)/demand))
        purchase=max(0,int((reorder+safety-stock)*random.uniform(.65,1.25)))
        doi=stock/max(demand/30,.1)
        slow=int(doi>75)
        excess_qty=max(0,stock-int(reorder+safety*1.25)); excess=int(excess_qty>0)
        w.writerow([f"INV-{i+1:06d}",dt,p[0],wh[0],sup[0],stock,reorder,safety,lead,purchase,demand,stockout,round(stock*p[3],2),round(otif,4),round(fill,4),slow,excess,round(excess_qty*p[3],2),backorder,round(doi,2)])
print(f"Generated {ROWS:,} synthetic rows in {OUT.resolve()}")
