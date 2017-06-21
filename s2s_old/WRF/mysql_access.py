import MySQLdb

# recebe o id vindo do cliente, devolve o token
def token_get (id1):
	db = MySQLdb.connect("localhost","root","senha","TESTE_DB" )
	cursor = db.cursor()
	r_token = """Select token from tb_token where id=%i""" % (id1)
	token_db=cursor.execute(r_token)
	r_id = """Select id from tb_token where token=%i""" % (token_db)
	id_db  =  cursor.execute(r_id)	
	db.close()
	
	return(token_db)

# recebe o valor do token e do id
def token_update(hash1, id1):
	db = MySQLdb.connect("localhost","root","senha","TESTE_DB" )
	cursor = db.cursor()
	u_token=""" UPDATE tb_token SET token=%s WHERE id=%i """, (hash1, id1)
	cursor.execute(u_token)
	db.close()
	
	return(true)

