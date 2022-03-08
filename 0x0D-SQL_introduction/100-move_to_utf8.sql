-- convert 'hbtn_0c_0' database to UTF8
-- select the database 'hbtn_0c_0'
USE hbtn_0c_0;
-- convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
