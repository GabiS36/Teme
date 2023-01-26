from abc import abstractmethod, ABC


class FormaGeomatrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am coluri')


class Patrat(FormaGeomatrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def get_latura(self):
        return self.__latura

    def set_latura(self, new_latura):
        self.__latura = new_latura

    def delete_latura(self):
        del self.__latura

    def aria(self):
        return self.__latura ** 2


class Cerc(FormaGeomatrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def get_raza(self):
        return self.__raza

    def set_raza(self, new_raza):
        self.__raza = new_raza

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.pi * self.__raza ** 2

    def descrie(self):
        print('Eu nu am colturi')


print('Patrat: ')
patrat1 = Patrat(10)
patrat1.descrie()
print('- Latura patratului este: ', patrat1.get_latura)
print('- Aria patratului este:', patrat1.aria())
patrat1.set_latura(8)
print("- Valoarea noua a laturii patratului este:", patrat1.get_latura)
print("- Aria patratului devine:", patrat1.aria())
patrat1.delete_latura()

print('Cerc: ')
cerc1 = Cerc(12)
cerc1.descrie()
print('- Aria cercului este:', cerc1.aria())
cerc1.set_raza(20)
print('- Valoarea noua a razei cercului este: ', cerc1.get_raza)
print('- Aria cercului este: ', cerc1.aria())
cerc1.delete_raza()
