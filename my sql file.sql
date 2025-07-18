CREATE DATABASE IF NOT EXISTS salarie;
USE salarie;

/* Top 20 Job Titles by Average Salary */
SELECT 
    job_title AS Job_Title,
    ROUND(AVG(salary_in_usd), 2) AS Average_Salary_USD,
    COUNT(*) AS Employee_Count
FROM cleaned_salaries
GROUP BY job_title
ORDER BY Average_Salary_USD DESC
LIMIT 20;

/* Employee Distribution by Country and Remote Ratio */
SELECT 
    employee_residence AS Country,
    remote_ratio AS Remote_Percentage,
    COUNT(*) AS Employee_Count
FROM cleaned_salaries
GROUP BY Country, Remote_Percentage
ORDER BY Employee_Count DESC
LIMIT 20;
/*Average Salary per Year*/
SELECT 
    work_year AS Year,
    ROUND(AVG(salary_in_usd), 2) AS Average_Salary_USD
FROM cleaned_salaries
GROUP BY Year
ORDER BY Year;

/* Top 20 Countries by Total Salary Paid */
SELECT 
    employee_residence AS Country,
    ROUND(SUM(salary_in_usd), 2) AS Total_Salary_USD,
    COUNT(*) AS Employee_Count
FROM cleaned_salaries
GROUP BY Country
ORDER BY Total_Salary_USD DESC
LIMIT 20;

/* Average Salary by Company Size */
SELECT 
    company_size AS Company_Size,
    COUNT(*) AS Employee_Count,
    ROUND(AVG(salary_in_usd), 2) AS Average_Salary_USD
FROM cleaned_salaries
GROUP BY Company_Size
ORDER BY Company_Size;

/* Average Salary by Experience Level */
SELECT 
    experience_level AS Experience_Level,
    COUNT(*) AS Employee_Count,
    ROUND(AVG(salary_in_usd), 2) AS Average_Salary_USD
FROM cleaned_salaries
GROUP BY Experience_Level;





