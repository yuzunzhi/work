#!/bin/bash

HOST="10.19.64.69"
#HOST="127.0.0.1"
PORT=6379
CACHETTL=30
CACHE=/tmp/redis-status.cache
METRIC=$1

if [ -s "$CACHE" ]; then
    CACHE_CTIME=`stat -c"%Z" $CACHE`
else
    CACHE_CTIME=0
fi

TIMENOW=`date +%s`

if [ $(( $TIMENOW - $CACHE_CTIME )) -gt $CACHETTL ]; then
    /opt/platform/redis/redis-cli -h $HOST -p $PORT info > $CACHE
fi

case $METRIC in
    status )
	/opt/platform/redis/redis-cli -h $HOST -p $PORT ping | grep -c PONG
	;;
    redis_version )
	cat $CACHE | grep "redis_version:" | cut -d':' -f2
	;;
    redis_mode )
	cat $CACHE | grep "redis_mode:" | cut -d':' -f2
        ;;
    uptime_in_seconds )
	cat $CACHE | grep "uptime_in_seconds:" | cut -d':' -f2
        ;;
    used_memory_rss )
	cat $CACHE | grep "used_memory_rss:" | cut -d':' -f2
        ;;
    used_memory_persent )
	Used_memory=$(cat $CACHE | grep "used_memory_rss:" | cut -d':' -f2 | sed ""s/\\r//"")
	Total_memory=$(cat $CACHE | grep "total_system_memory:" | cut -d':' -f2 | sed ""s/\\r//"")
	echo "scale=4; ${Used_memory} / ${Total_memory};" | bc | awk '{printf "%.4f", $0}'
	;;
    total_system_memory )
	cat $CACHE | grep "total_system_memory:" | cut -d':' -f2
        ;;
    connected_clients )
	cat $CACHE | grep "connected_clients:" | cut -d':' -f2
        ;;

    * )
	echo "Not selected metric."
	exit 0
	;;
esac
