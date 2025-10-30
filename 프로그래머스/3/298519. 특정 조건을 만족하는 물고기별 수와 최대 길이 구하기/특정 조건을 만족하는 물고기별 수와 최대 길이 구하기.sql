# 1. 데이터 전처리
WITH new_fish_info AS (
    SELECT id, fish_type, 
        CASE 
            # WHEN length <= 10 THEN 10
            WHEN length IS NULL THEN 10
            ELSE length
        END
        AS new_length
    FROM fish_info
)

# 2. 그룹 만들고 평균 구하기, 평균 33 이상인놈들 추출
SELECT COUNT(id) AS FISH_COUNT, MAX(new_length) AS MAX_LENGTH, FISH_TYPE
FROM new_fish_info
GROUP BY fish_type
HAVING AVG(new_length) >= 33
ORDER BY fish_type