class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):
    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salaray(self, ):
        if self.salary <= self.company_bank:
            self.company_bank -= self.salary
            print(f'Сотрудник получил зарплату  в размере: {self.salary}$')
        else:
            print(f'Недостаточно средсв!')

    def person_info(self, ):
        print(f'{self.first_name}{self.last_name}\nзарплата:{self.salary}$')


erzat = Person(int(input('Капитал банка в даный момент:')), 'Bakai bank', 'Erzat', 'Amirbek uulu', 40)
erzat.person_info()
erzat.get_salaray()
