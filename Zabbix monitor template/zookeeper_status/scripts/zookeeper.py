#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------
# @Date    : 2016-11-08 14:46:52
# @Author  : wye
# @Version : v1.0
# @Desrc   : zabbix monitor plugin for zookeeper run status
# ----------------------------------------------------

import socket
import sys

zk_host = "127.0.0.1"
zk_client_port = 2181

def GetRawData(cmd):
    """
    Access socket interface of zookeeper to get status data 
    """
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = (zk_host,zk_client_port)
        sock.connect(server_address)
        sock.sendall(cmd)
        data = sock.recv(1024)
        return data
    finally:
        sock.close()

def GetRunStatusData():
    """
    Get run status data from zookeeper  
    """
    cmd = "mntr"
    data = GetRawData(cmd)
    DataDict = {}
    for i in data.strip("\n").split("\n"):
        DataDict[i.split("\t")[0].strip()] = i.split("\t")[1].strip()
    #DataDict = {i.split("\t")[0].strip():i.split("\t")[1].strip() for i in data.strip("\n").split("\n")}
    return DataDict

def GetSelfCheckData():
    """
    Get self check status data from zookeeper
    """
    cmd = "ruok"
    data = GetRawData(cmd)
    return data.strip()

def GetStatusDataByZabbixRequest(StatusName):
    """
    Get different status data of zookeeper,according to the zabbix request.
    """
    if StatusName == "zk_self_check":
        print GetSelfCheckData()
    else:
        DataDict = GetRunStatusData()
        if DataDict.has_key(StatusName):
            try:
                StatusData = int(DataDict[StatusName])
            except ValueError:
                StatusData = DataDict[StatusName]
            print StatusData
        else:
            pass

if __name__ == "__main__":
    GetStatusDataByZabbixRequest(sys.argv[1])
