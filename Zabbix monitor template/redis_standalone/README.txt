/etc/hosts文件内需要添加内网IP和hostname的解析记录
需要安装bc做浮点运算,yum install -y bc

此redis为standalone模式，且仅用于ELK的消息队列
所以监控项较少

目前监控项如下
#status					redis存活状态
#redis_version			redis版本
#redis_mode				redis模式
#uptime_in_seconds		redis运行时长（秒）
#used_memory_rss		redis使用的系统内存
#used_memory_persent	redis使用的系统内存百分比
#connected_clients		redis客户端连接数
