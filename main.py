class Vehicle:
    owner = None
    __model = None
    __engine_power = None
    __color = None
    __COLOR_VARIANTS = ['blue', 'candy_red', 'Emerald_Blue', 'black', 'white']
    def get_model(self, __model):
        self.__model = __model
        return print(f'Модель {self.__model}')
    def get_power(self,__engine_power):
        self.__engine_power = __engine_power
        return print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self, __color):
        self.__color = __color
        return print(f'Цвет: {self.__color}')
    def print_info(self, owner):
        self.owner = owner
        print(self.get_model)
        print(self.get_power)
        print(self.get_color)
        print(f'Владелец:{self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'candy_red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('CANDY_RED')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()