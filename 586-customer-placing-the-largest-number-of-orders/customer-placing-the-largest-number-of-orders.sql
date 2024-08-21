# Write your MySQL query statement below
SELECT customer_number
FROM orders
GROUP BY customer_number
order by COUNT(order_number) desc
limit 1;


