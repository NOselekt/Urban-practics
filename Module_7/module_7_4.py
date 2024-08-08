team1_num = 15
team2_num = 24
score_1 = 30
score_2 = 12
team1_time = 1.5
team2_time = 1
challenge_result = 'Мастера кода' if score_1 > score_2 else 'Волшебники данных'
tasks_total = score_2 + score_1
average_time = (team1_time + team2_num) / tasks_total
print("В команде Мастера кода участников: %s!" % team1_num)
print("В команде Волшебники данных участников: %s!" % team2_num)
print("Итого сегодня участников: %s и %s!" % (team1_num, team2_num))
print("Команда Мастера кода решила задач: {}!".format(score_1))
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Мастера кода решили задачи за {} ч!".format(team1_time))
print("Волшебники данных решили задачи за {} ч!".format(team2_time))
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: победа команды {challenge_result}!")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {round(average_time, 2)} часа на задачу!")
