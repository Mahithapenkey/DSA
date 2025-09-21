# Write your MySQL query statement below
select(SELECT distinct salary from Employee
order by salary DESC
Limit 1 
Offset 1)as SecondHighestSalary;
