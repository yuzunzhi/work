#!/bin/bash
#Moniter Nginx Status

HOST=127.0.0.1
Nginx_status="curl http://${HOST}/ng_status 2>/dev/null"

case $1 in
	Processer)
		ps aux | grep nginx | grep -v grep | wc -l
		;;
		
	Active)
		${Nginx_status} | grep $1 | awk '{print $NF}'
		;;
		
	Reading)
		${Nginx_status} | grep $1 | awk '{print $2}'
		;;
		
	Writing)
		${Nginx_status} | grep $1 | awk '{print $4}'
		;;
		
	Accepts)
		${Nginx_status} | awk NR==3 | awk '{print $1}'
		;;
		
	Handled)
		${Nginx_status} | awk NR==3 | awk '{print $2}'
		;;
		
	Requests)
		${Nginx_status} | awk NR==3 | awk '{print $3}'
		;;

	Dropped)
		Active=`${Nginx_status} | grep $1 | awk '{print $NF}'`
		Handled=`${Nginx_status} | awk NR==3 | awk '{print $2}'`
		Dropped=`expr ${Active} - ${Handled}`
		echo ${Dropped}
		;;
		
	*)
		echo "USAGE : $0 [Processer|Active|Reading|Writing|Accepts|Handled|Requests|Dropped]"
esac
