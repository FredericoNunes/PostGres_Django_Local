import os

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')


assert DB_HOST, 'Environment variable DB_HOST not found.'
assert DB_NAME, 'Environment variable DB_NAME not found.'
assert DB_PASSWORD, 'Environment variable DB_PASSWORD not found.'
assert DB_PORT, 'Environment variable DB_PORT not found.'
assert DB_USER, 'Environment variable DB_USER not found.'
