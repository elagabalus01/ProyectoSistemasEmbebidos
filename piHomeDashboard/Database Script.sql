drop database ARMS;
create database ARMS;
use ARMS;
create table users (username varchar(255), password varchar(255), first_name varchar(255), Last_name varchar(255), email varchar(255), phone_number varchar(255), last_login datetime, api_key varchar(255));
show tables;
select * from users;
alter table users add unique (username, api_key);
alter table users add primary key (username, api_key);
truncate users;

insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) 
values ('angel', 'password', 'Angel', 'Santander', 'angelsantander609@gmail.com', '8770262013', now(), 'abhikuchnhihai');

create table Node (deviceID varchar(255), username varchar(255), field_name varchar(255), temperature int, humidity int, moisture int, light int, 
foreign key (username) references users(username), primary key (deviceID));
select * from Node;
select field_name, temperature, humidity, moisture, light from Node where username="amansingh";

insert into Node (deviceID, username, field_name, temperature, humidity, moisture, light)
values('dev1', 'angel', 'Rose Garden', 45, 54, 100, 600);
insert into Node (deviceID, username, field_name, temperature, humidity, moisture, light)
values('dev2', 'angel', 'Samy Garden', 45, 54, 100, 600);

select * from Node;

create table Rosegarden (deviceID varchar(255), temperature int, humidity int, moisture int, light int, date_time datetime,
foreign key (deviceID) references Node(deviceID));

insert into Rosegarden (deviceID, temperature, humidity, moisture, light, date_time)
values('dev2', 45, 54, 100, 600, now());

select * from users where username = "hellboy";
update users set last_login = now() where username = "hellboy";

select * from Rosegarden;
select * from (select * from Rosegarden order by date_time desc limit 10) dummy order by date_time asc;
select * from (select * from Rosegarden order by date_time desc limit 10) dummy order by date_time asc;

