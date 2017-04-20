#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------
# Purpose:
#    Zabbix plugin for activemq
# ----------------------------------------------------
# @Date    : 2016-11-04 14:17:22
# @Author  : wye  
# @Version : v1.0 
# @DESRC   : activemq global status and queue status 
#          + for monitor
# ----------------------------------------------------

#------------------------------
# Activemq instance parameter
#------------------------------

ActivemqHost="127.0.0.1"                   # Activemq instance IP Address
ActivemqConPort="8161"                     # Activemq console port
ActivemqApiPrefix="/api/jolokia/read/"     # Activemq REST API String
ActivemqBrokerName="localhost"             # Activemq broker name

ActivemqAdminUser="admin"                  # Activemq console administrator
ActivemqAdminPasswd="admin"                # Activemq console administrator password

#ActivemqZabbixPluginLogPath="/var/log/activemq.log"

import os
import sys
import json
import urllib2


def CallApiGetJsonData(ActivemqApiSuffix):
    """
    Call activemq api interface get json data of activemq run data
    """

    url = "http://" + ActivemqHost + ":" + ActivemqConPort +  ActivemqApiPrefix + ActivemqApiSuffix
    username = ActivemqAdminUser
    password = ActivemqAdminPasswd
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None,url,username,password)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    JsonStr = urllib2.urlopen(url).read()

    try: 
        import usjon
    except ImportError:
        RunDataDict = json.loads(JsonStr)
    else:
        RunDataDict = ujson.decode(JsonStr)

    return RunDataDict


class ExecFunByZabbixRequest(object):
    """
    Execute different functions based on zabbix request
    """

    def __init__(self,ParasList):
        try:
            FunObj = getattr(self,ParasList[0])
        except AttributeError:
            print "Without this function of %s"%(ParasList[0])
        else:
            FunObj(ParasList[1:])


    def ActivemqQueuesDiscovery(self,ParasList):
        """
        Returns all queues name in the activemq instance
        """
        TmpDict = {}
        TmpList = []

        ActivemqApiSuffix = "org.apache.activemq:type=Broker,brokerName=%s"%(ActivemqBrokerName)
        RunDataDict = CallApiGetJsonData(ActivemqApiSuffix)
        QueuesObjList =  RunDataDict["value"]["Queues"]
        QueuesList = [ i['objectName'].split(",")[1].split("=")[1] for i in QueuesObjList]

        for queuename in QueuesList:
            #TmpList.append({"{#QUEUENAME}":unicode.encode(queuename)})
            TmpList.append({"{#QUEUENAME}":queuename})
        TmpDict["data"] = TmpList
       
        try:
            import ujson
        except ImportError:
            print json.dumps(TmpDict) 
        else:
            print ujson.encode(TmpDict)

    
    def ActivemqQueueSstatus(self,ParasList):
        """
        Return activemq queue status value , 
        Queue has the following status needs to be monitored.
        #######
        QueueSize : Number Of Pending Messages
        EnqueueCount : Messages Enqueued 
        DequeueCount : Messages Dequeued
        ProducerCount : Number of Producers
        ConsumerCount : Number Of Consumers
        #######
        """

        QueueName = ParasList[0]
        StatusName = ParasList[1]

        ActivemqApiSuffix = "org.apache.activemq:brokerName=%s,destinationName=%s,destinationType=Queue,type=Broker"%(ActivemqBrokerName,QueueName)
        RunDataDict = CallApiGetJsonData(ActivemqApiSuffix)
        StatusValue = RunDataDict["value"][StatusName]

        print int(StatusValue)


    def ActivemqStatus(self,ParasList):
        """
        Return activemq global status value,
        Activemq has the following status needs to be monitored.
        ######
        StorePercentUsage
        MemoryPercentUsage
        TempPercentUsage
        TotalDequeueCount
        TotalEnqueueCount
        TotalProducerCount
        TotalConsumerCount
        CurrentConnectionsCount
        -MinMessageSize
        -MaxMessageSize
        AverageMessageSize
        #######
        """
        
        StatusName = ParasList[0]
        ActivemqApiSuffix = "org.apache.activemq:type=Broker,brokerName=%s"%(ActivemqBrokerName)
        RunDataDict = CallApiGetJsonData(ActivemqApiSuffix)
        StatusValue = RunDataDict["value"][StatusName]

        print int(StatusValue)

          
if __name__ == "__main__":
    
    ExecFunByZabbixRequest(sys.argv[1:])



