year = input("В каком году родился Пушкин? ")
if year == "1799":
    day = input("Введите день рождения Пушкина в формате DD/MM ")
    if day=="06/06":
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")
