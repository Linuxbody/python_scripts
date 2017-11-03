# coding=utf-8
# Email: ccg0428@163.com
__author__ = "victor"
__date__ = '2017-11-02 17:35'

import redis

connect = redis.ConnectionPool(host='10.0.0.196', port=6379, decode_responses=True)

r = redis.Redis(connection_pool=connect)

info = r.info()

RedisInfo = {}

version = info['redis_version']
run_days = info['uptime_in_days']
con_clients = info['connected_clients']
used_memory = info['used_memory_human']
max_memory = info['used_memory_peak_human']
hits= info['keyspace_hits']
miss = info['keyspace_misses']
role = info['role']
key_nums = info['db0']['keys']

"""
可以把上面的值放进字典
如以此添加：
    RedisInfo['version'] = version
    RedisInfo['run_days'] = run_days

"""
print("版本:", version)
print("运行天数:",run_days)
print("链接数:",con_clients)
print("使用内存:",used_memory)
print("峰值内存:",max_memory)
print("命中次数:",hits)
print("丢失次数:",miss)
print("角色:",role)
print("db0数据库key数:",key_nums)


