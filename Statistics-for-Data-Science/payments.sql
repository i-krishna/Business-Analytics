SELECT
    f.name,
    COUNT(cp.payment) AS total_payments,
    MIN(cp.payment) AS min_payment,
    MAX(cp.payment) AS max_payment,
    ROUND(AVG(cp.payment), 2) AS avg_payment
FROM
    funds AS f
JOIN
    coupon_payments AS cp ON f.id = cp.fund_id
GROUP BY
    f.name
HAVING
    avg_payment > 500.00
ORDER BY
    f.name ASC;
