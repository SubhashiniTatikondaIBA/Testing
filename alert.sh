#!/bin/bash
count=$(ls /usr/share/tomcat/temp/ | wc -l)
instance_id=$(curl http://169.254.169.254/latest/meta-data/instance-id)
echo $count
echo $instance_id
if [ $count -gt 10 ]
then
aws sns publish --topic-arn arn:aws:sns:eu-west-1:596827047038:IBA-Devops --subject "Actionable Alert " --message "Number of files exceeds 10000 for instance id: "$instance_id 
else
echo "No need of alert"
fi
