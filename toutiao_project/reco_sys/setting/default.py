from collections import namedtuple


class DefaultConfig(object):
    """离线在线的一些配置
    """
    SPARK_ONLINE_CONFIG = (
        ("spark.app.name", "onlineUpdate"),  # 设置启动的spark的app名称，没有提供，将随机产生一个名称
        # ("spark.master", "yarn"),
        ("spark.master", "local"),
        ("spark.executor.instances", 4)
    )

    # kafka的IP和端口配置
    KAFKA_SERVER = "192.168.19.137:9092"

    # redis的IP和端口配置
    REDIS_HOST = "192.168.19.137"
    REDIS_PORT = 6379

    # 配置grpc开启的服务IP和端口
    RPC_SERVER = "192.168.19.137:9999"

    # SPARK grpc配置
    SPARK_GRPC_CONFIG = (
        ("spark.app.name", "grpcSort"),  # 设置启动的spark的app名称，没有提供，将随机产生一个名称
        ("spark.master", "yarn"),
        ("spark.executor.instances", 4)
    )


CHANNEL_INFO = {
            1: "html",
            2: "开发者资讯",
            3: "ios",
            4: "c++",
            5: "android",
            6: "css",
            7: "数据库",
            8: "区块链",
            9: "go",
            10: "产品",
            11: "后端",
            12: "linux",
            13: "人工智能",
            14: "php",
            15: "javascript",
            16: "架构",
            17: "前端",
            18: "python",
            19: "java",
            20: "算法",
            21: "面试",
            22: "科技动态",
            23: "js",
            24: "设计",
            25: "数码产品",
        }


from collections import namedtuple

# abtest参数信息
# ABTest参数
param = namedtuple('RecommendAlgorithm', ['COMBINE',
                                          'RECALL',
                                          'SORT',
                                          'CHANNEL',
                                          'BYPASS']
                   )

RAParam = param(
    COMBINE={
        'Algo-1': (1, [100, 101, 102, 103, 104], [200]),  # 首页推荐，所有召回结果读取+LR排序
        'Algo-2': (2, [100, 101, 102, 103, 104], [200])  # 首页推荐，所有召回结果读取 排序
    },
    RECALL={
        100: ('cb_recall', 'als'),  # 离线模型ALS召回，recall:user:1115629498121 column=als:18
        101: ('cb_recall', 'content'),  # 离线word2vec的画像内容召回 'recall:user:5', 'content:1'
        102: ('cb_recall', 'online'),  # 在线word2vec的画像召回 'recall:user:1', 'online:1'
        103: 'new_article',  # 新文章召回 redis当中    ch:18:new
        104: 'popular_article',  # 基于用户协同召回结果 ch:18:hot
        105: ('article_similar', 'similar')  # 文章相似推荐结果 '1' 'similar:2'
    },
    SORT={
        200: 'LR',
    },
    CHANNEL=25,
    BYPASS=[
            {
                "Bucket": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd'],
                "Strategy": "Algo-1"
            },
            {
                "BeginBucket": ['e', 'f'],
                "Strategy": "Algo-2"
            }
        ]
)
