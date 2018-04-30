# OKerberos
A complete set of services to show a simplified example of how Oauth Authentication
is provided

# Requirements

 - setuptools


    pip3 install setuptools



# Installation
 To install dependencies and run scripts

    sudo python3 setup.py install
   # Development
   To see on going changes after installation run:


    sudo python3 setup.py develop

## Create Required Database

    CREATE DATABASE my_oauth2_db;

Update Database with schema and seed with one authorized user

    mysql -u root -p my_oauth2_db < db.sql 

# Services

 - Client
 - Oauth Server
 - Authentication Server
 - App Server

## Running Client


    okerberos client


## Running App Server

## Running Authentication Server


    okerberos authserver
