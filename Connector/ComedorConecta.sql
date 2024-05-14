drop database if exists ComedorConecta;
create database ComedorConecta;
use ComedorConecta;

create table users(
id			int				auto_increment primary key,
username	varchar(100)	not null,
email		varchar(300)	unique not null,
passwd		varchar(255)	not null,
centro		varchar(200) 	not null,
telefono 	varchar(15)		null
);

create table cursos(
curso		int				primary key not null
);
insert into cursos values (1);
insert into cursos values (2);
insert into cursos values (3);
insert into cursos values (4);
insert into cursos values (5);
insert into cursos values (6);

create table clase(
letra	char	not null primary key,
curso 	int		not null,
constraint fk_curso_clase foreign key (curso) references cursos (curso)
	on delete cascade on update cascade
);
insert into clase (letra, curso) values ('A', 1);
insert into clase (letra, curso) values ('B', 2);
insert into clase (letra, curso) values ('C', 3);
insert into clase (letra, curso) values ('D', 4);
insert into clase (letra, curso) values ('E', 5);
insert into clase (letra, curso) values ('F', 6);


create table alumno(
nre			int				primary key unique,
nombre		varchar(200)	not null,
curso		int				not null,
clase		char			not null,
madre		varchar(200)	not null,
constraint fk_clase foreign key (clase) references clase(letra)
	on delete cascade on update cascade
);

create table madre(
id			int 			primary key auto_increment,
nombre		varchar(200)	not null,
nre_hijo 	int				not null,	
constraint fk_nre_hijo foreign key (nre_hijo) references alumno (nre)
	on delete cascade on update cascade
);

select * from alumno;
