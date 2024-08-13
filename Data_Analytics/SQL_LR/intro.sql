SELECT * FROM customer_data;

SELECT COUNT(*) as row_count FROM customer_data; -- counting row


-- total kinds
SELECT
SUM(kidhome) as total_kinds,
COUNT(*) as total_rows
FROM customer_data;


WITH id_value_counts as (
	SELECT id, count(id) as id_count
	FROM customer_data
	GROUP BY id
)
SELECT * from id_value_counts
WHERE id_count > 1
ORDER BY id_count DESC
-- no rows indicating id not reffering to any household.


---Looking into year.
SELECT 
year_birth, count(year_birth) as count_of_values
from customer_data
GROUP BY year_birth
ORDER BY year_birth DESC;

-- undersatning the year_birth
WITH YEAR_OF_BITH_COUNT AS (
	SELECT 
	year_birth, count(year_birth) as count_of_values
	from customer_data
	GROUP BY year_birth
	ORDER BY year_birth DESC
)
SELECT
    COUNT(count_of_values) AS total_years,
    AVG(count_of_values) AS average_count,
    MIN(count_of_values) AS min_count,
    MAX(count_of_values) AS max_count,
    -- APPROX_QUANTILES(count_of_values, 100)[OFFSET(50)] AS median_count,
    STDDEV(count_of_values) AS stddev_count
FROM
	YEAR_OF_BITH_COUNT;



