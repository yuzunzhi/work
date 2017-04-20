#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import commands
import sys


# 输出logstash进程数据,输出格式为zabbix的low level discover要求的数据格式
def LogstashDiscover():
    List = []
    Dict = {}
    output = commands.getoutput(
        "ps auxww | grep -w logstash | grep -v grep | grep -v python | awk -F'/' '{print $NF}' | awk -F'.' '{print $1}'")

    for name in output.split():
        List.append({"{#LOGSTASHNAME}": name})

    Dict["data"] = List
    print json.dumps(Dict)


# 获取指定logstash的进程数，正常为1
def LogstashProcessCheck(logstashname):
    returnval = commands.getoutput("ps auxww | grep -w %s | grep -v grep | grep -v python | wc -l" % logstashname)
    print returnval


# 获取指定logstash物理内存使用量
def UsedMemory(logstashname):
    returnval = commands.getoutput(
        "ps auxww | grep -w %s | grep -v grep | grep -v python | awk '{print $6}'" % logstashname)
    print returnval


# 错误函数
def fail():
    print "Usage : %s [discover|usedmemory|status [logstashname]]" % sys.argv[0]
    sys.exit(1)


# 脚本执行逻辑
try:
    if sys.argv[1] == "discover":
        LogstashDiscover()
    elif sys.argv[1] == "status":
        LogstashProcessCheck(sys.argv[2])
    elif sys.argv[1] == "usedmemory":
        UsedMemory(sys.argv[2])
    else:
        print "Error function %s" % sys.argv[1]
        print "Usage : %s [discover|usedmemory|status [logstashname]]" % sys.argv[0]
except:
    fail()
