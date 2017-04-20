#!/bin/bash
#zabbix web monitor

Web_monitor(){
	curl -Is --connect-timeout 2 $1 | head -1 | grep 200 | wc -l
}

Web_url="http://$1"

Web_monitor $Web_url
