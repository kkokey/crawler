import mysql.connector
import ConfigParser
from distutils.util import strtobool

ppConfig = ConfigParser.RawConfigParser()
ppConfig.read('/usr/local/crawler/config.properties')

#config = {
#	'user': configUser,
#	'password': configPass,
#	'host': configHost,
#	'database': configDb,
#	'raise_on_warnings': configRow,
#	'use_pure': configIsPure,
#}

config = {}
config['user'] = ppConfig.get("SectionDB", "user")
config['password'] = ppConfig.get("SectionDB", "password")
config['host'] = ppConfig.get("SectionDB", "host")
config['database'] = ppConfig.get("SectionDB", "database")
config['raise_on_warnings'] = eval(ppConfig.get("SectionDB","raise_on_warnings"))
config['use_pure'] = ppConfig.get("SectionDB", "use_pure")


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT host, user, password  FROM user")

rs = cursor.execute(query)

for (host, user, password) in cursor:
		print("'{}', '{}', '{}'".format(host, user, password))

cnx.close()


