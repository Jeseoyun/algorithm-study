SELECT product_code, SUM(sales_amount*price) AS sales
FROM product
    JOIN offline_sale ON product.product_id=offline_sale.product_id
GROUP BY product_code
ORDER BY sales DESC, product_code;