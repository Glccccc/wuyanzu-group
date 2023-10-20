drop database if exists mus_library;

create database mus_library;

use mus_library;


create table styles (
    id tinyint unsigned primary key auto_increment,
    style varchar(50) not null unique
);

create table performers (
    id smallint unsigned primary key auto_increment,
    performer varchar(100) not null unique
);

create table publishers (
    id smallint unsigned primary key auto_increment,
    publisher varchar(100) not null unique,
    country varchar(50) not null
);

create table collections (
    id smallint unsigned primary key auto_increment,
    collection varchar(100) not null unique,
    performer_id smallint unsigned not null,
    `date` year,
    style_id tinyint unsigned not null,
    publisher_id smallint unsigned not null,
    foreign key (performer_id) references performers (id),
    foreign key (style_id) references styles (id)  ,
	foreign key (publisher_id) references publishers (id)
);

create table songs (
	id int unsigned primary key auto_increment,
	song varchar(100) not null,
	performer_id smallint unsigned not null,
	collection_id smallint unsigned not null,
    style_id tinyint unsigned not null,
	duration time not null,
    foreign key (performer_id) references performers (id),
	foreign key (collection_id) references collections (id),
	foreign key (style_id) references styles (id)
);


 -- MySQL  localhost:3306 ssl  mus_library  SQL > \. 2.2.sql
-- Query OK, 4 rows affected (0.0472 sec)
-- Query OK, 1 row affected (0.0021 sec)
-- Default schema set to `mus_library`.
-- Fetching global names, object names from `mus_library` for auto-completion... Press ^C to stop.
-- Query OK, 0 rows affected (0.0391 sec)
-- Query OK, 0 rows affected (0.0249 sec)
-- Query OK, 0 rows affected (0.0364 sec)
-- Query OK, 0 rows affected (0.0481 sec)
-- Query OK, 0 rows affected (0.0397 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL >
