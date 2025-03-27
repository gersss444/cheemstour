import psycopg2

def get_connection():
    return psycopg2.connect(
        host='aws-0-us-west-1.pooler.supabase.com',
        port=6543,
        user='postgres.hgxoohrxwgugotqpafiz',
        password='A54C4jofR5OPgS25',
        database='postgres')
