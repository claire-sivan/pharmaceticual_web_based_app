import mysql.connector
__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='0000',
                                        host='127.0.0.1',
                                        port='3307',
                                        database='qwklife_pharma')
    return __cnx
