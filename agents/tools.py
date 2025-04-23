from langchain.tools import tool
from db import db
import dateparser

@tool
def add_todo_tool(task: str) -> str:
    """Add a task to the todo list."""
    
    # Add the task to the database
    db.add_todo(task)
    return f"'{task}' added to TO-DO'."

@tool
def show_todo_tool() -> str:
    """Get the todo list."""
    
    # Get the todo list from the database
    todos = db.show_todo()
    if not todos:
        return "No tasks in the TO-DO list."
    
    # Format the todo list as a string
    todo_list = "\n".join([f"- {todo[1]}" for todo in todos])
    return f"TO-DO list:\n{todo_list}"

@tool
def delete_todo_tool(task: str) -> str:
    """Delete a task from the todo list."""
    
    # Delete the task from the database
    db.delete_todo(task)
    return f"'{task}' deleted from TO-DO'."

@tool
def add_reminder_tool(note: str, time_str: str) -> str:
    """Add a reminder. The time string will be parsed, like 'in 2 hours' or 'tomorrow at 5pm'."""
    
    remind_at = dateparser.parse(time_str)
    if not remind_at:
        return "⚠️ Couldn't understand the reminder time."
    db.add_reminder(note, remind_at.isoformat())
    return f"🔔 Reminder set: {note} at {remind_at.strftime('%Y-%m-%d %H:%M')}"

@tool
def show_reminders_tool() -> str:
    """Get the reminders."""
    
    reminders = db.show_reminders()
    if not reminders:
        return "No reminders set."

    reminder_list = "\n".join([f"- {reminder[1]} at {reminder[2]}" for reminder in reminders])
    return f"Reminders:\n{reminder_list}"

@tool
def delete_reminder_tool(reminder_id: int) -> str:
    """Delete a reminder."""
    
    db.delete_reminder(reminder_id)
    return f"Reminder with ID {reminder_id} deleted."