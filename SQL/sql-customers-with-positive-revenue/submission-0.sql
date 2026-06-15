-- Write your query below
SELECT DISTINCT c2019.customer_id
FROM customers c2019
JOIN customers c2020
    ON c2019.customer_id = c2020.customer_id
WHERE c2019.year = 2019
    AND c2020.year = 2020
ORDER BY c2019.customer_id;