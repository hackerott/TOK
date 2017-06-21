import MySQLdb


# recebe o id vindo do cliente, devolve o token
def token_get (id0):
	id1 = int(id0)
	db = MySQLdb.connect("localhost","root","&i1hm","tempook_db" )
	cursor = db.cursor()
	r_token = "Select token from main_tb where id='%i';" % (id1)
	cursor.execute(r_token)
	token_db=cursor.fetchall()
	r_id = "Select id from main_tb where token='%s';" % (token_db[0])
	cursor.execute(r_id)	
	id_db  =  cursor.fetchall()	
	db.close()
	for row in token_db:
		0
#		print  row[0]
	for rrow in id_db:
		0
#		print rrow[0]
	return(row[0], rrow[0])

# recebe o valor do token e do id
def token_update(hash1, id0):
#	print hash1
	id1 = int(id0[0])
	db = MySQLdb.connect("localhost","root","&i1hm","tempook_db" )
	cursor = db.cursor()
	u_token="UPDATE main_tb SET token='%s' WHERE id='%i';" % (hash1, id1)
	cursor.execute(u_token)
	db.commit()
	db.close()
	return(True)

