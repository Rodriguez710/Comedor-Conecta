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
curso		int				primary key not null,
centro		varchar(200) 	not null
);

create table clase(
letra	char	primary key,
curso 	int		not null,
constraint fk_curso_clase foreign key (curso) references cursos (curso)
	on delete cascade on update cascade
);

create table alumno(
nre			int				primary key,
nombre		varchar(200)	not null,
letra_clase	char			not null,
curso		int				not null,
madre		varchar(200)		not null,
constraint fk_clase foreign key (letra_clase) references clase(letra)
	on delete cascade on update cascade
);

create table madre(
id			int 			primary key auto_increment,
nombre		varchar(200)	not null,
nre_hijo 	int				not null,	
constraint fk_nre_hijo foreign key (nre_hijo) references alumno (nre)
	on delete cascade on update cascade
);