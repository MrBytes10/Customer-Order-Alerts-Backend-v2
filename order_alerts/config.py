# order_alerts/config.py

import os

DATABASE_CONFIG = {
    'NAME': os.environ.get('DB_NAME', 'order-alertdb'),
    'USER': os.environ.get('DB_USER', 'ndeti'),
    'PASSWORD': os.environ.get('DB_PASSWORD', 'ndeti@2030'),
    'HOST': os.environ.get('DB_HOST', 'localhost'),
    'PORT': os.environ.get('DB_PORT', '5432'),
}
