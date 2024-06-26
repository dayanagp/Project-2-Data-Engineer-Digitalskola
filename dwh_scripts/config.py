# create table
ddl_statements = {

"dim_categories" : """
create or replace TABLE DWH_DBT_PROJECT.PUBLIC.DIM_CATEGORIES (
	CATEGORYID NUMBER(38,0),
	CATEGORYNAME VARCHAR(16777216),
	DESCRIPTION VARCHAR(16777216),
	PICTURE FLOAT,
	primary key (CATEGORYID)
);
""",
"dim_employees" : """
create or replace TABLE DWH_DBT_PROJECT.PUBLIC.DIM_EMPLOYEES (
	EMPLOYEEID NUMBER(38,0),
	LASTNAME VARCHAR(16777216),
	FIRSTNAME VARCHAR(16777216),
	TITLE VARCHAR(16777216),
	TITLEOFCOURTESY VARCHAR(16777216),
	BIRTHDATE TIMESTAMP_NTZ(9),
	HIREDATE TIMESTAMP_NTZ(9),
	ADDRESS VARCHAR(16777216),
	CITY VARCHAR(16777216),
	REGION VARCHAR(16777216),
	POSTALCODE VARCHAR(16777216),
	COUNTRY VARCHAR(16777216),
	HOMEPHONE VARCHAR(16777216),
	EXTENSION NUMBER(38,0),
	PHOTO FLOAT,
	NOTES VARCHAR(16777216),
	REPORTSTO VARCHAR(16777216),
	PHOTOPATH VARCHAR(16777216),
	primary key (EMPLOYEEID)
);
""",
"dim_suppliers" : """
create or replace TABLE DWH_DBT_PROJECT.PUBLIC.DIM_SUPPLIERS (
	SUPPLIERID NUMBER(38,0),
	COMPANYNAME VARCHAR(16777216),
	CONTACTNAME VARCHAR(16777216),
	CONTACTTITLE VARCHAR(16777216),
	ADDRESS VARCHAR(16777216),
	CITY VARCHAR(16777216),
	REGION VARCHAR(16777216),
	POSTALCODE VARCHAR(16777216),
	COUNTRY VARCHAR(16777216),
	PHONE VARCHAR(16777216),
	FAX VARCHAR(16777216),
	HOMEPAGE VARCHAR(16777216),
	primary key (SUPPLIERID)
);
""",
"fact_orders" : """
create or replace TABLE DWH_DBT_PROJECT.PUBLIC.FACT_ORDERS (
	ORDERID NUMBER(38,0),
	CUSTOMERID VARCHAR(16777216),
	EMPLOYEEID NUMBER(38,0),
	ORDERDATE TIMESTAMP_NTZ(9),
	REQUIREDDATE TIMESTAMP_NTZ(9),
	SHIPPEDDATE VARCHAR(16777216),
	SHIPVIA NUMBER(38,0),
	FREIGHT NUMBER(38,2),
	SHIPNAME VARCHAR(16777216),
	SHIPADDRESS VARCHAR(16777216),
	SHIPCITY VARCHAR(16777216),
	SHIPREGION VARCHAR(16777216),
	SHIPPOSTALCODE VARCHAR(16777216),
	SHIPCOUNTRY VARCHAR(16777216),
	primary key (ORDERID),
	constraint FK_ORDERS_EMPLOYEES foreign key (EMPLOYEEID) references DWH_DBT_PROJECT.PUBLIC.DIM_EMPLOYEES(EMPLOYEEID)
);
""",
"dim_products" : """
create or replace TABLE DWH_DBT_PROJECT.PUBLIC.DIM_PRODUCTS (
	PRODUCTID NUMBER(38,0),
	PRODUCTNAME VARCHAR(16777216),
	SUPPLIERID NUMBER(38,0),
	CATEGORYID NUMBER(38,0),
	QUANTITYPERUNIT VARCHAR(16777216),
	UNITPRICE NUMBER(38,2),
	UNITSINSTOCK NUMBER(38,0),
	UNITSONORDER NUMBER(38,0),
	REORDERLEVEL NUMBER(38,0),
	DISCONTINUED NUMBER(38,0),
	constraint FK_PRODUCTS_CATEGORY foreign key (CATEGORYID) references DWH_DBT_PROJECT.PUBLIC.DIM_CATEGORIES(CATEGORYID),
	primary key (PRODUCTID),
	constraint FK_PRODUCTS_SUPPLIERS foreign key (SUPPLIERID) references DWH_DBT_PROJECT.PUBLIC.DIM_SUPPLIERS(SUPPLIERID)
);
""",
"fact_order_details" : """
create or replace TABLE DWH_DBT_PROJECT.PUBLIC.FACT_ORDER_DETAILS (
	ORDERID NUMBER(38,0),
	PRODUCTID NUMBER(38,0),
	UNITPRICE NUMBER(38,2),
	QUANTITY NUMBER(38,0),
	DISCOUNT NUMBER(38,2),
	constraint FK_OD_ORDER foreign key (ORDERID) references DWH_DBT_PROJECT.PUBLIC.FACT_ORDERS(ORDERID),
	constraint FK_OD_PRODUCTS foreign key (PRODUCTID) references DWH_DBT_PROJECT.PUBLIC.DIM_PRODUCTS(PRODUCTID)
);
"""

}


