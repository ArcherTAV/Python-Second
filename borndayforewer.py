year = input("В каком году родился Пушкин? ")
while True:
    if year == "1799":
        break
    else:
        print("Неверно")
        year = input("В каком году родился Пушкин? ")
print("Верно")


day = input("Введите день рождения Пушкина в формате DD/MM ")
while True:
    if day=="06/06":
        break
    else:
        print("Неверно")
        day = input("Введите день рождения Пушкина в формате DD/MM ")
        
print("Верно")