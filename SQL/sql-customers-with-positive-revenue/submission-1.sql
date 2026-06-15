-- Write your query below
SELECT customer_id
FROM customers
WHERE year = 2019
  AND customer_id IN (
      SELECT customer_id
      FROM customers
      WHERE year = 2020
  )
ORDER BY customer_id;