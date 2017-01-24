/*
180. Consecutive Numbers

@date: 2016/05/16

Write a SQL query to find all numbers that appear at least three times 
consecutively.
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that 
appears consecutively for at least three times.
*/
Select distinct(l1.Num) 
from Logs l1, Logs l2, Logs l3 
where l1.Id+1 = l2.Id and l1.Id+2 = l3.Id 
and l1.Num = l2.Num and l1.Num = l3.Num;