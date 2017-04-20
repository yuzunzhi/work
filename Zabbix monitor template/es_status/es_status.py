#!/usr/bin/env python
# -*- coding: utf-8 -*-

import elasticsearch
import sys

es_host = '10.19.64.72'
#es_host = '127.0.0.1'
es_port = '9200'

conn = elasticsearch.Elasticsearch(es_host + ':' + es_port, sniff_on_start=False)


def cluster_status():
    status = conn.cluster.health()["status"]
    if status == "green":
        returnval = 0
    elif status == "yellow":
        returnval = 1
    elif status == "red":
        returnval = 2
    return returnval

def service_status():
    status = conn.ping()
    if status:
        returnval = 1
    else:
        returnval = 0
    return returnval

def fail():
    print """This script is not supported.
Usage : %s [cluster_status|service_status]""" % sys.argv[0]
    sys.exit(2)

if len(sys.argv) != 2:
    fail()

if sys.argv[1] == "cluster_status":
    print cluster_status()
elif sys.argv[1] == "service_status":
    print service_status()

