import redis
import sys
sys.path.append("../../..")
from config.config import Config
conf = Config()
configs = conf.getConfig()
class BjjsRedis:
    def __init__(self):
        self.conn = redis.Redis(host=configs.REDIS['host'], port=configs.REDIS['port'], db=0,password=configs.REDIS['pass'])

    def save(self,key,val,ex=None):
        self.conn.set(key,val,ex)

    def get(self,key):
        return self.conn.get(key)


if __name__ == '__main__':
    rr = BjjsRedis()
    rr.save("test","test1")

    print rr.get("test")

    if(rr.get("test")):
        print "exist"
    else:
        print "not exist"