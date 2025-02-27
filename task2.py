import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min >= 1 \ 
            and max <= 1000 \
            and quantity <= (max - min +1) \
            and quantity > 0 and max > min: #перевіряємо всі необхідні умови
            num_list = list(range(min, max+1))
            return sorted(random.sample(num_list, quantity)) #повертаємо посортований список
        else:
            return []
    except TypeError: #виключаємо помилку при введенні неправильног оформату даних
        return []



lottery_numbers = get_numbers_ticket(7, 8, 1)
print("Ваші лотерейні числа:", lottery_numbers) #приклад виведення