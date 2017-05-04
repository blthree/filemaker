import pyodbc
import datetime
conn_str = 'Driver=FileMaker ODBC;AllAsText=0;ApplicationUsingThreads=1;FetchChunkSize=100;' \
           'FileOpenCache=0;IntlSort=0;MaxTextlength=255;ServerAddress=127.0.0.1;' \
           'TranslationOption=0;UseRemoteConnection=1;'
# make the connection
cnxn = pyodbc.connect("DSN=ABRC-DNAOrdItems;UID=admin;PWD=")
# create a cursor object
cursor = cnxn.cursor()
j = cursor.tables().fetchall()
print(j)

sql = '''select ABRC_stock_number, order_id_tair, date_order_placed from DNAOrdItem where date_order_shipped > ?'''

#test1 = """SELECT ABRC_stock_number, num_stocks_perstocknum, date_item_shipped FROM DNAOrdItem WHERE date_item_shipped > DATE '2017-01-01'"""

test = """SELECT COUNT (ABRC_stock_number), month_item_shipped, YEAR(year_item_shipped) FROM DNAOrdItem WHERE year_item_shipped = ? GROUP BY month_item_shipped, year_item_shipped"""
#test1 = """SELECT ABRC_stock_number, num_stocks_perstocknum, date_item_shipped FROM DNAOrdItem WHERE date_item_shipped = DATE '2017-01-01'"""
#print(cursor.execute(test, datetime.date(2016,1,1)).fetchall())
print(cursor.execute(test, datetime.date(2016,1,1)).fetchall())
#for year in range(2011,2018):
#    print(year)
#    a = cursor.execute(test, datetime.date(year,1,1)).fetchall()
#    print(a)