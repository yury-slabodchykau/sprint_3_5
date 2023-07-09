class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        self.full = full
        if not full:
            return super().describe()
        else:
            return (f'Попугай {self.name} — заметная птица, '
                    f'окрас её перьев — {self.color}, а размер — {self.size}. '
                    f'Интересный факт: попугаи чувствуют ритм, '
                    f'а вовсе не бездумно двигаются под музыку. '
                    f'Если сменить композицию, '
                    f'то и темп движений птицы изменится.')


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        self.full = full
        if not full:
            return super().describe()
        else:
            return (f'Размер пингвина {self.name} из рода {self.genus} — '
                    f'{self.size}. '
                    f'Интересный факт: однажды группа геологов-разведчиков '
                    f'похитила пингвинье яйцо, и их принялась преследовать вся'
                    f' стая, не пытаясь, впрочем, при этом нападать.'
                    f' Посовещавшись, похитители вернули птицам яйцо,'
                    f' и те отстали.')


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')


print(kesha.describe())
print(kowalski.describe(True))
