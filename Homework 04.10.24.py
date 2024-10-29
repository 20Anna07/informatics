import matplotlib.pyplot as plt

# Упражнение 1
# x = [(i ** 2 + 5) * (i ** 2 + i - 12) for i in range (1, 77, 3)]
# y = [ i for i in range(1, 77, 3)]

# plt.plot(x, y)
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
# plt.title('Функция f(x)')
# plt.grid(True, which = 'major', axis = 'both', linestyle = 'dashed')
# plt.scatter(x, y, color = 'purple', marker = '*')
# plt.plot(x, y, color = 'pink', marker = '_' , markersize = 7)
# plt.show()


#Упражнение 2
# amount = [77, 7, 7, 8, 3, 6]
# groups = ["комар", "лесничий", "леший", "хруст ветки", "волк", "тени"]
# color_ = ["salmon", "violet", "bisque", "cyan", "magenta", "pink"]
# plt.pie(amount, labels=groups, colors=color_, autopct='%1.f%%')
# plt.title("Что самое страшное ночью в лесу?")
# plt.show()

#Упражнение 3
length = [189, 172, 162, 192, 154, 188, 183, 198, 162, 199, 193, 197, 160, 171, 184, 168, 188, 155, 178, 163, 181, 173, 161, 151, 200, 163, 165, 192, 185, 193, 162, 177, 194, 153, 153, 162, 171, 187, 153, 193, 151, 168, 168, 199, 162, 166, 174, 195, 172, 167, 171, 183, 185, 194, 190, 179, 152, 162, 198, 159, 171, 174, 173, 177, 196, 190, 174, 181, 169, 187, 175, 179, 196, 199, 175, 180, 174, 188, 198, 150, 154, 186, 185, 190, 200, 160, 162, 184, 174, 192, 163, 190, 152, 187, 176, 176, 186, 193, 184, 192]
plt.hist(length, bins=5, edgecolor='mediumspringgreen', color = 'lightcoral')
plt.xlabel('length')
plt.ylabel('Person count')
plt.show()
