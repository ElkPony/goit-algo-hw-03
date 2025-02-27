import re as re

def normalize_phone(phone_number):
    #видаляємо всі зайві значення крім чисел та знака "+"
    num_clean = re.sub(r"[^0-9\+]+", "", phone_number)

    #перевіряємо значення після очистки, якщо начає чисел, або значення менше, виводимо інформацію що це не є номером (можна нічого не виводити)
    if not re.search(r"\d", num_clean) or len(num_clean) < 9:
        return f'{phone_number} is not phone number' #return 

    #в залежності як починається рядок додаємо або "+" або "+380"
    if re.match(r"^\+", num_clean): 
        return num_clean
    elif re.match(r"^380", num_clean):
        return "+" + num_clean
    else:
        return "+38" + num_clean

#дані для перевірки
raw_numbers = [ 
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "00",
    "++"
]

#вивід функції
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)