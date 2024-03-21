import os
import sys

sys.path.append("..")
SCRIPTS_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPTS_DIR, '../..')))

from datetime import datetime
import requests



def campaign_get_activity_data():
    API = 'https://www.boredapi.com/api/activity'
    r = requests.get(API)
    return r.json()

if __name__ == "__main__":
    campaign_get_activity_data()

