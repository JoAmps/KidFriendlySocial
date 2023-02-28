/*create the user at localhost */
CREATE USER 'authenticate_user'@'local_host' IDENTIFIED BY 'Auth123';

/*create the database */
CREATE DATABASE authentication;

/*grant all privileges to admin*/
GRANT ALL PRIVILEGES ON authentication.* TO 'authenticate_user'@'local_host'; 

/* use the database*/
USE authentication;

/* create the user with the id, email and password*/
CREATE TABLE user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

/* after user has access to auth service api */
INSERT INTO user (email, password) VALUES ('ampaduh@gmail.com', 'admin_rights');