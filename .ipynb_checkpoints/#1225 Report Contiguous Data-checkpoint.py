"""
Author: Naresh Chava
Date: 05/28/2021

Language: MYSQL 


Table: Failed

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| fail_date    | date    |
+--------------+---------+
Primary key for this table is fail_date.
Failed table contains the days of failed tasks.
Table: Succeeded

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| success_date | date    |
+--------------+---------+
Primary key for this table is success_date.
Succeeded table contains the days of succeeded tasks.
 

A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

Order result by start_date.

The query result format is in the following example:

Failed table:
+-------------------+
| fail_date         |
+-------------------+
| 2018-12-28        |
| 2018-12-29        |
| 2019-01-04        |
| 2019-01-05        |
+-------------------+

Succeeded table:
+-------------------+
| success_date      |
+-------------------+
| 2018-12-30        |
| 2018-12-31        |
| 2019-01-01        |
| 2019-01-02        |
| 2019-01-03        |
| 2019-01-06        |
+-------------------+


Result table:
+--------------+--------------+--------------+
| period_state | start_date   | end_date     |
+--------------+--------------+--------------+
| succeeded    | 2019-01-01   | 2019-01-03   |
| failed       | 2019-01-04   | 2019-01-05   |
| succeeded    | 2019-01-06   | 2019-01-06   |
+--------------+--------------+--------------+

The report ignored the system state in 2018 as we care about the system in the period 2019-01-01 to 2019-12-31.
From 2019-01-01 to 2019-01-03 all tasks succeeded and the system state was "succeeded".
From 2019-01-04 to 2019-01-05 all tasks failed and system state was "failed".
From 2019-01-06 to 2019-01-06 all tasks succeeded and system state was "succeeded".


"""
# Write your MySQL query statement below



with status_change as (
    
    select status, 
DATE_SUB(dt,INTERVAL num DAY),
min(dt) as start_date, 
max(dt) as end_date
from 

(select 'failed' as status, fail_date dt,
    row_number() over(order by fail_date  ASC) as num
from Failed a
where fail_date between STR_TO_DATE('2019-01-01','%Y-%m-%d') and STR_TO_DATE('2019-12-31','%Y-%m-%d') ) a

group by 1,2
              
UNION 

select status, 
DATE_SUB(dt,INTERVAL num DAY) ,
min(dt) as start_date, 
max(dt) as end_date
from 

(select 'succeeded' as status, success_Date dt,
    row_number() over(order by success_Date  ASC) as num
from Succeeded a
where success_Date between STR_TO_DATE('2019-01-01','%Y-%m-%d') and STR_TO_DATE('2019-12-31','%Y-%m-%d')
) a

group by 1,2 )


select status period_state, start_date, end_date

from status_change
order by start_Date
                       



