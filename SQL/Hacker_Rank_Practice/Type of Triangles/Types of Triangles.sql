/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
Select
CASE WHEN A+B > C AND B+C > A AND C+A > B THEN
        CASE
            WHEN A=B AND B=C THEN 'Equilateral'
            WHEN A=B OR B=C OR C=A THEN 'Isosceles'
            ELSE 'Scalene'
        END
    ELSE 'Not A Triangle'
END AS 'TYPE OF TRIANGLE'
FROM TRIANGLES;