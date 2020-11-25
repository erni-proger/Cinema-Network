Network = []
flag = False


class Cinema:
    def __init__(self, name, n_zal):
        self.name = str(name)
        self.cinema = []
        for i in range(int(n_zal)):
            self.cinema.append(Zal())

    def zal_size(self, n_zal, x, y):
        self.cinema[int(n_zal) - 1].zal_size(int(x), int(y))

    def get_zal(self, n):
        try:
            return self.cinema[int(n) - 1].info()
        except IndexError:
            print('Ошибка: Зал не найден')

    def buy(self, n_zal, x, y):
        if int(n_zal) > len(self.cinema):
            print('Ошибка: Зал не найден')
            return None
        self.cinema[int(n_zal) - 1].buy_seat(int(x), int(y))

    def sell(self, n_zal, x, y):
        if int(n_zal) > len(self.cinema):
            print('Ошибка: Зал не найден')
            return None
        self.cinema[int(n_zal) - 1].sell_seat(int(x), int(y))

    def info(self):
        return f"Название кинотеатра: {self.name} \n Кол-во залов: {len(self.cinema)}"


class Zal:
    def __init__(self):
        self.seats = []

    def zal_size(self, x, y):
        self.seats = []
        for i in range(y):
            self.seats.append([0 for i in range(x)])
        return self.seats

    def buy_seat(self, x, y):
        try:
            if self.seats[y - 1][x - 1] != 1:
                self.seats[y - 1][x - 1] = 1
                return True
            else:
                print('Место нельзя купить')
                return False
        except IndexError:
            print('Ошибка: Такого места нет')
            return None

    def sell_seat(self, x, y):
        try:
            if self.seats[y - 1][x - 1] != 0:
                self.seats[y - 1][x - 1] = 0
                return True
            else:
                print('Место нельзя продать')
                return False
        except IndexError:
            print('Ошибка: Такого места нет')
            return None

    def info(self):
        return self.seats


if __name__ == '__main__':
    while True:
        print('Для помощи введите {help}')
        command = input()
        if command == 'help':
            print('Все кинотеатры      --- network')
            print('Создать сеть        --- crt_network')
            print('Выбрать кинотеатр   --- cinema {num}')
            print('Указать размер зала --- zal_size {num} {x} {y}')
            print('Показать зал        --- get_zal {num}')
            print('Купить              --- buy {num} {x} {y}')
            print('Продать             --- sell {num} {x} {y}')
            print('Инфо                --- info')

        if command == 'network':
            for el in Network:
                print(el.info())

        if command == 'crt_network':
            try:
                print("Введите кол-во кинотеатров:")
                n = int(input())
                for i in range(n):
                    print(f"Введите название кинотеатра №{i + 1}:")
                    name = input()
                    print(f"Введите кол-во залов:")
                    n = int(input())
                    Network.append(Cinema(name, n))
                print("Сеть создана")
            except Exception:
                print('Ошибка: введены неверные данные')
        try:
            if command.split()[0] == 'cinema':
                cinema = int(command.split()[1]) - 1
                print('Вы вошли в кинотеатр')
                flag = True
        except Exception:
            print('Такого кинотеатра нет')
        try:
            if command.split()[0] == 'zal_size':
                if flag is True:
                    Network[cinema].zal_size(command.split()[1], command.split()[2],
                                             command.split()[3])
                    print("Зал изменен")
                else:
                    print('Сначала войдите в кинотеатр')

            if command.split()[0] == 'get_zal':
                if flag is True:
                    for i in range(len(Network[cinema].get_zal(command.split()[1]))):
                        print(Network[cinema].get_zal(command.split()[1])[i])
                else:
                    print('Сначала войдите в кинотеатр')

            if command.split()[0] == 'buy':
                if flag is True:
                    if Network[cinema].buy(command.split()[1], command.split()[2],
                                           command.split()[3]):
                        print("Место куплено")
                else:
                    print('Сначала войдите в кинотеатр')

            if command.split()[0] == 'sell':
                if flag is True:
                    if Network[cinema].sell(command.split()[1], command.split()[2],
                                            command.split()[3]):
                        print("Место продано")
                else:
                    print('Сначала войдите в кинотеатр')
        except Exception:
            print('Ошибка: команда введена неверно')
        if command == 'info':
            if flag is True:
                print(Network[cinema].info())
            else:
                print('Сначала войдите в кинотеатр')
