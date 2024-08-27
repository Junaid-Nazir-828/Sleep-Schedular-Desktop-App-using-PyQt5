import os
from pathlib import Path

def get_logged_in_username(self):
        return os.getlogin()

def get_database_path(self):
    machine_name = get_logged_in_username()
    base_path = Path(f"C:/Users/{machine_name}/Documents")
    database_path = base_path / "sleep_schedular.db"
    return database_path