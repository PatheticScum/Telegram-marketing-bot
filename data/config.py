import os

BOT_TOKEN = '1986053589:AAH9Wnvu_AkaLUSIa9nhJ6UPPXpM3xi24_s'  # Bot token
ADMINS = [402031255, ]  # adminlar ro'yxati


WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
PROVIDER_TOKEN = '371317599:TEST:1649507975065'
