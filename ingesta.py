import mysql.connector
import csv
import boto3

conexion = mysql.connector.connect(
    host="18.213.155.42",
    user="root",
    password="utec",
    database="tienda"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM fabricantes")

with open('archivo.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    columnas = [i[0] for i in cursor.description]
    csvwriter.writerow(columnas)
    
    for fila in cursor.fetchall():
        csvwriter.writerow(fila)

cursor.close()
conexion.close()

ficheroUpload = "archivo.csv"
nombreBucket = "bucket-output-guillermo124"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")
