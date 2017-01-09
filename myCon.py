import mysql.connector
import ConfigParser

class DbConnection():

	def getConfig():
		config = {}
		
		ppConfig = ConfigParser.RawConfigParser()
		ppConfig.read(r'../config.properties')

		config['user'] = ppConfig.get("SectionDB", "user")
		config['password'] = ppConfig.get("SectionDB", "password")
		config['host'] = ppConfig.get("SectionDB", "host")
		config['database'] = ppConfig.get("SectionDB", "database")
		config['raise_on_warnings'] = eval(ppConfig.get("SectionDB","raise_on_warnings"))

## Perhaps add option??
#config['pool_size'] = 5
#config['use_pure'] = ppConfig.get("SectionDB", "use_pure")

		return config

	def getDbPool(dbConfig):
		cnxPool = mysql.connector.connect(pool_name="myPool", **dbConfig)

## another option?
#cnxPool = mysql.connector.connect(pool_name="myPool", pool_size="5")
#cnxPooling = mysql.connector.pooling.MySQLConnectionPool(pool_name = "myPool", pool_size = "3", **dbConfig)

		return cnxPool

	def selectQuery(cnx, strQuery):
		if not strQuery:
			strQuery = ("SELECT host, user, password  FROM user")

		cursor = cnx.cursor()
		rs = cursor.execute(strQuery)

		for (host, user, password) in cursor:
				print("'{}', '{}', '{}'".format(host, user, password))

	def dbClose(cnx):
		cnx.close()
	
	print("##### GO")
	selectQuery(getDbPool(getConfig()), "")



