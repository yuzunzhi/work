# ------------------------------
# �汾˵��
# -------------------------------
// V1.0 in 20161106
// ��activemqȫ�ֺ͵���queue�Ĺؼ�ָ����,���Զ����ּ����queue�����м�ء�

# ------------------------------
# ʹ������
# ------------------------------
// activemq�汾�����5.8.0
// activemq�迪������̨��Ĭ���ǿ����ģ���˿�Ĭ����8161.

# ------------------------------
# Zabbix֮activemq��ز��ʹ�÷���
# -------------------------------

(1)��zabbix web����̨����ģ���ļ�zbx_activemq.status_templates.xml

(2)��zabbix web����̨���activemq������Ϊ������յ����ģ��activemq_status

(3)��activemq������װzabbix agent

(4)��activemq�����£���activemq.conf�ļ�����/etc/zabbix/zabbix_agentd.conf.d/

(5)��activemq�����£���activemq.py�ļ�����/etc/zabbix/scripts/,��Ϊ����Ͽ�ִ��Ȩ�ޡ�

(6)��activemq.py�ҵ����´���Σ��޸Ĳ�����һ��ֻ���޸��������ɡ�

ActivemqHost="127.0.0.1"                   # Activemq instance IP Address
ActivemqConPort="8161"                     # Activemq console port
ActivemqApiPrefix="/api/jolokia/read/"     # Activemq REST API Prefix String
ActivemqBrokerName="localhost"             # Activemq broker name
ActivemqAdminUser="admin"                  # Activemq console administrator
ActivemqAdminPasswd="admin"                # Activemq console administrator password

(7)��activemq�����£�����zabbix agent

--------------
wye in 20161106


