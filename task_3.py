print('Задача 3. Таймер для микроволновых печей')

# Мы разрабатываем микропрограмму — таймер обратного отсчета для микроволновых печей.
# Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране.
# В нашем случае будем выводить в консоль сообщение с обратным отсчетом в секундах от “reverse_timer” до момента
# готовности, то есть «0» секунд, и спрашивать пользователя, готов ли он забрать еду.

# Пользователь в любой момент может прервать режим разогрева, введя «1» (то есть ответить «Да, еда готова»), тогда
# программа выводит на экран сообщение «Ваша еда готова, можете забрать» и показывает, на какой секунде был прерван
# таймер.
# Если пользователь отвечает «0», что равноценно «Нет», то таймер уменьшается. Когда он достигнет «0» секунд, выводим
# сообщение «Ваша еда готова, осторожно горячo!»

# В данном задании используем цикл for.
# “reverse_timer” – переменная счетчик, которую запрашиваем у пользователя через функцию ввода input.

reverse_timer = int(input("Установите время разогрева: "))

for second in range(reverse_timer, -1, -1):
    print(f"Осталось {second} секунд.")
    food_cooked = int(input("Еда готова? 1/0: "))
    if food_cooked:
        break

print("Ваша еда готова, осторожно горячо!")
