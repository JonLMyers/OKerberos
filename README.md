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

## Add PHP oauth Server

copy the root contents of oauth_provider to /var/www/html

  cp oauth_provider/* /var/www/html

Test connection with

  curl -u testclient:testpass http://localhost/token.php -d 'grant_type=client_credentials'
  {"access_token":"03807cb390319329bdf6c777d4dfae9c0d3b3c35","expires_in":3600,"token_type":"bearer","scope":null}

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
