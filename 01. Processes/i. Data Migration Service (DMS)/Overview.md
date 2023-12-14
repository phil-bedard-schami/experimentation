# Data Migration Service (DMS)

[AWS Database Migration Service (DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) is a tool provided by Amazon Web Services that simplifies the process of moving databases to the cloud. Imagine you have a database running on your own servers, and you want to shift it to AWS. DMS helps with this transition, ensuring a smooth and secure move. It supports various types of databases, like MySQL, PostgreSQL, Oracle, and SQL Server.

DMS allows for different scenarios: moving databases of the same type (homogeneous) or even changing the type of database (heterogeneous). It can continuously replicate data, making sure your new AWS database stays up-to-date in real-time leveraging Change Data Capture (CDC). During migration, DMS can adjust the data to fit the new database structure, minimizing any disruptions to your applications. It's built with security in mind, encrypting data during the transfer and allowing you to control access using AWS security features. The service also provides monitoring tools, helping you keep an eye on the migration progress. Overall, AWS DMS is a user-friendly solution for businesses looking to seamlessly migrate their databases to the AWS cloud.

## Change Data Capture (CDC)

In AWS, [Change Data Capture (CDC)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) is a technique used to identify and capture changes made to a database, such as inserts, updates, and deletes. It is particularly useful for real-time data replication, data warehousing, and maintaining synchronized data across different systems. AWS provides services like AWS Database Migration Service (DMS) and AWS Glue that support Change Data Capture, allowing you to replicate data between various data sources and targets while tracking changes.*

In more simple terms, imagine you have a large database containing lots of information, such as customer details, product inventory, or financial transactions. In real-life applications, this data is constantly changing: new customers are signing up, products are being added or updated, and transactions are taking place.

Change Data Capture is like having a smart system in place that keeps track of all these changes automatically. It monitors the database closely and notes down every little change that happens, whether it's a new entry, an update to existing information, or the removal of data. This eliminates the need to do a full refresh of the data on a scheduled basis as it logs the updates in real-time.

# Pulsar Use Case

``` mermaid
%% GRAPH DESIGN
graph LR

source <-- DMS / CDC -->target -->raw

%% COMPONENTS
source[(Oracle)]
target[(PostgreSQL)]
raw[(S3 Raw)]

%% STYLING
style source fill:#ED1B24
style target fill:#2D72B8
style raw fill:#E05243

```

The data captured from radio frequency (RF) towers and stations is stored in an Oracle database. It's important to note that the data leveraged in the reports are not pointing directly to the source database. The data is first migrated to an Aurora PostgreSQL by leveraging AWS Data Migration Service (DMS) capabilities to then be cleaned/curated and stored in an AWS Redshift Data warehouse.

In order to make sure the data leveraged in reports is consistent with the data from the originating source we need to setup a DMS with CDC support. The DMS will help migrate the data over to our Aurora PostgreSQL with an initial full load of the data. CDC will then continuously make sure the data is consistent between both platforms by replicating the changes accordingly with an ongoing replication.

The advantage of leveraging CDC and an ongoing replication is that there is no need to migrate all of the data on a scheduled basis. You can migrate the bulk of the data once and then insert, delete or update rows when the system notices a change. Ongoing replication allows for much faster processing when it comes to data migration/replication and avoids the need for full data loads on a scheduled basis. Since the data is almost always up to date this removes the need for inserting timestamps in the data to understand when the data was migrated over as it now no longer relies on the one overnight full load.

Right now in DEV1 all of the data (millions of rows) get migrated over to the data source leverage by the reports every morning at 7AM. This is a waste of processing power and resources. Ongoing replication and leveraging the CDC eliminates the redundancy of needing to migrate the entire data every day.