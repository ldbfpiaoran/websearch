#!/bin/sh
bin=/home/cjx/Desktop/elasticsearch-jdbc-2.3.4.0/bin
lib=/home/cjx/Desktop/elasticsearch-jdbc-2.3.4.0/lib


echo '{
"type" : "jdbc",
"jdbc": {
"elasticsearch.autodiscover":true,
"elasticsearch.cluster":"my-application",
"url":"jdbc:mysql://10.8.5.101:3306/chttp",
"user":"root",
"password":"123456",
"metrics": {
            "enabled" : true
        },
"sql":"select * from cc where updatetime>\"2016-06-10 00:00:00\"",

"elasticsearch" : {
  "host" : "127.0.0.1",
  "port" : 9300
},
"index" : "chttp",
"type" : "ip_data ",

}
}'| java \
  -cp "${lib}/*" \
  -Dlog4j.configurationFile=${bin}/log4j2.xml \
  org.xbib.tools.Runner \
  org.xbib.tools.JDBCImporter