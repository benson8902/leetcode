SELECT IFNULL(
    (SELECT DISTINCT salary # remove duplicates
FROM Employee
ORDER BY salary DESC 
LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary # OFFSET 1 = start from second one
