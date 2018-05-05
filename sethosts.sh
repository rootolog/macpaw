#!/bin/bash
container_ip=`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' macpaw`
echo "$container_ip internship.macpaw.io" >> /etc/hosts
