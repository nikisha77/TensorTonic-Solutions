-- Returns: name, salary.
SELECT name, salary
FROM employees
WHERE salary > 70000
  AND department IN ('Engineering', 'Marketing');