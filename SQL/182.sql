/*
182. Duplicate Emails

@date: 2016/05/16

Write a SQL query to find all duplicate emails in a table named Person.
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
*/
Select distinct(a.Email) 
from Person as a, Person as b 
where a.Id != b.Id and a.Email = b.Email;