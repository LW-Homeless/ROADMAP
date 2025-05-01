import redis
import json


class RedisWeather:

    def __init__(self):
        self.__redis_server = redis.Redis(host='192.168.50.224', port=6379,
                                          password='kdn#gkntrLB6$9', db=0, socket_timeout=2)

    def set_redis(self, key, query_weather):
        return self.__redis_server.set(key, json.dumps(query_weather), ex=86400)

    def get_redis(self, key):
        query_record = self.__redis_server.get(key)
        return query_record

    def server_state(self):
        try:
            response = self.__redis_server.ping()

            if response:
                return True

        except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError):
            return False

    def close_connection(self):
        self.__redis_server.close()