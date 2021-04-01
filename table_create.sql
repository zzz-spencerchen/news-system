CREATE DATABASE new_database;

use new_database;

CREATE TABLE t_type(
id INT UNSIGNED PRIMARY KEY auto_increment,
type varchar(20) NOT NULL UNIQUE
);

INSERT INTO t_type(type) value("breaking news"),("sports"),("sience"),("history");


CREATE TABLE t_role(
id INT UNSIGNED PRIMARY KEY auto_increment,
role VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO t_role (role) VALUES("admin"), ("news_editor");


CREATE TABLE t_user(
id INT UNSIGNED PRIMARY KEY auto_increment,
username VARCHAR(20) NOT NULL UNIQUE,
password VARCHAR(500) NOT NULL,
email VARCHAR(50) NOT NULL,
role_id INT UNSIGNED NOT NULL,
INDEX(username)
);


INSERT INTO t_user(username, password,email, role_id) values("AAA", HEX(AES_ENCRYPT("123456","hash")), "AAA@gmail.com", 1);


INSERT INTO t_user(username, password,email, role_id) values("BBB", HEX(AES_ENCRYPT("123456","hash")), "BBB@gmail.com", 2);


CREATE TABLE t_news(
id INT UNSIGNED PRIMARY KEY auto_increment,
title VARCHAR(40) NOT NULL,
editor_id INT UNSIGNED NOT NULL,
type_id INT UNSIGNED NOT NULL,
content_id CHAR(12) NOT NULL,
is_top TINYINT UNSIGNED NOT NULL,
create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
status ENUM("unfinished","processing","valid", "hide") NOT NULL,
INDEX(editor_id),
INDEX(type_id),
INDEX(status),
INDEX(create_time),
INDEX(is_top)
);