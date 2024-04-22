create table HGVS(
hgvs varchar(200)
);

insert into HGVS(hgvs) values('protein_coding|48/63|c.6997dupA|p.Thr2333fs'),('protein_coding|4/13|c.1592delT|p.Leu531fs'),
('protein_coding|18/24|c.5152T>C|p.Cys1718Arg'),('protein_coding|3/23|c.135-1G>T');

alter table HGVS add primary key(hgvs);

select * from HGVS;
