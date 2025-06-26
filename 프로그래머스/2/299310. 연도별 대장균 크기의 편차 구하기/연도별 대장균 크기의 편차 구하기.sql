-- 1. 연도별 크기 가장 큰 값 테이블 생성
-- 2. 원래 테이블이랑 JOIN해서 편차 구하기

WITH year_max AS (
    SELECT YEAR(differentiation_date) AS d_year, MAX(size_of_colony) AS max_size
    FROM ecoli_data
    GROUP BY YEAR(differentiation_date)
)

SELECT year_max.d_year AS year, ABS(ecoli_data.size_of_colony-year_max.max_size) AS year_dev, ecoli_data.id
FROM ecoli_data 
    JOIN year_max ON YEAR(ecoli_data.differentiation_date)=year_max.d_year
ORDER BY d_year, year_dev;
