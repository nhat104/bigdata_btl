
# Work Flow
Sau khi kết nối các máy bằng SSH thành công:
Khởi động hệ thống Hadoop File System:
Vào Terminal, lần lượt chạy các câu lệnh sau: hdfs namenode -format
						star-dfs.sh

Khởi động Spark: Sử dụng lệnh trên terminal:
	cd /opt/spark/sbin  (nơi lưu trữ thư mục sbin spark của hệ thống)
	./start-master.sh
	./start-workers.sh
	
Khởi động elasticsearch: sudo systemctl start elasticsearch

Chạy spark-submit: câu lệnh spark-submit được lưu trong runspark.sh
	Trên terminal mở với thư mục chứa runspark.sh: bash runspark.sh
	Khởi chạy spark-worker với 8 core hoạt động song song

Sau đó, khởi đọngo kibana: sudo systemctl start kibana
Các port sử dụng:
	master:9870 Hadoop home
	master:9000 namenode
	master:8088 Hadoop yarn
	master:8088 Spark master
	master:9200 Elasticsearch
	master:5601 Kibana
# Requirement:
- At least 8GB RAM on namenode, and 2 datanode.
- elasticsearch version 7.15.7
- kibana lastest version
- hadoop 3.15.1
- jdk 8
- ssh and pdsh. Hệ thống kết bằng private IP.
- pyspark
- python3
