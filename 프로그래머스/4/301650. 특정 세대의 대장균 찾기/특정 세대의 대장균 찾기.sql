-- 1. 트리 연결해서 3세대 친구들 구한다
-- 2. id에 대해 오름차순 정렬

WITH root AS (
    SELECT *
    FROM ecoli_data
    WHERE parent_id IS NULL
)

SELECT g3.id as id
FROM root AS g1
    LEFT JOIN ecoli_data AS g2
    ON g1.id=g2.parent_id
    
    LEFT JOIN ecoli_data AS g3
    ON g2.id=g3.parent_id
WHERE g3.id IS NOT NULL
ORDER BY g3.id;