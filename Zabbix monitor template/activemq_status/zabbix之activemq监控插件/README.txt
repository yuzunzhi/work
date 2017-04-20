# ------------------------------
# 版本说明
# -------------------------------
// V1.0 in 20161106
// 对activemq全局和单个queue的关键指标监控,可自动发现加入的queue并进行监控。

# ------------------------------
# 使用条件
# ------------------------------
// activemq版本需大于5.8.0
// activemq需开启控制台，默认是开启的，其端口默认是8161.

# ------------------------------
# Zabbix之activemq监控插件使用方法
# -------------------------------

(1)在zabbix web控制台导入模板文件zbx_activemq.status_templates.xml

(2)在zabbix web控制台添加activemq主机并为其引入刚导入的模板activemq_status

(3)在activemq主机安装zabbix agent

(4)在activemq主机下，将activemq.conf文件放入/etc/zabbix/zabbix_agentd.conf.d/

(5)在activemq主机下，将activemq.py文件放入/etc/zabbix/scripts/,并为其加上可执行权限。

(6)在activemq.py找到如下代码段，修改参数。一般只需修改最后两项即可。

ActivemqHost="127.0.0.1"                   # Activemq instance IP Address
ActivemqConPort="8161"                     # Activemq console port
ActivemqApiPrefix="/api/jolokia/read/"     # Activemq REST API Prefix String
ActivemqBrokerName="localhost"             # Activemq broker name
ActivemqAdminUser="admin"                  # Activemq console administrator
ActivemqAdminPasswd="admin"                # Activemq console administrator password

(7)在activemq主机下，重启zabbix agent

--------------
wye in 20161106


