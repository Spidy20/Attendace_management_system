import pymysql.connections
connection = pymysql.connect(host='localhost', user='root', password='', db='test')
cursor = connection.cursor()
import csv
name='javaa_2019_02_21_time_09_33_12'
cursor.execute("select * from "+name+";")
with open("out.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor)