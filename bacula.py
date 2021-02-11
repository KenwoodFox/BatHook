import psycopg2
from config import read_config as config


class Bacula:
    def __init__(self):
        print("Created a new bacula instance.")

        print("Reading config params.")
        # read connection parameters
        self.params = config(filename='config.ini',
                             section='postgresql')

        # Collect the database cursor from the connect method.
        self.cur = self.connect() 
        print("Connected, nothing to do. Closing now.")
        self.cur.close()

    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**self.params)
            
            # create a cursor
            cur = conn.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

            return(cur)

            #print('Try showing what running jobs look like:')
            #cur.execute("Select * from Job where JobStatus='R';")
            #jobs = cur.fetchall()
            #for job in jobs:
            #    print(job)

        
            # close the communication with the PostgreSQL
            #cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
