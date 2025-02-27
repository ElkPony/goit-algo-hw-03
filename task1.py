#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
from datetime import datetime

def get_days_from_today(date):
    try:
        today = datetime.today() #знаходимо сьогоднішню дату
        conv_date = datetime.strptime(date, "%Y-%m-%d") # конвертуємо введені дані у формат дати
        return (today - conv_date).days
    except ValueError :
        return f"{date} is not a date, please write a date"
    
print(get_days_from_today('2020-12-02')) #вивід функції