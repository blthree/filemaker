import pyodbc
conn_str = 'Driver=FileMaker ODBC;AllAsText=0;ApplicationUsingThreads=1;FetchChunkSize=100;' \
           'FileOpenCache=0;IntlSort=0;MaxTextlength=255;ServerAddress=127.0.0.1;' \
           'TranslationOption=0;UseRemoteConnection=1;'
# make the connection
cnxn = pyodbc.connect("DSN=ABRC-DNAOrdItems;UID=admin;PWD=")
# create a cursor object
cursor = cnxn.cursor()
j = cursor.tables()
orders = cursor.execute('''select ABRC_stock_number, num_stocks_perstocknum from DNAOrdItem where num_stocks_perstocknum > 1''')
print(type(orders))
sql = '''select ABRC_stock_number, num_stocks_perstocknum from DNAOrdItem where num_stocks_perstocknum > ?'''
test = []
for row in cursor.execute(sql, 1):
    test.append(row)
    print(row)

a = test.copy()

print(a)




