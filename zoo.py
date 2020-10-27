class Client:
    def __init__(self):
        self.client_data={}
        self.variant=None
    def append_data(self,f,b):
        if f not in self.client_data:
            self.client_data[f]=b
        else:
            print('Клиент уже существует')    
    def output_data(self,f):
        print(f"фио: {f}, ,баланс: {self.client_data[f]}")
    def get_request(self):
        variant=int(input('Введите 1 для внесения записи, 2 - для вывода информации: '))
        if variant in (1,2):
            self.variant=variant
            if self.variant is 1:
                fio=input('Введите ФИО: ')
                balance=int(input('Введите баланс: '))
                self.append_data(fio,balance)
            else:
                fio=input('Введите ФИО: ')
                self.output_data(fio)
        else:
            print('Некорретный ввод')
            
cl=Client()
job=True
while job is True:
    cl.get_request()
    ans=input('Продолжить/закончить работу y/n: ')
    if ans is 'y':
        continue
    elif ans is 'n':
        break
    else:
        print('Введен неверный ответ')
    