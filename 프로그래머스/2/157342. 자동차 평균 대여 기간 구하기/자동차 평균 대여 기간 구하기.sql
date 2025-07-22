# WITH rental_duration AS (
#     SELECT car_id, DATEDIFF(end_date, start_date)+1 AS duration
#     FROM car_rental_company_rental_history
# )

# SELECT car_id, ROUND(AVG(duration), 1) AS average_duration
# FROM rental_duration
# GROUP BY car_id
# HAVING AVG(duration) >= 7
# ORDER BY average_duration DESC, car_id DESC;

SELECT car_id, ROUND(AVG(DATEDIFF(end_date, start_date)), 1)+1 AS average_duration
FROM car_rental_company_rental_history
GROUP BY car_id
HAVING average_duration >= 7
ORDER BY average_duration DESC, car_id DESC;

