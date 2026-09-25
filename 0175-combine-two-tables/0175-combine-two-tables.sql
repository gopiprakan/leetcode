# Write your MySQL query statement below
select p.firstName,p.lastName,a.city,a.state FROM Person p left join address a on p.personId=a.personId;