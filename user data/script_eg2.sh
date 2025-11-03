#!/bin/bash
echo "Hello from user-data!"

sudo apt update -y
sudo apt install -y apache2
sudo chmod -R 777 /var/www/html/index.html
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
sudo apt instal mariadb-server -y
Wget
https://staticwebsiteshobeem.s3.eu-west-1.amazonaws.com/coupon/couponservice-0.0.1-SNAPSHOT.jar
sudo apt install -y java*
jara -jar couponservice-0.0.1-SNAPSHOT.jar
mysql -h database-1.cvg60cnemdlx.eu-west-1.rds.amazonaws.com -P 3306 -u root -p
