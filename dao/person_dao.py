from config.db_config import pg_config
import psycopg2


class PersonDao:

    def __init__(self):
        #Connect to Database
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url) # verify if is _connect

    # Retrieve all the accounts...
    def get_persons(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Person;" # Get all Person...
        cursor.execute(query)
        result = []
        for row in cursor :
            result.append(row)
        return result