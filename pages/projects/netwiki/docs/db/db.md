Like many web-based applications, NetWiki makes use of a relational database.

## Backend Support
At first, for development purposes, NetWiki would just use SQLite3.

There are plans to add the configuration option to use a different database engine such as MySQL/MariaDB and PostgresDB.

## Schema
NetWiki uses a database with a non-configurable schema. This greatly simplifies code relating to the setup, management and access of the database.

### Table: config
The "config" table stores the configuration of the application.

### Table: pages
