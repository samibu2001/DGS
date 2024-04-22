create table interpretation(
clinical_significance varchar(30),
variant_origin int,
review_status varchar(150),
submitter varchar(40) unique
);

insert into interpretation(clinical_significance,variant_origin,review_status,submitter)
values('Pathogenic',1,'reviewed_by_expert_panel','ClinGen:CA345709'),('Pathogenic',1,'reviewed_by_expert_panel','ClinGen:CA250432'),
('Pathogenic',1,'reviewed_by_expert_panel','ClinGen:CA003228'),('Pathogenic',1,'reviewed_by_expert_panel','ClinGen:CA000895');

select * from interpretation;
