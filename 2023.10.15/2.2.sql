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
    foreign key (performer_id) references performers (id)
    foreign key (style_id) references styles (id)
	foreign key (publisher_id) references publishers (id)
);

create table songs (
	id int unsigned primary key auto_increment,
	song varchar(100) not null,
	performer_id smallint unsigned not null,
	collection_id smallint unsigned not null,
    style_id tinyint unsigned not null,
	duration time not null,
    foreign key (performer_id) references performers (id)
	foreign key (collection_id) references collection (id)
	foreign key (style_id) references styles (id)
);
