-- 1. id당 milk 개수와 yogurt 개수 구한다
-- 2. milk와 yogurt가 모두 1개 이상인 놈들 찾는다

WITH milk_count AS (
    SELECT cart_id, COUNT(*) as cnt
    FROM cart_products
    WHERE name="Milk"
    GROUP BY cart_id
), yogurt_count AS (
    SELECT cart_id, COUNT(*) as cnt
    FROM cart_products
    WHERE name="Yogurt"
    GROUP BY cart_id
)

SELECT milk_count.cart_id
FROM milk_count 
    JOIN yogurt_count ON milk_count.cart_id=yogurt_count.cart_id
WHERE milk_count.cnt >= 1 AND yogurt_count.cnt >= 1