#!/bin/bash
#simple password generator

echo "Please enter the length of the password"
read pass_length

for p in $(seq 1);
do 
 openssl rand -base64 48 | cut -c1-$pass_length
done



