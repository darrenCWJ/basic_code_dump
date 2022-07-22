/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CONCAT(NAME, '(' , SUBSTRING(OCCUPATION,1,1) , ')')
FROM OCCUPATIONS
ORDER BY NAME;
SELECT CONCAT('There are a total of ', COUNT(OCCUPATION)," ", lower(OCCUPATION), "s.")
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION;