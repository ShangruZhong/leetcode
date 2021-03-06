/*
184. Department Highest Salary

@date: 2016/05/16

The Employee table holds all employees. Every employee has an Id, 
a salary, and there is also a column for the department Id.
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in 
each of the departments. For the above tables, Max has the highest 
salary in the IT department and Henry has the highest salary in the 
Sales department.
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
*/
select d.Name as Department, e.Name as Employee, maxS.maxSalary as Salary 
from (select e.DepartmentId, Max(Salary) as maxSalary 
	from Employee as e 
	left join Department as d 
	on e.DepartmentId = d.Id group by e.DepartmentId) 
as maxS, Employee as e, Department as d 
where maxS.DepartmentId = e.DepartmentId and maxS.maxSalary = e.Salary 
and e.DepartmentId = d.Id;