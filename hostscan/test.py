from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search,Q
client = Elasticsearch()
import json






# def search(searchtype,content):
#
#     if searchtype == 'ip':
#         s = Search().using(client).query("match", ip=content)
#     elif searchtype == 'title':
#         s = Search().using(client).query("match", title=content)
#     elif searchtype == 'port':
#         s = Search().using(client).query("match", port=content)
#     elif searchtype == 'header':
#         s = Search().using(client).query("match", header=content)
#     elif searchtype == 'appname':
#         s = Search().using(client).query("match", appname=content)
#     elif searchtype == 'ipaddrs':
#         s = Search().using(client).query("match", ipaddrs=content)
#     elif searchtype == 'domain':
#         s = Search().using(client).query("match", domain=content)
#
#     response = s.execute()
#
#     return s

def search(page='1',scontent=None, content=None):

    limitpage = 15

    searcharray = []
    if scontent is not None:
        q = Q("multi_match", query=scontent, fields=['ip', 'title', 'header',
                                                    'appname', 'ipaddrs', 'domain'])
    else:
        for key in content.keys():
            if key == 'ip':
                searcharray.append(Q('term', ip=content[key]))
            elif key == 'title':
                searcharray.append(Q('match', title=content[key]))
            elif key == 'port':
                searcharray.append(Q('term', port=content[key]))
            elif key == 'header':
                searcharray.append(Q('match', header=content[key]))
            elif key == 'appname':
                searcharray.append(Q('term', appname=content[key]))
            elif key == 'ipaddrs':
                searcharray.append(Q('match', ipaddrs=content[key]))
            if key == 'domain':
                searcharray.append(Q('match', domain=content[key]))
        print(searcharray)
        if searcharray == []:
                return []
        else:
            q = Q('bool', must=searcharray)
            # print(q)
    s = Search(index='chttp', doc_type='ip_data').using(client)
    s = s.query(q)
    s = s[int(page) * limitpage:int(page) * limitpage + limitpage]
    response = s.execute()
    count = len(response)
    print('返回的实际数量为%d' % count)
    if response.success():
        portarray = []
        count = response.hits.total
        print('返回的集中率为%d' % count)
        if count == 0:
            pagecount = 0
        elif count%limitpage> 0:
            pagecount = int((count + limitpage - 1) / limitpage)
        else:
            pagecount = count / limitpage


        if count > 0:
            for i in response:
                dic = i.to_dict()
                portarray.append(dic)
        return portarray, count, pagecount

    else:
        return None



# portarray, count, pagecount = search(scontent='辽宁')

searchdata ='辽宁'


if ':' in searchdata:
    searchdata = searchdata.split('&')
    content = {}
    for i in searchdata:
        i = i.split(':')
        content[i[0]] = i[1]
    portarray, count, pagecount = search(content=content)
else:
    portarray, count, pagecount = search(scontent=searchdata)


for i in portarray:
    print(i)


