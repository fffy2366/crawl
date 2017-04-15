#dev,prod,testing
class Config(object):
	ENV = "dev"
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite://:memory:'
	HOST = "http://joke.liangcuntu.com"
	def getConfig(self):
		conf = Config()
		if(self.ENV=="dev"):
			conf = DevelopmentConfig()
		elif(self.ENV=="testing"):
			conf = TestingConfig()
		elif(self.ENV=="prod"):
			conf = ProductionConfig()
		return conf

class ProductionConfig(Config):
	DATABASE_URI = 'mysql://user@localhost/foo'
	REDIS = {
        'host':'127.0.0.1',
        'port':6379,
        'pass':'db2016'
    }
	MAIL = {
		"host":"smtp.163.com",
		"user":"fffy2366",
		"pass":"vjdyps@163",
		"postfix":"163.com"
	}

class DevelopmentConfig(Config):
	DEBUG = True
	HOST = "http://localhost:5000"
	REDIS = {
        'host':'127.0.0.1',
        'port':6379,
        'pass':'db2016'
    }
	MAIL = {
		"host":"smtp.163.com",
		"user":"fffy2366",
		"pass":"vjdyps@163",
		"postfix":"163.com"
	}

class TestingConfig(Config):
	TESTING = True


if __name__ == "__main__":
	conf = Config()

	print conf.getConfig().REDIS['host']