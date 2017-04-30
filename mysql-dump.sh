#!/bin/sh
bin=/home/cjx/Desktop/elasticsearch-jdbc-2.3.4.0/bin
lib=/home/cjx/Desktop/elasticsearch-jdbc-2.3.4.0/lib


echo '{
    "type": "jdbc",
    "jdbc": {
    	"elasticsearch.autodiscover" : true,
        "url": "jdbc:mysql://127.0.0.1:3306/chttp",
        "user": "root",
	"useSSL":"true",
        "password": "root",
        "sql": "select * from ip_data where updatetime>\"2016-06-10 00:00:00\"",
        "treat_binary_as_string": true,
        "elasticsearch": {
            "host": "127.0.0.1",
            "port": 9300
        },
        "index": "chttp",
        "type": "ip_data"
}
}' | java \
-cp "${lib}/*" \
-Dlog4j.configurationFile=${bin}/log4j2.xml \
org.xbib.tools.Runner \
org.xbib.tools.JDBCImporter
