-- Running total
SELECT Vaccine Data, Month, Type, SUM(Vaccine Data) OVER (ORDER BY TYPE) as total_sum
From VaccineDataset

-- Aggregation (showing the average dose amount for each type)
SELECT Vaccine Data,dose_amount,location, ROUND(AVG(dose_amount) OVER(PARTITION BY Type)) as avg_dose_amount
FROM VaccineDataset
ORDER BY dose_amount DESC


-- Common table Expression
WITH subset as (
SELECT id as id
From id
WHERE location = "Tampines"
AND Status = "Fully_Vacc"
)

Select *
From vaccine_data
WHERE id in (SELECT id from subset)

-- Ranking the Data
SELECT id, amount,
RANK () OVER (ORDER BY amount desc)
FROM source

-- Can alse use DENSE_RANK() if you dont want to skip rows with same value

-- Adding Subtotals
-- Generates a subtotal amount to the columns
-- E.G.
SELECT type, Gender sum(amount) as total_amount
FROM source
GROUP BY Type, id with ROLLUP

-- TYPE		Gender		total_amount
-- PFIZER	M		3000
-- PFIZER	F		2000
-- PFIZER	NULL		5000
-- Moderna	M		1500
-- Moderna	F		2000
-- Moderna	NULL		3500
-- NULL		NULL		8500


-- Temporary Functions

CREATE TEMPORARY FUNCTION get_age_group(age varchar) AS (
  CASE WHEN age < 20 THEN "Below 20"
	WHEN age > 19 AND age < 30 "Below 30"
	ELSE "Senile" 
)

SELECT id, get_age_group(age) as age_group
from DATA


-- Variance and Standard Deviation
SELECT VARIANCE(amount) AS var_amount, VAR_POP(amount) AS var_pop_amount, STDDEV_SAMP(amount) AS var_samp_amount, STDDEV_SAMP(amount) as stddev_sample_amount, STDDEV_POP(amount) as stddev_pop_amount
FROM DATA

-- VAR_POP population variance
-- VAR_SAMP sample variance
-- STDDEV_SAMP sample stadard deviation
-- STDDEV_POP population standard deviation


-- Correlated Subqueries
SELECT location, vacc_type, dose_amount, round(SELECT AVG(dose_amount)
									FROM vaccine_data
									WHERE v1.vacc_type = v2.vacc_type) as avg_dose_amount
FROM vaccine_data v1
WHERE dose_amount < (SELECT 
					AVG(dose_amount)
					FROM vaccine_date v2
					WHERE v1.vacc_type = v2.vacc_type
					GROUP BY vacc_type)
ORDER BY dose_amount

-- Case when clause (GROUPING into category)
SELECT location,dose_amount,(SELECT ROUND(AVG(dose_amount)) FROM vaccine_data) as avg_dose_amount,
(CASE WHEN dose_amount > (SELECT AVG(dose_amount) FROM vaccine_data) THEN 'higher_than_average'
ELSE 'lower_than_average' END) as Salary_Case
FROM vaccine_data


