/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
WITH GROUP_LM_RESULT AS (
SELECT COUNT(DISTINCT LEAD_MANAGER_CODE) AS COUNT_LM, COMPANY_CODE FROM LEAD_MANAGER
    GROUP BY COMPANY_CODE
),
GROUP_SM_RESULT AS (
SELECT COUNT(DISTINCT SENIOR_MANAGER_CODE) AS COUNT_SM, COMPANY_CODE FROM SENIOR_MANAGER
    GROUP BY COMPANY_CODE
),
GROUP_M_RESULT AS (
SELECT COUNT(DISTINCT MANAGER_CODE) AS COUNT_M, COMPANY_CODE FROM MANAGER
    GROUP BY COMPANY_CODE
),
GROUP_E_RESULT AS (
SELECT COUNT(DISTINCT EMPLOYEE_CODE) AS COUNT_E, COMPANY_CODE FROM EMPLOYEE
    GROUP BY COMPANY_CODE
),
ALL_GROUP_RESULT AS (
SELECT LM.COMPANY_CODE, COUNT_LM, COUNT_SM, COUNT_M, COUNT_E FROM GROUP_LM_RESULT AS LM
    LEFT JOIN GROUP_SM_RESULT AS SM
    ON LM.COMPANY_CODE = SM.COMPANY_CODE
    LEFT JOIN GROUP_M_RESULT AS M
    ON LM.COMPANY_CODE = M.COMPANY_CODE
    LEFT JOIN GROUP_E_RESULT AS E
    ON LM.COMPANY_CODE = E.COMPANY_CODE
)
SELECT C.COMPANY_CODE, C.FOUNDER, LM.COUNT_LM, LM.COUNT_SM, LM.COUNT_M, LM.COUNT_E FROM COMPANY AS C
LEFT JOIN ALL_GROUP_RESULT AS LM
ON C.COMPANY_CODE = LM.COMPANY_CODE
ORDER BY C.COMPANY_CODE;


/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT C.COMPANY_CODE, C.FOUNDER, COUNT(DISTINCT LM.LEAD_MANAGER_CODE), COUNT(DISTINCT SM.SENIOR_MANAGER_CODE), COUNT(DISTINCT M.MANAGER_CODE), COUNT(DISTINCT E.EMPLOYEE_CODE)
FROM COMPANY AS C, LEAD_MANAGER AS LM, SENIOR_MANAGER AS SM, MANAGER AS M, EMPLOYEE AS E
WHERE C.COMPANY_CODE = LM.COMPANY_CODE AND
C.COMPANY_CODE = SM.COMPANY_CODE AND
C.COMPANY_CODE = M.COMPANY_CODE AND
C.COMPANY_CODE = E.COMPANY_CODE
GROUP BY C.COMPANY_CODE, C.FOUNDER
ORDER BY COMPANY_CODE;
