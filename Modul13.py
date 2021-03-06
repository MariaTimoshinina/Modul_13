# Ввод количества билетов; сообщение оскидке, если человек регистрирует больше трёх человек на конференцию
tickets = int(input("При покупке от 4-х билетов действует скидка 10% от стоимости заказа!\n"
                   "Введите количество билетов, которое хотите приобрести на мероприятие:"))

# Ввод возраста владельца каждого из билетов
age = list(map(int, input("Укажите через пробел возраст посетителей: ").split()))

# Проверка, что количество билетов совпадает с количеством ввода возрастов, иначе запрашивается повторный ввод
while tickets != len(age):
    age = list(map(int, input("Количество посетителей не совпадает с количеством билетов.\n"
                              "Укажите через пробел возраст посетителей: ").split()))

# Создание списка для заполнения стоимости билетов в зависимости от возраста
price = []
for i in age:
    if i in range(0, 18):
        price.append(0)
    elif i in range(18, 25):
        price.append(990)
    else:
        price.append(1390)

# Если купили более 3х билетов, то выводится сумма к оплате с учетом скидки 10%,
if tickets > 3:
    print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", sum(price), "рублей")
