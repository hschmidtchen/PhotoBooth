drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	path text not null,
	session_id integer not null,
	in_session_id integer not null
);