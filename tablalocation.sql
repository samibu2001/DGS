create table location(
pos int,
ref varchar(30),
primary key(pos)
);

insert into location(pos,ref) values(108198392,'T'),(23646274,'CA'),(41215954,'A'),(41258551,'C');

select * from location;