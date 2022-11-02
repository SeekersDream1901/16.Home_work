from pathlib import Path

# Главная директория
GENERAL_DIR = Path(__file__).resolve().parent
# Директория с файлами json
DATA_DIR = GENERAL_DIR.joinpath('data')

# Файлы json
OFFERS_JSON = DATA_DIR.joinpath('offers.json')
ORDERS_JSON = DATA_DIR.joinpath('orders.json')
USERS_JSON = DATA_DIR.joinpath('users.json')

# Директория для БД и указание имени для создаваемой БД
APP_DIR = GENERAL_DIR.joinpath('app', 'database.db')
