import json
import pprint
from elasticsearch import Elasticsearch
username = input("Enter elsatic search username: ")
password = input ("Enter elastic search password: ")
path_to_file = input("enter the path of jsonfile: ")
indexname =input("enter the index name: ")

es = Elasticsearch([{'host': 'localhost', 'port': '9200' , 'http_auth' :(username, password)}], timeout=30)

jsonfile= open(path_to_file,'r').read()
ClearData = jsonfile.splitlines(True)
i=0
json_str=""
docs ={}
for line in ClearData:
    line = ''.join(line.split())
    if line != "},":
        json_str = json_str+line
    else:
        docs[i]=json_str+"}"
        json_str=""
        print(docs[i])
        es.index(index=indexname, ignore=400, body=docs[i])
        i=i+1


