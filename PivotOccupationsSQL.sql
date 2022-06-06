--https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true


select doctor,professor,singer,actor from (select * from 
(select Name, occupation, (ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name)) as row_num from occupations order by name asc) 
pivot ( min(name) for occupation in ('Doctor' as doctor,'Professor' as professor,'Singer' as singer,'Actor' as actor)) order by row_num);



create table OCCUPATIONS
(
name varchar2(20),
occupation varchar2(20)
)

insert into occupations values('Samantha','Doctor');
insert into occupations values('Julia','Actor');
insert into occupations values('Maria','Actor');
insert into occupations values('Meera','Singer');
insert into occupations values('Ashley','Professor');
insert into occupations values('Ketty','Professor');
insert into occupations values('Christeen','Professor');
insert into occupations values('Jane','Actor');
insert into occupations values('Jenny','Doctor');
insert into occupations values('Priya','Singer');

commit;