import sys
import socket
try:
    import psycopg2
except ImportError:
    print("PostgreSQL test requested, but psycopg2 not installed. "
          "Try 'pip install psycopg2' and try again.")
    sys.exit(1)

def pg_check(config):
    host = config.get("host", "localhost")
    port = int(config.get("port", 5432))
    user = config.get("user")
    passw = config.get("pass")
    dbname = config.get("database")
    try:
        conn = psycopg2.connect(host=host, port=port, user=user,
                                password=passw, dbname=dbname,
                                connect_timeout=2)
        conn.cursor().execute(config.get("test_query", "select 1"))
        conn.close()
    except:
        return False
    else:
        return True


