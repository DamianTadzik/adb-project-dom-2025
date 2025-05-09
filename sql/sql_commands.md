1. Log into database control panel

```https://mysql.agh.edu.pl/phpMyAdmin/index.php```
Use credentials provided in private message, brzanad2 and so on... 

2. Commands used to create databases in the panel

```
CREATE TABLE locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(10),
    latitude DOUBLE,
    longitude DOUBLE
);

CREATE TABLE measurements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT,
    parameter VARCHAR(50),
    value FLOAT,
    unit VARCHAR(10),
    timestamp DATETIME,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);
```
3. Done

