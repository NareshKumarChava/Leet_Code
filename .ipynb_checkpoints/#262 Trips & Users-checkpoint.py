"""
Author: Naresh Chava
Date: 05/28/2021

Language: MYSQL 

Cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03"

The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Return the result table in any order. Round Cancellation Rate to two decimal points.

"""




# Cancellation rate: #of trips cancelled/#of total trips
#It must be zero for days if there are no cancellations
#Round to 2 decimals & Order by date

select request_at as Day,
round(sum(case when Status!='completed' then 1 else 0 end)/count(Id),2) as "Cancellation Rate" 

from Trips a
left join Users b
on a.Driver_Id=b.Users_Id
left join Users c
on a.Client_Id=c.Users_Id

where b.Banned='No' and c.Banned='No' 
and a.request_at between STR_TO_DATE(20131001, '%Y%m%d') and STR_TO_DATE(20131003, '%Y%m%d')

group by 1
order by 1


