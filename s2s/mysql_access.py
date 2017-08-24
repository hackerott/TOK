import MySQLdb

#######################################
## receives the station id, returns station location and first date from dataset
def _pull_station_loc (id0):
	id1 = int(id0)
	db = MySQLdb.connect("localhost","root","&i1hm","s2s_db" )
	cursor = db.cursor()
	s_lat = "Select lat from station_tb where id='%i';" % (id1)
	s_lon = "Select lon from station_tb where id='%i';" % (id1)
	s_date = "Select date from station_tb where id='%i';" % (id1)
	cursor.execute(s_lat)
	cursor.execute(s_lon)
	cursor.execute(s_date)

	lat, lon, date = cursor.fetchall()
	db.close()

	return(lat[0], lon[0], date[0])
#######################################
## receives the station id, returns station data set
def _pull_station_data(id0, var_id):
	db = MySQLdb.connect("localhost","root","&i1hm","s2s_db" )
	cursor = db.cursor()
	s_date = "Select date from data_station where id='%i';" % (id0)
	s_datea= "Select '%i' from data_station where id='%i';" % (var_id, id0)
	cursor.execute(s_date)
	cursor.execute(s_data)
	date, data = cursor.fetchall()
	db.close()
	
	return(data, date)
#######################################
def _pull_model_data(id0, var_id):
	db = MySQLdb.connect("localhost","root","&i1hm","s2s_db" )
	cursor = db.cursor()
	s_date = "Select date from data_model where id='%i';" % (id0)
	s_data = "Select '%i' from data_model where id='%i';" % (var_id, id0)
	s_star = "Select '%i' from data_model where id='%i';" % (var_id, id0)
	cursor.execute(s_date)
	cursor.execute(s_data)
	cursor.execute(s_star)
	date, data, start = cursor.fetchall()
	db.close()
	
	return(data, date, start)
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

