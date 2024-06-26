This project contains 0x0E. SQL - More queries

General
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION


How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$



Tasks
0. My privileges!
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

1. Root user
Write a script that creates the MySQL server user user_0d_1.
user_0d_1 should have all privileges on your MySQL server
The user_0d_1 password should be set to user_0d_1_pwd
If the user user_0d_1 already exists, your script should not fail

2. Read user
Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
The user_0d_2 password should be set to user_0d_2_pwd
If the database hbtn_0d_2 already exists, your script should not fail
If the user user_0d_2 already exists, your script should not fail

3. Always a name
Write a script that creates the table force_name on your MySQL server.
force_name description:
id INT
name VARCHAR(256) can’t be null
The database name will be passed as an argument of the mysql command
If the table force_name already exists, your script should not fail

4. ID can't be null
Write a script that creates the table id_not_null on your MySQL server.
id_not_null description:
id INT with the default value 1
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table id_not_null already exists, your script should not fail


4. ID can't be null
Write a script that creates the table id_not_null on your MySQL server.
id_not_null description:
id INT with the default value 1
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table id_not_null already exists, your script should not fail


6. States table
Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
states description:
id INT unique, auto generated, can’t be null and is a primary key
name VARCHAR(256) can’t be null
If the database hbtn_0d_usa already exists, your script should not fail
If the table states already exists, your script should not fail


7. Cities table
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
cities description:
id INT unique, auto generated, can’t be null and is a primary key
state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
name VARCHAR(256) can’t be null
If the database hbtn_0d_usa already exists, your script should not fail
If the table cities already exists, your script should not fail


8. Cities of California
Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
The states table contains only one record where name = California (but the id can be different, as per the example)
Results must be sorted in ascending order by cities.id
You are not allowed to use the JOIN keyword
The database name will be passed as an argument of the mysql command


9. Cities by States
Write a script that lists all cities contained in the database hbtn_0d_usa.
Each record should display: cities.id - cities.name - states.name
Results must be sorted in ascending order by cities.id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command


10. Genre ID by show
Import the database dump from hbtn_0d_tvshows to your MySQL server: download
Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
