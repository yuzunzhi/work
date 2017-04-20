#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import commands


# 开始函数
def start(self):
    try:
        func = getattr(logstash_status(), sys.argv[1])
        # 判断logstash_status()中是否有sys.argv[1]的方法，如果有就初始化func实例
    except:
        print "Error function %s" % sys.argv[1]
        fail()
    else:
        func(sys.argv[2])
        # 如果成功，将sys.argv[2]参数传给func实例


# 错误函数
def fail():
    print "Usage : %s [discover|usedmemory|status [logstashname]]" % sys.argv[0]
    sys.exit(1)


class logstash_status(object):
    # 输出logstash进程数据,输出格式为zabbix的low level discover要求的数据格式
    def discover(self, a):
        List = []
        Dict = {}
        output = commands.getoutput(
            "ps auxww | grep -w logstash | grep -v grep | grep -v python | awk -F'/' '{print $NF}' | awk -F'.' '{print $1}'")

        for name in output.split():
            List.append({"{#LOGSTASHNAME}": name})

        Dict["data"] = List
        print json.dumps(Dict)

    # 获取指定logstash的进程数，正常为1
    def status(self, a):
        try:
            returnval = commands.getoutput("ps auxww | grep -w %s | grep -v grep | grep -v python | wc -l" % a[0])
            print returnval
        except:
            fail()

    # 获取指定logstash物理内存使用量
    def usedmemory(self, a):
        try:
            returnval = commands.getoutput(
                "ps auxww | grep -w %s | grep -v grep | grep -v python | awk '{print $6}'" % a[0])
            print returnval
        except:
            fail()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        fail()
    else:
        start(sys.argv[1:])
