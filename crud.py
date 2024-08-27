import sqlite3
import utils

def insert_sleep_schedule(hours, minutes):
    db_path = utils.get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO sleep_schedular (hours, minutes)
        VALUES (?, ?)
    ''', (hours, minutes))
    
    conn.commit()
    conn.close()

def read_sleep_schedules():
    db_path = utils.get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sleep_schedular')
    rows = cursor.fetchall()
    
    conn.close()
    return rows

def update_sleep_schedule(schedule_id, hours, minutes):
    db_path = utils.get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE sleep_schedular
        SET hours = ?, minutes = ?
        WHERE id = ?
    ''', (hours, minutes, schedule_id))
    
    conn.commit()
    conn.close()

def delete_sleep_schedule_by_time(hour, minute):
    db_path = utils.get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Delete the record that matches the given hour and minute
    cursor.execute('''
        DELETE FROM sleep_schedular
        WHERE hours = ? AND minutes = ?
    ''', (hour, minute))

    conn.commit()
    conn.close()

# formatted functions

def get_formatted_times():
    db_path = utils.get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Select all hours and minutes from the sleep_schedular table
    cursor.execute('SELECT hours, minutes FROM sleep_schedular')
    rows = cursor.fetchall()
    
    conn.close()

    # Format the times as 'H:MM' and return them as a list
    formatted_times = [f'{hour}:{minute:02d}' for hour, minute in rows]
    
    return formatted_times