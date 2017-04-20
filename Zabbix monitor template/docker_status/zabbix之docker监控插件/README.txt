# ------------------------------
# 版本说明
# ------------------------------
// V1.0 in 20170221
// 对docker基础指标进行监控

# ------------------------------
# 插件使用方法
# ------------------------------
(1)在docker主机,安装cadvisor,如下所示：

sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  172.30.33.88:5000/quark/cadvisor:v1 \
  --http_auth_file /usr/bin/htpasswd --http_auth_realm cadvisor
  
(2)在docker主机下，将DockerStats.conf文件放入/etc/zabbix/zabbix_agentd.conf.d/
(3)在docker主机下，将DockerStats.py文件放入/etc/zabbix/scripts/,并为其加上可执行权限
(4)在DockerStats.py找到如下代码段，修改参数。一般默认即可。

CadvisorHost="127.0.0.1"
CadvisorPort=8080

DockerHost="127.0.0.1"
DockerPort=2375

(5)在docker主机下，重启zabbix-agent。
(6)在zabbix web控制台导入模板文件zbx_docker.status_templates.xml
(7)在zabbix web控制台添加docker主机并为其引入刚导入的模板docker_status

# ------------------------------
# docker监控指标说明
# ------------------------------
相关指标和报警阈值请在导入模板后查看

--------------
wye in 20170221
