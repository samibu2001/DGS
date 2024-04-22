create table data(
name varchar(8),
URL varchar(300)
);

insert into data(name, URL) values('ClinVar','https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz');

select * from data;