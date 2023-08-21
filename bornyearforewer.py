year = input("В каком году родился Пушкин? ")
while True:
    if year == "1799":
        break
    else:
        print("Неверно")
        year = input("В каком году родился Пушкин? ")
print("Верно")
