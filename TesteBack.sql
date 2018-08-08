drop table tb_customer_account

create table tb_customer_account (
	id_customer int NOT NULL,
	cpf_cnpj numeric,
	nm_customer char(20),
	is_active bit,
	vl_total float
	PRIMARY KEY(id_customer)
);

select * from tb_customer_account