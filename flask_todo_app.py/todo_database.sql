create database todo;
use todo;

create table todolist(
sno int primary key , 
title char(100) not null , 
descp char(225) not null , 
date_created timestamp not null default current_timestamp
);


ALTER TABLE todolist CHANGE sno sno INT  AUTO_INCREMENT;
select * from todolist	;	
delete  from todolist;

ALTER TABLE todolist AUTO_INCREMENT = 1;


create database lib_manag;


use lib_manag;

create table user_login(
username char(50) not null , 
password char(50) not null 
);



