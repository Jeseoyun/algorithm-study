-- 틀린 풀이: 기간 동안 렌탈 이력이 있는 SUV/세단을 필터링 하고 30일동안의 대여 금액을 구한다
-- 틀린 이유: 만약 렌탈 이력이 없다면 대여할 수 있음에도 불구하고 필터링 되지 않는다 => LEFT JOIN 사용 필요

# WITH possible_filtered_car AS (
#     SELECT car_id, car_type, daily_fee
#     FROM car_rental_company_car AS car
#     WHERE car_type in ('SUV', '세단') AND NOT EXISTS (
#         SELECT *
#         FROM car_rental_company_rental_history AS hist
#         WHERE hist.car_id=car.car_id AND NOT (hist.end_date < '2022-11-01' OR hist.start_date > '2022-11-30')
#     )
# )
# SELECT fc.car_id, fc.car_type, ROUND(fc.daily_fee*30*dp.discount_rate*0.01, 0) AS fee
# FROM possible_filtered_car AS fc
#     JOIN car_rental_company_discount_plan AS dp ON dp.duration_type='30일 이상' AND fc.car_type=dp.car_type
# WHERE fc.daily_fee*30*dp.discount_rate*0.01 >= 500000 AND fc.daily_fee*30*dp.discount_rate*0.01 < 2000000
# ORDER BY fee DESC, car_type, car_id DESC;


WITH possible_filtered_car AS (
    SELECT car_id, car_type, daily_fee
    FROM car_rental_company_car AS car
    WHERE car_type IN ('세단', 'SUV')
      AND NOT EXISTS (
          SELECT 1
          FROM car_rental_company_rental_history AS hist
          WHERE hist.car_id=car.car_id AND hist.start_date <= '2022-11-30' AND hist.end_date >= '2022-11-01'
      )
)
SELECT fc.car_id, fc.car_type, ROUND(fc.daily_fee*30*(100-dp.discount_rate)*0.01, 0) AS fee
FROM possible_filtered_car AS fc
JOIN car_rental_company_discount_plan dp ON dp.car_type = fc.car_type AND dp.duration_type = '30일 이상'
WHERE ROUND(fc.daily_fee*30*(100-dp.discount_rate)*0.01, 0) >= 500000 AND ROUND(fc.daily_fee*30*(100-dp.discount_rate)*0.01, 0) < 2000000
ORDER BY FEE DESC, car_type ASC, car_id DESC;