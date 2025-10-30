WITH bitmask AS (
    SELECT
        SUM(CASE WHEN name="Python" THEN code END) AS py_code, 
        SUM(CASE WHEN name="C#" THEN code END) AS csharp_code,
        SUM(CASE WHEN category="Front End" THEN code END) AS fe_code
    FROM skillcodes
), 
graded AS (
    SELECT 
        CASE
            WHEN (d.skill_code & b.py_code > 0) AND (d.skill_code & b.fe_code > 0) THEN "A"
            WHEN (d.skill_code & b.csharp_code > 0) THEN "B"
            WHEN (d.skill_code & b.fe_code > 0) THEN "C"
        END
        AS final_grade, 
    d.id
    FROM developers AS d
        CROSS JOIN bitmask AS b
)

SELECT g.final_grade AS GRADE, g.id AS ID, d.email AS EMAIL
FROM developers AS d
    JOIN graded AS g ON d.id=g.id
WHERE g.final_grade IS NOT NULL
ORDER BY g.final_grade, d.id