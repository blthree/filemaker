import pyodbc
import datetime
conn_str = 'Driver=FileMaker ODBC;AllAsText=0;ApplicationUsingThreads=1;FetchChunkSize=100;' \
           'FileOpenCache=0;IntlSort=0;MaxTextlength=255;ServerAddress=127.0.0.1;' \
           'TranslationOption=0;UseRemoteConnection=1;'
# make the connection
cnxn = pyodbc.connect("DSN=ABRC-DNAOrdItems;UID=admin;PWD=")
# create a cursor object
cursor = cnxn.cursor()
j = cursor.tables()
print(j)
#orders = cursor.execute('''select ABRC_stock_number, num_stocks_perstocknum, Person_tair_id from DNAOrdItem where num_stocks_perstocknum > 1''')
sql = '''select ABRC_stock_number, order_id_tair, date_order_placed from DNAOrdItem where date_order_shipped > ?'''
#orders = cursor.execute('''select ABRC_stock_number, num_stocks_perstocknum, Person_tair_id from DNAOrdItem where date_order_shipped > ?''')
test1 = """SELECT ABRC_stock_number, num_stocks_perstocknum, date_item_shipped FROM DNAOrdItem WHERE date_item_shipped > DATE '2017-01-01'"""
orders = cursor.execute(test1)
test = """SELECT COUNT (ABRC_stock_number), INT(year_item_shipped), INT (month_item_shipped) FROM DNAOrdItem WHERE date_item_shipped > ? GROUP BY year_item_shipped, month_item_shipped"""
#orders = cursor.execute(sql, datetime.date(2016,6,30)).fetchall()
print(cursor.execute(test, datetime.date(2016,1,1)).fetchall())
'''while orders is not None:
    #orders = cursor.execute(test, datetime.date(2017,1,1)).fetchall()
    print(orders.fetchall())
    test = []
    for row in orders:
        test.append(row)
        print(row)
'''
#a = test.copy()

#print(a)




