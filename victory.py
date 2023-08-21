while True:
    correctAnswers = 0
    year = input("В каком году родился Наполеон? ")  # 1769
    if year == "1769":
        correctAnswers += 1
    year = input("В каком году родилась Мадонна? ")  # 1958
    if year == "1958":
        correctAnswers += 1
    year = input("В каком году родился Леонардо да Винчи? ")  # 1452
    if year == "1452":
        correctAnswers += 1
    year = input("В каком году родился Гагарин? ")  # 1932
    if year == "1932":
        correctAnswers += 1
    year = input("В каком году родился Пётр I? ")  # 1672
    if year == "1672":
        correctAnswers += 1
    print(f"Верных ответов: {correctAnswers}")
    print(f"Ошибок: {5 - correctAnswers}")
    print(f"% верных ответов: {correctAnswers*20}%")
    print(f"% ошибок: {100 - correctAnswers*20}%")
    repeat = input("Начать игру сначала? ")
    if repeat != "да":
        break