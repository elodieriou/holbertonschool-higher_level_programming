-- create a database 'hbtn_0d_2' and user 'user_0d_2'
-- CREATE IF NOT EXIST DATABASE/USER
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- give only SELECT privilege to the user
-- GRANT SELECT ON .. TO ..
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
