/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with cte as ( select RANK() OVER (PARTITION BY Occupation ORDER BY Name) as Rank,
             case when Occupation='Doctor' then Name else null end as doctor, 
             case when Occupation='Professor' then Name else null end as prof, 
             case when Occupation='Singer' then Name else null end as singer, 
             case when Occupation='Actor' then Name else null end as actor from Occupations) 
select min(doctor), min(prof), min(singer), min(actor) from cte group by Rank