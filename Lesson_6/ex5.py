# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.
class FamilyMember:
    first_name: str
    middle_name: str
    last_name: str
    age: str
    sisters: list
    brothers: list
    sex: str

    def __init__(self, first_name, last_name, age, sex, middle_name=''):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.sisters = []
        self.brothers = []

    def __str__(self):
        result = f'{self.get_full_name()}\n' \
                 f'Age: {self.age}\n' \
                 f'Sex: {self.sex}'
        if self.sisters:
            result = f'{result}\nSisters: {self.get_sisters()}'
        if self.brothers:
            result = f'{result}\nBrothers: {self.get_brothers()}'
        return result

    def get_full_name(self):
        if self.middle_name:
            full_name = f'{self.first_name} {self.middle_name} {self.last_name}'
        else:
            full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def add_sister(self, sister):
        if sister not in self.sisters:
            self.sisters.append(sister)
            if self.sex == 'male':
                sister.add_brother(self)
            else:
                sister.add_sister(self)

    def add_brother(self, brother):
        if brother not in self.brothers:
            self.brothers.append(brother)
            if self.sex == 'male':
                brother.add_brother(self)
            else:
                brother.add_sister(self)

    def get_sisters(self):
        sisters = []
        for sister in self.sisters:
            sisters.append(sister.first_name)
        return sisters

    def get_brothers(self):
        brothers = []
        for sister in self.brothers:
            brothers.append(sister.first_name)
        return brothers


class Parent(FamilyMember):
    daughters: list
    sons: list

    def __init__(self, *args):
        super(Parent, self).__init__(*args)
        self.daughters = []
        self.sons = []


class Child(FamilyMember):
    parents: list
    mom: FamilyMember
    father: FamilyMember

    def __init__(self, *args):
        super(Child, self).__init__(*args)
        self.parents = []


class Mom(Parent):
    husband: FamilyMember


class Father(Parent):
    wife: FamilyMember


class Daughter(Child):
    pass


class Son(Child):
    pass


if __name__ == '__main__':
    marge = Mom('Marjorie', 'Simpson', 37, 'female', 'Jacqueline')
    homer = Father('Homer', 'Simpson', 38, 'male', 'Jay')
    marge.husband = homer
    homer.wife = marge
    lisa = Daughter('Lisa', 'Simpson', 8, 'female', 'Marie')
    bart = Son('Bartholomew', 'Simpson', 10, 'male', 'JoJo')
    maggie = Daughter('Margaret', 'Simpson', 1, 'female', 'Evelyn')
    bart.add_sister(lisa)
    bart.add_sister(maggie)
    lisa.add_sister(maggie)
    print(marge, '\n')
    print(bart, '\n')
    print(lisa, '\n')
    print(maggie)
