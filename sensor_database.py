
#!/usr/bin/python

import serial 
import MySQLdb

#establish connection to MySQL. You'll have to change this for your database.
dbConn = MySQLdb.connect("localhost","root","","ping") or die ("could not connect to database")
#open a cursor to the database
cursor = dbConn.cursor()

device = '/dev/ttyACM0' #this will have to be changed to the serial port you are using
try:
  print "Trying...",device 
  arduino = serial.Serial(device, 9600)
  print "Connected...."
except: 
  print "Failed to connect on",device    
while True:
    try: 
      data = arduino.readline()  #read the data from the arduino
      #pieces = data.split("\t")  #split the data by the tab
      #Here we are going to insert the data into the Database
      try:
        #cursor.execute("id int NOT NULL AUTO_INCREMENT")  
        cursor.execute("INSERT INTO distance (distance_cm) VALUES (%s)", data)
        print "Data inserted"
        dbConn.commit() #commit the insert
        #cursor.close()  #close the cursor
      except MySQLdb.IntegrityError:
        print "failed to insert data"
      #finally:
        #cursor.close()  #close just incase it failed
    except:
      print "Failed to get data from Arduino!"
