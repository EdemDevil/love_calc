print("Добро пожаловать в калькулятор любви!")
name1 = input("Введите ваше имя: ")
name2 = input("Введите имя вашего партнера: ")
lower_name = name1.lower() + name2.lower()

true = lower_name.count("t") + lower_name.count("r") + lower_name.count("u") + lower_name.count("e")
love = lower_name.count("l") + lower_name.count("o") + lower_name.count("v") + lower_name.count("e")
love_score = str(true) + str(love)
int_love_score = int(love_score)

if int_love_score <= 10 or int_love_score >= 90:
    print(f"Ваш счёт {int_love_score}, вы совместимы как Кола и Ментос")
elif int_love_score >= 40 and int_love_score <= 50:
    print(f"Ваш счёт {int_love_score}, вамм будет комфортно вместе")
else:
    print(f"Ваш счёт {int_love_score}%")