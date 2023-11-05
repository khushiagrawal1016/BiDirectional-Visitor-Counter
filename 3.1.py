from bottle import route, run

temp=input("Enter the temperature: ")+'*C'
humidity=input("Enter the humidity: ")+'%'
wind_speed=input("Enter the wind speed: ")+'km/hr'
rain=input("Is it rainy or not: ")

@route("/")
def sensor_data():
	sensor_log = {  'temperature':temp,
			'humidity':humidity,
			'wind speed':wind_speed,
			'rain':rain  }
	return sensor_log
run(host='localhost', port=8080, debug=True)
		