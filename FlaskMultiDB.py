# To work with flask import flask library.
from flask import Flask
# To work with sqlalchemy import sqlalchemy library.
from sqlalchemy import create_engine

# flask constructor.
app = Flask(__name__)


# Decorating route URL for postgresql and binding the function of route.
@app.route('/postgresql')
def postgresql():
    query = 'select * from employees;'
    cur = conn.execute(query)
    pgsql_data = cur.fetchall()

    for row in pgsql_data:
        print("id =", row[0], )
        print("name =", row[1], )
        print("desig =", row[2], "\n")
    return str(pgsql_data)


# Decorating route URL for mysql and binding the function of route.
@app.route('/mysql')
def mysql():
    query = 'select * from employees;'
    cur = conn1.execute(query)
    mysql_data = cur.fetchall()
    return str(mysql_data)


# Attribute value set to run the main program.
if __name__ == '__main__':
    connection = create_engine('postgresql://postgres:secret123@localhost/mohit')
    connection1 = create_engine('mysql+pymysql://root:oracle@localhost/mohit')
    conn = connection.connect()
    conn1 = connection1.connect()
    app.run()
