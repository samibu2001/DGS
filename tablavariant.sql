create table variant(
varianttype varchar(80),
ID int unique not null,
alt varchar(10),
primary key(ID)
);

insert into variant(varianttype,ID,alt) values('frameshift_variant',587781299,'TA'),('frameshift_variant',180177102,'C'),
('missense_variant',80356993,'G'),('splice_acceptor_variant&intron_variant',80358158,'A');

select * from variant;