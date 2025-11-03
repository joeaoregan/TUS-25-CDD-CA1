#!/bin/bash
# Update packages
yum update -y

# install Java 17 (Amazon Corretto)
yum install -y java-17-amazon-corretto

# Create app directory
mkdir -p /opt/myapp
cd /opt/myapp

# Download the JAR from S3
wget https://mgiblins3demo.s3.us-east-1.amazonaws.com/
couponserviceh2.jar -O /opt/myapp/couponsericeh2.jar

# Run the JAR in the background so it doesn't block boot
nohup java -jar /opt/myapp/couponserviceh2.jar > /opt/myapp/
app.log 2>&1 &