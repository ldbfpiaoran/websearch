from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search,Q
client = Elasticsearch()







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

def search(page='0',scontent=None, dic=None):

    limitpage = 15

    searcharray = []
    if scontent is not None:
        q = Q("multi_match", query=scontent, fields=['ip', 'title', 'header',
                                                    'appname', 'ipaddrs', 'domain'])
    else:
        for key in dic.keys():
            if key == 'ip':
                searcharray.append(Q('term', ip=dic[key]))
            elif key == 'title':
                searcharray.append(Q('match', title=dic[key]))
            elif key == 'port':
                searcharray.append(Q('term', port=dic[key]))
            elif key == 'header':
                searcharray.append(Q('match', header=dic[key]))
            elif key == 'appname':
                searcharray.append(Q('term', appname=dic[key]))
            elif key == 'ipaddrs':
                searcharray.append(Q('match', ipaddrs=dic[key]))
            if key == 'domain':
                searcharray.append(Q('match', domain=dic[key]))

        if searcharray == []:
            return []
        else:
            q = Q('bool', must=searcharray)
    print(q)
    s = Search(index='chttp', doc_type='ip_data').using(client)
    s = s.query(q)
    s = s[int(page) * limitpage:int(page) * limitpage + limitpage]
    response = s.execute()

    # print('返回的实际数量为%d' % count)
    if response.success():
        portarray = []
        count = response.hits.total
        # print('返回的集中率为%d' % count)
        if count == 0:
            pagecount = 0
        elif count%limitpage> 0:
            pagecount = int((count + limitpage - 1) / limitpage)
        else:
            pagecount = count / limitpage

        count = len(response)
        if count > 0:
            for i in response:
                dic = i.to_dict()
                portarray.append(dic)
        return portarray, count, pagecount



