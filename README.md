# Recommended_system_project
	1.环境：Hadoop、Hive、Spark、Hbase、Redis
	2.技术栈：Python、Flume、Kafka、SparkStreaming、SparkSql


离线部分：完成用户画像和文章画像
在线部分：在线召回以及召回读取，经过LR排序模型后将推荐数据存储在Redis缓存中
推荐服务中心：通关Grpc，相应客户端请求，根据参数返回对应的推荐结果
