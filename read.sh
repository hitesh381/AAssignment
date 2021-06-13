#!/bin/bash

MachineIP=`curl http://169.254.169.254/latest/meta-data/local-ipv4`

werd="pam_unix(sshd:session): session opened"
var=""
while [ "${var}" == "" ]
do
var=$(tail -1 /var/log/secure | grep "${werd}") && echo "Script read.sh was executed" >> logFile;
done
echo "${var}" && counts=`cat logFile | wc -l` && curl -i -H "Content-Type: application/json" -X PUT -d "{\"m-location\":\"$MachineIP had "$counts" attempt(s)\"}" http://10.14.24.69:8082/v1;
