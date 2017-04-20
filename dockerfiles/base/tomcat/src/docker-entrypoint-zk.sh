#!/bin/bash
set -e


case ${1} in
    debug | jpda | run | start | configtest)
        set -- catalina.sh "$@"
        AppIp=${AppAddress%:*}
        AppPort=${AppAddress#*:}
        [ -z "${AppId}" ] && AppId=${AppLabel}_${AppAddress}
        [ -z "${InstanceId}" ] && InstanceId=${AppLabel}
        [ -n "${AppCfgs}" ] && [ -z "${InstanceId}" ] && echo 'InstanceId and AppLabel can not be nil.' 1>&2 && exit 1
        for AppCfg in `echo ${AppCfgs} | sed 's/,/ /g'`
        do
            echo "zkGet.py ${ZookeeperCluster} /instances/${InstanceId}/${AppCfg} ..."
            mkdir -p `dirname "${CATALINA_HOME}/${AppCfg}"`
            zkGet.py "${ZookeeperCluster}" "/instances/${InstanceId}/${AppCfg}" "${CATALINA_HOME}/${AppCfg}"
            [ $? -ne 0 ] && echo "zkGet.py ${ZookeeperCluster} /instances/${InstanceId}/${AppCfg} failure!" 1>&2 && exit 1
            echo "zkGet.py ${ZookeeperCluster} /instances/${InstanceId}/${AppCfg} success!"
        done
        [ -z "${JmxIp}" ] && JmxIp=${AppIp}
        [ -n "${JmxIp}" ] && [ -n "${JmxPort}" ] && CATALINA_OPTS="${CATALINA_OPTS} -Djava.rmi.server.hostname=${JmxIp} -Dcom.sun.management.jmxremote.port=${JmxPort} -Dcom.sun.management.jmxremote.rmi.port=${JmxPort} -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"
        ;;
    stop | version) set -- catalina.sh "$@";;
    # *) set -- "/bin/bash"
esac

export AppId AppLabel AppAddress CATALINA_OPTS

exec "$@"
