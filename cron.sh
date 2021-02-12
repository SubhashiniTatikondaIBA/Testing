#!/bin/bash
crontab<<EOF
$(crontab -l)
0 6 * * * find /usr/share/tomcat/temp/ -type f -mtime +14 -exec rm -f {} \;
*/10 * * * * /usr/share/tomcat/temp/alert.sh
EOF
