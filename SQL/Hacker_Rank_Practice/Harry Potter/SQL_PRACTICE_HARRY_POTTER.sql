-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
-- HARRY POTTER BASIC JOIN OLIVANDER'S INVENTORY

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT C.ID, C.AGE, C.COINS_NEEDED, C.POWER
FROM (
    SELECT W.ID AS ID, P.AGE AS AGE, W.COINS_NEEDED AS COINS_NEEDED, W.POWER AS POWER,
    MIN(COINS_NEEDED) OVER (PARTITION BY P.AGE, W.POWER) AS MIN_COINS
    FROM WANDS AS W
    INNER JOIN WANDS_PROPERTY AS P
    ON W.CODE = P.CODE
    WHERE P.IS_EVIL = 0
) AS C
WHERE C.COINS_NEEDED = C.MIN_COINS
ORDER BY C.POWER DESC, C.AGE DESC;