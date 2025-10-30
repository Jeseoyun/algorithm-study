SELECT e.dept_id AS DEPT_ID, d.dept_name_en AS DEPT_NAME_EN, ROUND(AVG(e.sal), 0) AS AVG_SAL
FROM hr_employees AS e JOIN hr_department AS d ON e.dept_id=d.dept_id
GROUP BY e.dept_id
ORDER BY AVG_SAL DESC