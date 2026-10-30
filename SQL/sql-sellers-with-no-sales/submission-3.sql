-- Write your query below
SELECT seller_name
FROM seller
LEFT JOIN orders ON 
    seller.seller_id=orders.seller_id
    and
    sale_date between '2020-01-01' and '2020-12-31'
where order_id is null
ORDER BY seller_name;