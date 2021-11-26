drop database PiHome;
create database PiHome;
use PiHome;
create table users (username varchar(255), password varchar(255), first_name varchar(255), Last_name varchar(255), email varchar(255), phone_number varchar(255), last_login datetime, api_key varchar(255));
show tables;
alter table users add unique (username, api_key);
alter table users add primary key (username, api_key);
truncate users;
insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) 
values 
('angel', 'password', 'Angel', 'Santander', 'angelsantander609@gmail.com', '8770262013', now(), 'abhikuchnhihai'),
('gustavo', 'password', 'Gustavo', 'Jiménez', 'jimenezruizga@gmail.com', '0182656548', now(), 'abhikuchnhihai'),
('agustin', 'password', 'Agustín', 'Hernández', 'agustinht.fi@gmail.com', '5479413892', now(), 'abhikuchnhihai'),
('alejandro', 'password', 'Alejandro', 'Anaya', 'yair.anaya@ingenieria.unam.edu', '4875142894', now(), 'abhikuchnhihai');
select * from users;