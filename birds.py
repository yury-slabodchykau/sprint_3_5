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
        if full:
            return (f'Попугай {self.name} — заметная птица, '
                    f'окрас её перьев — {self.color}, '
                    f'а размер — {self.size}. '
                    'Интересный факт: попугаи чувствуют ритм, '
                    'а вовсе не бездумно двигаются под музыку. '
                    'Если сменить композицию, '
                    'то и темп движений птицы изменится.')
        return super().describe()

    def repeat(self, phraze):
        self.phraze = phraze
        return f'Попугай {self.name} говорит: {self.phraze}.'


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if full:
            return (f'Размер пингвина {self.name} '
                    f'из рода {self.genus} — {self.size}. '
                    'Интересный факт: однажды группа геологов-разведчиков '
                    'похитила пингвинье яйцо, '
                    'и их принялась преследовать вся стая, '
                    'не пытаясь, впрочем, при этом нападать. '
                    'Посовещавшись, похитители вернули птицам яйцо, '
                    'и те отстали. ')
        return super().describe()

    def swimming(self):
        return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.'


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')


print(kesha.repeat('Кеша хороший!'))
print(kowalski.swimming())
