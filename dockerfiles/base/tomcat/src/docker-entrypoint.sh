#!/bin/bash
set -e

case ${1} in
    debug | jpda | run | start | configtest)
        set -- catalina.sh "$@"
        AppIp=${AppAddress%:*}
        AppPort=${AppAddress#*:}
        [ -z "${AppId}" ] && AppId=${AppLabel}_${AppAddress}
        [ -z "${JmxIp}" ] && JmxIp=${AppIp}
        [ -n "${JmxIp}" ] && [ -n "${JmxPort}" ] && CATALINA_OPTS="${CATALINA_OPTS} -Djava.rmi.server.hostname=${JmxIp} -Dcom.sun.management.jmxremote.port=${JmxPort} -Dcom.sun.management.jmxremote.rmi.port=${JmxPort} -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"
        ;;
    stop | version) set -- catalina.sh "$@";;
    # *) set -- "/bin/bash"
esac

export AppId AppLabel AppAddress CATALINA_OPTS

exec "$@"
