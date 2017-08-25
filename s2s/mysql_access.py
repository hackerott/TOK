import MySQLdb

#######################################
## receives the station id, returns station location and first date from dataset
def _pull_station_loc (id0):
	id1 = int(id0)
	db = MySQLdb.connect("localhost","root","&i1hm","s2s_db" )
	cursor = db.cursor()
	s_data = "Select lat, lon, date from station_tb where id='%i';" % (id1)   ## search all at same time
	cursor.execute(s_data)
	data = cursor.fetchall()
	db.close()
	lat, lon, date = data[:,0], data[:,1], data[:,2]
	return(lat, lon, date)
#######################################
## receives the station id, returns station data set
def _pull_station_data(id0, var_id):
	db = MySQLdb.connect("localhost","root","&i1hm","s2s_db" )
	cursor = db.cursor()
	s_data= "Select '%i', date from data_station where id='%i';" % (var_id, id0)
	cursor.execute(s_data)
	data = cursor.fetchall()
	db.close()
	out, date = data[:,0], data[:,1]
	return(out, date)
#######################################
def _pull_model_data(id0, var_id):
	db = MySQLdb.connect("localhost","root","&i1hm","s2s_db" )
	cursor = db.cursor()
	s_data = "Select '%i', date, start from data_model where id='%i';" % (var_id, id0)
	cursor.execute(s_data)
	data = cursor.fetchall()
	db.close()
	out, date, start = data[:,0], data[:,1], data[:,2]
	return(out, date, start)
#######################################
##
def _push_model_data(hash1, id0):
#	print hash1
	id1 = int(id0[0])
	db = MySQLdb.connect("localhost","root","&i1hm","tempook_db" )
	cursor = db.cursor()
	u_token="UPDATE main_tb SET token='%s' WHERE id='%i';" % (hash1, id1)
	cursor.execute(u_token)
	db.commit()
	db.close()
	return(True)

