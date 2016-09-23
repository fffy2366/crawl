#dev,prod,testing
class Config(object):
	ENV = "dev"
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite://:memory:'
	HOST = "http://joke.liangcuntu.com"

class ProductionConfig(Config):
	DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
	DEBUG = True
	HOST = "http://localhost:5000"    

class TestingConfig(Config):
	TESTING = True