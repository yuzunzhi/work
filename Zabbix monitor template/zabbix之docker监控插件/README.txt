# ------------------------------
# �汾˵��
# ------------------------------
// V1.0 in 20170221
// ��docker����ָ����м��

# ------------------------------
# ���ʹ�÷���
# ------------------------------
(1)��docker����,��װcadvisor,������ʾ��

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
  
(2)��docker�����£���DockerStats.conf�ļ�����/etc/zabbix/zabbix_agentd.conf.d/
(3)��docker�����£���DockerStats.py�ļ�����/etc/zabbix/scripts/,��Ϊ����Ͽ�ִ��Ȩ��
(4)��DockerStats.py�ҵ����´���Σ��޸Ĳ�����һ��Ĭ�ϼ��ɡ�

CadvisorHost="127.0.0.1"
CadvisorPort=8080

DockerHost="127.0.0.1"
DockerPort=2375

(5)��docker�����£�����zabbix-agent��
(6)��zabbix web����̨����ģ���ļ�zbx_docker.status_templates.xml
(7)��zabbix web����̨���docker������Ϊ������յ����ģ��docker_status

# ------------------------------
# docker���ָ��˵��
# ------------------------------
���ָ��ͱ�����ֵ���ڵ���ģ���鿴

--------------
wye in 20170221
