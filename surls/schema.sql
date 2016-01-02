drop table if exists entries;
create table entries (
	url text primary key not null,
	links text not null,
	text text
);