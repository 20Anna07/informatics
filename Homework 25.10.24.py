class Students:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
class Characteristics(Students):
    def __init__(self, name, course, happiness, health, knowledge):
        super().__init__(name, course)
        if self.course == 'applicant':
            self.happiness = 10
            self.health = 10
            self.knowledge = 1
        elif self.course == 'first':
            self.happiness = 7
            self.health = 5
            self.knowledge = 3
        elif self.course == 'second':
            self.happiness = 6
            self.health = 8
            self.knowledge = 6
        elif self.course == 'third':
            self.happiness = 5
            self.health = 6
            self.knowledge = 9
        elif self.course == 'fourth':
            self.happiness = 5
            self.health = 7
            self.knowledge =  8
        elif self.course == 'graduate':
            self.happiness = 10
            self.health = 10
            self.knowledge = 6
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Knowledge: {self.knowledge}")
    
    def sleeping(self):
        """"Восстановление здоровья"""
        type = input('Когда спал персонаж?')
        if type == 'day':
            print(f'{self.name} спит днем')
            self.health += 1
            self.happiness += 3
            print(f'Health: {self.health}({self.health - 1}+1)')
            print(f'Happiness: {self.happiness}({self.happiness - 3}+3)')
        elif type == 'night':
            print(f'{self.name} спит ночью')
            self.health += 3
            self.happiness += 2
            print(f'Health: {self.health}({self.health - 3}+3)')
            print(f'Health: {self.health}({self.health - 2}+2)')

    def exams(self):
        """Потеря здоровья"""
        type = input('Какое задание впереди?')
        if type == 'colloquium':
            self.health -= 2
            self.happiness -= 2
            self.knowledge += 2
            print(f'{self.name} готовится к {type}')
            print(f'Health: {self.health}({self.health + 2}-2)')
            print(f'Happiness: {self.happiness}({self.happiness + 2}-2)')
            print(f'Knowledge: {self.knowledge}({self.knowledge - 2}+2)')
        if type == 'homework':
            self.health -= 1
            self.happiness -= 1
            self.knowledge += 1
            print(f'{self.name} готовится к {type}')
            print(f'Health: {self.health}({self.health + 1}-1)')
            print(f'Happiness: {self.happiness}({self.happiness + 1}-1)')
            print(f'Knowledge: {self.knowledge}({self.knowledge - 1}+1)') 
        if type == 'test':
            self.health -= 3
            self.happiness -= 4
            self.knowledge += 4
            print(f'{self.name} готовится к {type}')
            print(f'Health: {self.health}({self.health + 3}-3)')
            print(f'Happiness: {self.happiness}({self.happiness + 4}-4)')
            print(f'Knowledge: {self.knowledge}({self.knowledge - 4}+4)') 
        if type == 'exam':
            self.health -= 4
            self.happiness -= 6
            self.knowledge += 7
            print(f'{self.name} готовится к {type}')
            print(f'Health: {self.health}({self.health + 4}-4)')
            print(f'Happiness: {self.happiness}({self.happiness + 6}-6)')
            print(f'Knowledge: {self.knowledge}({self.knowledge - 7}+7)')
        print('------------------')
        if self.health <= 3:
            print(f'Level of health:{self.health}')
            print('Вам стоит отдохнуть!')
        elif self.happiness <= 3:
            print(f'Level of health:{self.happiness}')
            print('Вам стоит отдохнуть!')

Valerie = Characteristics('Valerie', 'third', 0, 0, 0)
# Valerie.display_info()
Valerie.sleeping()
# Valerie.exams()