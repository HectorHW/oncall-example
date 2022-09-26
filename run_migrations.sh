#!/bin/bash
#this script is used to apply migrations to database (see docker-compose.yml)
for i in 1 2 3 4 5; do mysql -u root -p1234 -h mysql < ./db/schema.v0.sql && break || sleep 5; done
