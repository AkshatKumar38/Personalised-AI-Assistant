from langchain.tools import tool
from db import db
import dateparser

@tool
def add_todo_tool(task: str) -> str:
    """Add a task to the todo list."""

    db.add_todo(task)
    return f"'{task}' added to TO-DO'."

@tool
def show_todo_tool(input_str: str) -> str:
    """Display the to-do list. Accepts a dummy string input for compatibility."""

    todos = db.show_todo()
    if not todos:
        return "No tasks in the TO-DO list."

    todo_list = "\n".join([f"- {todo[1]}" for todo in todos])
    return f"TO-DO list:\n{todo_list}"

@tool
def delete_todo_tool(task: str) -> str:
    """Delete a task from the todo list."""

    db.delete_todo(task)
    return f"'{task}' deleted from TO-DO'."

@tool
def add_reminder_tool(reminder_text: str) -> str:
    """Add a reminder. The input should be a single string like 'Reminder text, Time string' (e.g., 'Buy groceries, tomorrow at 6pm')."""

    try:
        note, time_str = reminder_text.split(",", 1)
        note = note.strip()
        time_str = time_str.strip()
    except ValueError:
        return "⚠️ Invalid reminder format. Please use 'Reminder text, Time string' (e.g., 'Buy milk, tomorrow at 9am')."

    remind_at = dateparser.parse(time_str)
    if not remind_at:
        return "⚠️ Couldn't understand the reminder time."
    db.add_reminder(note, remind_at.isoformat())
    return f"🔔 Reminder set: {note} at {remind_at.strftime('%Y-%m-%d %H:%M')}"

@tool
def show_reminders_tool(input_str: str) -> str:
    """Get the reminders."""

    reminders = db.show_reminders()
    if not reminders:
        return "No reminders set."

    reminder_list = "\n".join([f"- {reminder[1]} at {reminder[2]}" for reminder in reminders])
    return f"Reminders:\n{reminder_list}"

@tool
def delete_reminder_tool(reminder_id: str) -> str:
    """Delete a reminder."""

    db.delete_reminder(int(reminder_id))
    return f"Reminder with ID {reminder_id} deleted."