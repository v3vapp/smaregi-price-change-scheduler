from dotenv import load_dotenv

load_dotenv()

import os

user = os.getenv('SUMAREGI_EMAIL')
pw = os.getenv('SUMAREGI_PASSWORD')
