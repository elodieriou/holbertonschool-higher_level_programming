-- create the user 'user_0d_1'
-- CREATE USER .. IDENTIFIED BY ..
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- give all privileges on the user
-- GRANT ALL PRIVILEGES
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
