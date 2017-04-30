#!/bin/sh
bin=/home/cjx/Desktop/elasticsearch-jdbc-2.3.4.0/bin
lib=/home/cjx/Desktop/elasticsearch-jdbc-2.3.4.0/lib


echo '{
    "type" : "jdbc",
    "statefile" : "statefile.json",
   "jdbc": {
        "url" : "jdbc:mysql://127.0.0.1/chttp",
        "user" : "root",
	"useSSL":"true",
        "password" : "root",
        "index" : "chttp",
        "type": "ip_data",
        "schedule" : "0 * * * * ?",
        "metrics" : {
            "enabled" : true
        },
        
       "sql" : [
            {
                "statement" : "select * from ip_data where updatetime > ?",
                "parameter" : [ "$metrics.lastexecutionstart" ]
            }
        ]
      
    }
}' | java \
       -cp "${lib}/*" \
       -Dlog4j.configurationFile=${bin}/log4j2.xml \
       org.xbib.tools.Runner \
       org.xbib.tools.JDBCImporter

