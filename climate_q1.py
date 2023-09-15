import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect("climate.db")  # connect to the database
cur = con.cursor()  # create a cursor to interact with the database

cur.execute("SELECT Year, CO2, Temperature FROM ClimateData")  # Select Year CO2 and Temp from the data
rows = cur.fetchall()  # get all data from the execute result

years = [row[0] for row in rows]
co2 = [row[1] for row in rows]
temp = [row[2] for row in rows]

cur.close()  # close the cursor
con.close()  # close the connection

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
