import redis
import sys
sys.path.append("../../..")
from bin.python.config.config import configs
class RedisResults:
    def __init__(self):
        self.conn = redis.Redis(host=configs['redis']['host'], port=configs['redis']['port'], db=0,password=configs['redis']['pass'])
    def save(self,hash,result):
        self.conn.set(hash,result,3600*24*14)

    def get(self,hash):
        return self.conn.get(hash)


if __name__ == '__main__':
    rr = RedisResults()
    rr.save("hash","value")

    print rr.get("hash")

    if(rr.get("test")):
        print "exist"
    else:
        print "not exist"