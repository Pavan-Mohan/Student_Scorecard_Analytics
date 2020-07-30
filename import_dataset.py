
import json
import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': '9200' , 'http_auth' :('elastic', 'kibana')}], timeout=30)

jsonfile= open("C:\Elastic_stack\work\students_score_card.json",'r').read()
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
        es.index(index='aut', ignore=400, body=docs[i] )
        i=i+1


