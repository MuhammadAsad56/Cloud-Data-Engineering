-- Q1. List top 5 customers by total order amount.
-- Retrieve the top 5 customers who have spent the most across all sales orders. Show CustomerID, CustomerName, and TotalSpent.

select top 5 c.CustomerID, c.Name ,
	sum(co.TotalAmount) total_amount
	from [dbo].[Customer] c
	join  [dbo].[SalesOrder] co
	on c.CustomerID = co.CustomerID
	group by c.CustomerID, c.Name
	order by total_amount desc


-- Q2. Find the number of products supplied by each supplier.
-- Display SupplierID, SupplierName, and ProductCount. Only include suppliers that have more than 10 products.


with cte as (
select s.Name as name,  s.SupplierID as supplierID, count(pod.ProductID) as prodId
	from [dbo].[Supplier] s
	join [dbo].[PurchaseOrder] po
	on s.SupplierID = po.SupplierID
	join [dbo].[PurchaseOrderDetail] pod
	on po.OrderID = pod.OrderID
	group by s.Name, s.SupplierID
	)
select cte.name, cte.supplierID , cte.prodId from cte
where cte.prodId  > 10


-- Q3. Identify products that have been ordered but never returned.
-- Show ProductID, ProductName, and total order quantity.

with cte as (
select p.ProductID as productId, p.Name as prodName
	from Product p
	left join ReturnDetail rd
	on p.ProductID = rd.ProductID
	where rd.ProductID is null
)

select o.productId, o.prodName, count (o.productId) as prod_saleCount
	from cte o
	join SalesOrderDetail sod
	on o.productId = sod.ProductID
	group by o.productId, o.prodName



-- Q4. For each category, find the most expensive product.
-- Display CategoryID, CategoryName, ProductName, and Price. Use a subquery to get the max price per category.


SELECT 
    c.CategoryID,
    c.Name AS CategoryName,
    p.Name AS ProductName,
    p.Price
FROM Product p
JOIN Category c
    ON p.CategoryID = c.CategoryID
WHERE p.Price = (
    SELECT MAX(p2.Price)
    FROM Product p2
    WHERE p2.CategoryID = p.CategoryID
);


-- Q5. List all sales orders with customer name, product name, category, and supplier.
-- For each sales order, display:
-- OrderID, CustomerName, ProductName, CategoryName, SupplierName, and Quantity.


select c.Name customerName, p.Name productName, ct.Name categoryName
	from SalesOrder so
	join Customer c
	on so.CustomerID = c.CustomerId
	join SalesOrderDetail sod 
	on so.OrderID = sod.OrderID
	join Product p
	on sod.ProductID = p.ProductID
	join Category ct
	on p.CategoryID = ct.CategoryID
	join PurchaseOrderDetail pod
	on p.ProductID = pod.ProductID
	join PurchaseOrder po
	on pod.OrderID = po.OrderID
	join Supplier sp
	on po.SupplierID = sp.SupplierID


-- Q6. Find all shipments with details of warehouse, manager, and products shipped. 
-- Display: ShipmentID, WarehouseName, ManagerName, ProductName, QuantityShipped, and TrackingNumber.


SELECT
    sh.ShipmentID,
    l.Name AS WarehouseName,
    e.Name AS ManagerName,
    p.Name AS ProductName,
    sd.Quantity AS QuantityShipped,
    sh.TrackingNumber
FROM shipment sh
JOIN warehouse w
    ON sh.WarehouseID = w.WarehouseID
JOIN location l
    ON w.LocationID = l.LocationID
JOIN employee e
    ON w.ManagerID = e.EmployeeID
JOIN shipmentdetail sd
    ON sh.ShipmentID = sd.ShipmentID
JOIN product p
    ON sd.ProductID = p.ProductID;



-- Q7. Find the top 3 highest-value orders per customer using RANK(). 
-- Display CustomerID, CustomerName, OrderID, and TotalAmount.

WITH RankedOrders AS (
    SELECT
        so.OrderID,
        so.CustomerID,
        c.Name AS CustomerName,
        so.TotalAmount,
        RANK() OVER (
            PARTITION BY so.CustomerID
            ORDER BY so.TotalAmount DESC
        ) AS order_rank
    FROM salesorder so
    JOIN customer c
        ON so.CustomerID = c.CustomerID
)

SELECT
    CustomerID,
    CustomerName,
    OrderID,
    TotalAmount
FROM RankedOrders
WHERE order_rank <= 3
ORDER BY CustomerID, TotalAmount DESC;



-- Q8. For each product, show its sales history with the previous and next sales quantities (based on order date). 
--Display ProductID, ProductName, OrderID, OrderDate, Quantity, PrevQuantity, and NextQuantity.


-- not solved

