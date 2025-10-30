WITH total_score AS (
    SELECT emp_no, year, SUM(score) AS score_sum
    FROM hr_grade
    GROUP BY emp_no, year
), highest_score AS (
    SELECT MAX(score_sum) AS highest_val
    FROM total_score
)

SELECT 
    ts.score_sum AS SCORE, 
    ts.emp_no AS EMP_NO, 
    e.emp_name AS EMP_NAME, 
    e.position AS POSITION, 
    e.email AS EMAIL
FROM total_score AS ts
    JOIN hr_employees AS e ON ts.emp_no=e.emp_no
    JOIN highest_score AS hs ON ts.score_sum=hs.highest_val
GROUP BY emp_no, year
