-- Lists all cities contained in the database

SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities 
JOIN hbtn_0d_usa.states on cities.state_id = states.id
ORDER BY cities.id ASC;
