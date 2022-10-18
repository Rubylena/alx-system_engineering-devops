# Tasks
0. get MySQL installed on both your web-01 and web-02 servers.
1. create a user and password for both MySQL databases which will allow the checker access to them.
2.  have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.
3. On your primary MySQL server (web-01), create a new user for the replica server.
4. 4-mysql_configuration_primary: The MySQL my.conf configuration file used to set up my first server as a primary database server on the database tyrell_corp.

4-mysql_configuration_replica: The MySQL my.conf configuration file used to set up my second server as the replica database server on the database tyrell_corp.

* [5-mysql_backup](./5-mysql_backup): Bash script that generates a compressed
`tar.gz` archive from a MySQL dump.
  * Usage: `./5-mysql_backup <MySQL root password>`
  * Generates a dump containing all MySQL databases on the root server.
  * Names the resulting tar archive in the format `day-month-year.tar.gz`.
