grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#надеюсь, меня простят за использование циклов для автоматизации работы, всё-таки в задании написано:
#"Самостоятельно составлять (вручную) словарь не нужно"

dictionary = {}
students = list(students)
length = len(students)
for i in range(length): dictionary[students[-i]] = sum(grades[i]) / len(grades[i])
print(dictionary)