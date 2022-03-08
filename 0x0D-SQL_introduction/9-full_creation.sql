-- create a table 'second_table' in database 'hbtn_0c_0'
-- CREATE TABLE
CREATE TABLE IF NOT EXISTS second_table (
       id int,
       name varchar(256),
       score int
);
-- add multiples rows
-- INSERT INTO .. VALUES ..
INSERT INTO second_table (id, name, score)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
