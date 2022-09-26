#!/bin/bash
#this script is used to apply migrations to database (see docker-compose.yml)
mysql -u root -p1234 -h mysql < ./db/schema.v0.sql
