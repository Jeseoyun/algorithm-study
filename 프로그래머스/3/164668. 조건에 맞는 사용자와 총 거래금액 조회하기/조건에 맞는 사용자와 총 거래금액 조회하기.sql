-- 1. 완료된 중고 거래의 총 금액이 70만원 이상인 사람 찾기
-- 2. 그 사람의 정보와 함께 출력

WITH filtered_user AS (
    SELECT writer_id, SUM(price) AS total_sales
    FROM used_goods_board
    WHERE status='DONE'
    GROUP BY writer_id
    HAVING SUM(price) >= 700000
)
SELECT used_goods_user.user_id, nickname, total_sales
FROM filtered_user 
    JOIN used_goods_user ON filtered_user.writer_id=used_goods_user.user_id
ORDER BY total_sales;