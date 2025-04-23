import sqlite3
from datetime import datetime

def init_db(): # create a database and two tables: todos and reminders
    """Initialize the database and create tables if they don't exist."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
            note TEXT NOT NULL,
            remind_at TEXT NOT NULL
        )''')
    conn.commit()
    conn.close()

# todo functions
def add_todo(task): # add a task to the todos table
    """Add a task to the todos table."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()

def show_todo(): # get all tasks from the todos table
    """Get all tasks from the todos table."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('SELECT todo_id, task FROM todos ORDER BY created_at DESC')
    todos = cursor.fetchall()
    conn.close()
    return todos

def delete_todo(todo_id): # delete a task from the todos table
    """Delete a task from the todos table."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()


# reminder functions
def add_reminder(note, remind_at): # add a reminder to the reminders table
    """Add a reminder to the reminders table."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reminders (note, remind_at) VALUES (?, ?)', (note, remind_at))
    conn.commit()
    conn.close()

def show_reminders(): # get all reminders from the reminders table
    """Get all reminders from the reminders table."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('SELECT reminder_id, note, remind_at FROM reminders ORDER BY remind_at ASC')
    reminders = cursor.fetchall()
    conn.close()
    return reminders

def delete_reminder(reminder_id): # delete a reminder from the reminders table
    """Delete a reminder from the reminders table."""
    
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reminders WHERE id = ?', (reminder_id,))
    conn.commit()
    conn.close()