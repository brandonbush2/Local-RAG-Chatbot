from datetime import datetime

GREETING_TRIGGERS = [
    "hi","hello","hey", "good morning", "good afternoon",
    "good evening", "yoh", "what's up", "sup", "greetings"
]

INTERNET_TRIGGERS =[
    "access the internet", "browse the web", "search online",
    "go online", "real-time", "live data", "current news",
    "latest news", "check online"
]

DATE_TRIGGERS - [
    "today's date", "what date", "what day", "current date",
    "what is today", "day is it", "when is today"
]

def get_date():
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y") #Thursday, April 09, 2026