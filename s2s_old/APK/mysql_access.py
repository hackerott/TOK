import MySQLdb


# recebe o id vindo do cliente, devolve o token
def token_get (id0):

	db = MySQLdb.connect("localhost","root","&i1hm","tempook_db" )
	cursor = db.cursor()
	r_token = "Select token from apk_tb where user='%s';" % (id0)
	cursor.execute(r_token)
	token_db=cursor.fetchall()
	db.close()
	for row in token_db:
		0
	return(row[0])

