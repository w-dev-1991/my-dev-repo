import Pyspark

df.show() #- wyswietla dane

#Reading the file
df = spark.read.csv("csv_file_name.csv", inferSchema = True, header=True)

    #reading multiline json file
    json_data = spark.read.option('multiline', "true").json("/temp/lesson1/mutliline_file.json")

#Writing to the file
df.write.mode('append')json('/temp/write_folder/file_name')
df.write.mode('overwrite')json('/temp/write_folder/file_name')



#Creating temporary view
df.createOrReplaceTempView("temp_view_name")

#Creating temporary view with SQL
%sql
CREATE TEMPORARY VIEW temp_view_name
USING csv
OPTIONS(path "/temp/lesson1/sampletable.csv")

#show dataframe Schema
df.printSchema()

#--Manipulating Columns--
import pyspark.sql.functions as F

df.select("col_name").show(1) 
df.select(F.col("col_name")).show(1)
df.select("col_name", "col_name2").show(1) 


#*Changing column name
df.select(F.expr("col_name as new_col_name")).show(1)
df.select(F.expr("col_name as new_col_name").alias("col_name").show(3)


#*Addition of new column
new_df = df.selectExpr("col_name as new_col_name", "col_name")
new_df2 = df.selectExpr("avg(sales)", "count(distinct(country))")

df.select(F.expr("*"), F.lit(1).alias("One").show() 




#****DBUTILS**** 
dbutils.help()
dbutils.fs.help()
dbutils.widgets.help()

#Widgets
dbutils.widgets.text('variable_name', 'default value', 'label')
print(dbutils.widgets.get('variable_name'))


#creating a file
dbutils.fs.put('/testfolder/file.txt', 'sample text in the file')

#removing a file
dbutils.fs.rm("/testfolder/file.txt") #Removes a file
dbutils.fs.rm('/testfolder/', True) #Removes everything in folder recursivly

#Displaying content of the path
%fs ls "path/"
dbutils.fs.ls('path')
display(dbutils.fs.ls('dbfs://path'))  #displays in tabular view

#running a notebook
dbutils.notebook('/path_to_notebook/notebook.py', 60)    #-> path, timeout
%run /path_to_notebook/notebook.py $arg1="value1" $arg2="value2" $arg3="value3"

#Exit notebook
dbutils.notebook.exit('Some parameters value.')


#*****READING FROM CSV IN PYSPARK*****
https://sparkbyexamples.com/spark/spark-read-csv-file-into-dataframe/

#*****ASTERISK IN PYTHON*****
https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558

#*****PASSING XIT VALUES FROM DATABRICKS NOTEBOOK*****
https://the.agilesql.club/2020/02/passing-status-messages-and-results-back-from-databricks-to-adf/

#*****CUSTOM LOGGING IN DATABRICKS*****
https://www.youtube.com/watch?v=SnIp6p8px5Q&list=PL50mYnndduIGmqjzJ8SDsa9BZoY7cvoeD&index=11&ab_channel=TechLake

