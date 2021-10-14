# DSSA Data Gathering & Warehousing

**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 6

---
## ETL with Databases and Python

---

### Introduction
__Extract, Transform & Load__ (ETL) is a process that extracts, transforms, and loads data from one or multiple sources to a __data warehouse__ or other unified data repository.

The following repository contains instructions for connection to a PostgreSQL database called `dvdrental` and writing your own ETL to create a __star-schema__ in the Data Warehouse (called dw) for the first Lab Assignment

### About the DVD Rental Database
The DVD rental database represents the business processes of a DVD rental store as an OLTP PostgreSQL DB. 
> The DVD rental database has many objects including:
>15 tables
>1 trigger
>7 views
>8 functions
>1 domain
>13 sequences

15 tables in the DVD Rental database:

> * actor – stores actors data including first name and last name.
> * film – stores film data such as title, release year, length, rating, etc.
> * film_actor – stores the relationships between films and actors.
> * category – stores film’s categories data.
> * film_category- stores the relationships between films and categories.
> * store – contains the store data including manager staff and address.
> * inventory – stores inventory data.
> * rental – stores rental data.
> * payment – stores customer’s payments.
> * staff – stores staff data.
> * customer – stores customer data.
> * address – stores address data for staff and customers
> * city – stores city names.
> * country – stores country names.

__Entity Relationship Diagrams__ - An entity relationship diagram (ERD) shows the relationships of entity sets stored in a database. An entity in this context <u>is an object </u>, a component of data. 

By defining the entities, their attributes, and showing the relationships between them, an ER diagram illustrates the logical structure of databases.

The __DVD Rental Database ERD__ can be found in the `docs` folder of this repository as a PDF

---

### Goal
The main objective of this lab is to implement an ETL process in python to create a __Star-Schema__ in a Data Warehouse that looks like the following:

![img](assets/img/star-schema.png)

Put simply, we need to:
1. _extract_ data from a OLTP database called `dvdrental`
2.  _transform_ it by creating an aggregation of the count of rentals
3. _load_ the data into the `dw` Data Warehouse

In our repository we need to do the following:
1. Define the star-schema 

__A walk-through of each table__

__Fact Table: FACT_RENTAL__
- `sk_customer` is the `customer_id` from customer table 
- `sk_date` is `rental_date` from the rental table
- `sk_store` the `store_id` from the store table
- `sk_film` is the `film_id` from the film table
- `sk_staff` is the `id` from the staff table
- `count_rentals` A count of the total rentals grouped by all other fields in the table
 
__Dimension Table: STAFF__
- `sk_staff` is the `id` field from the staff table
- `name` a concatenation of `first_name` and `last_name` from the staff table
- `email` is the `email` field from the staff table


__Dimension Table: CUSTOMER__
- `sk_customer` is the `customer_id` from customer table
- `name` is the concatenation of `first_name` & `last_name` from the customer table
- `email` is the customer's email 

__Dimension Table: DATE__
- `sk_date` is unique `rental_date` used as a primary key
- `quarter` is a column formatted from `rental_date` for quarter of the year
- `year` is a column formatted from `rental_date` for year
- `month` is a column formatted from `rental_date` for month of the year
- `day` is a column formatted from `rental_date` for day of the month

__Dimension Table: STORE__ 
- `sk_store` the `store_id` from the store table
- `name`  is a concatenation of `first_name` & `last_name` from the staff table
- `address` is the `address` field from the address table
- `city` is the `city` field from the city table
- `state` is the `district` field from the address table
- `country` is the `country field from the country table

__Dimension Table: FILM__
- `sk_film` is the `film_id` from the film table
- `rating_code` is the `rating` field from the film table
- `film_duration` is the `length` field from the film table
- `rental_duration` is the `rental_duration` from the film table
- `language` is the `name` field from the language table
- `release_year` is the `release_year` from the film table
- `title` is the `title` field from the film table
 
---

## Setup 

### Connecting to the Database

* database (OLTP): `dvdrental`
* database (DW): `dw` 
* hostname = `173.61.46.34`
* port number = `5432`

__Team #1__ 

> username = dssa_team_1
> password = StocktonDSSA!
* James, Halkes, Lluore and Benjamin, 

__Team #2__
> username = dssa_team_2
> password = StocktonDSSA!
* Brennan, Rodriguez, Weber and Withers

__Team #3__
> username = dssa_team_3
> password = StocktonDSSA!

__Team #4__
> username = dssa_team_4
> password = StocktonDSSA!

__Python Library Documentation__
[SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
[Pandas](https://pandas.pydata.org/docs/)

### Install requirements.txt
```python
# Install requirement libs by using pip
pip install -r requirements.txt
```

__Steps:__
__1. Connect to the Data Warehouse__
__1. Define the Data Warehouse Schema in the models folder:__
    Database schema defines the structure of a database system, in terms of tables, columns, fields, and the relationships between them. Schemas can be defined in raw SQL, or through the use of SQLAlchemy’s ORM feature. Use the py files to define the correct schema for each dimension table and fact table
    