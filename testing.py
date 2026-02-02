import sqlite3
from datetime import datetime
import csv
from pathlib import Path


def valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
valid_date()
    
