#! /usr/local/bin/env python3
from netapp_ontap import config
from netapp_ontap import HostConnection
from netapp_ontap.resources import Cluster
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
conn = HostConnection("192.168.0.102", username = "admin", password = "Netapp1!", verify = False)
config.CONNECTION = conn  
clus = Cluster()
clus.get()
print (clus.version)
print(clus)