#!/bin/bash
#Tcp status monitor

state=$1

metric(){
	output=`/bin/netstat -an|awk '/^tcp/{++S[$NF]}END{for(a in S) print a,S[a]}' | grep -w "$1" | awk '{print $2}'`

	if [ "$output" == "" ];
	then
        echo 0
	else
        echo $output
	fi
}

case $state in
   CLOSED)
		metric $state
        ;;
   LISTEN)
		metric $state
        ;;
   SYN-RECV)
		metric $state
        ;;
   SYN-SENT)
		metric $state
        ;;
   ESTABLISHED)
		metric $state
        ;;
   TIME-WAIT)
		metric $state
        ;;
   CLOSING)
		metric $state
        ;;
   CLOSE-WAIT)
		metric $state
        ;;
   LAST-ACK)
		metric $state
         ;;
   FIN-WAIT-1)
		metric $state
         ;;
   FIN-WAIT-2)
		metric $state
         ;;
         *)
          echo "USAGE : $0 [CLOSED|LISTEN|SYN-RECV|SYN-SENT|ESTABLISHED|TIME-WAIT|CLOSING|CLOSE-WAIT|LAST-ACK|FIN-WAIT-1|FIN-WAIT-2]"   
esac