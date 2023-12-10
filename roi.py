class Roi():

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.total_invest = 0
        self.annual_cashflow = 0
        self.cashRoi = 0

    def calcincome(self):
        self.rent = int(input("what is your rental income?: "))
        self.laundry = int(input(f"what is your laundry income?: "))
        self.storage = int(input(f"what is your storage income?: "))
        self.misc = int(input("how much are your misc income?: "))

        if self.rent >= 0:
            print(f"your monthly rental income is {self.rent}")
        elif self.rent < 0:
            print("Invalid, try again.")
        if self.laundry >= 0:
            print(f"your monthly laundry income is {self.laundry} ")
        elif self.laundry < 0:
            print("Invalid, try again.")
        if self.storage >= 0:
            print(f"Your monthly storage income is {self.storage}")
        elif self.storage < 0:
            print("Invalid, try again.")
        if self.misc >= 0:
            print(f"Your monthly miscellaneous income is {self.misc}")
        elif self.misc < 0:
            print("Invalid, try again.")

        self.income = self.rent + self.laundry + self.storage + self.misc

        return print(f"The total monthly income is: ${self.income}")
        

    def calcexpenses(self):
        self.expenses = int(input('what is your total monthly expenses? '))
        return print((f'your monthly expenses is {self.expenses}'))

    def calccashflow(self):
        self.cashflow = self.income - self.expenses
        self.annual_cashflow = self.cashflow * 12
        return print((f'your monthly cashflow is {self.cashflow}'))
    
    def calcroi(self):
        self.total_invest = int(input('what is your total investment? '))
        print((f'your total investment is {self.total_invest}'))
        self.cashRoi = (self.annual_cashflow/ self.total_invest) * 100
        return print(f'your cash on cash roi is {self.cashRoi} %')
    
    def run(self):
        while True:
            choice = input('what would you like to see income/expenses/cashflow/roi? ').lower()
            if choice == 'income':
                self.calcincome()
            elif choice == 'expenses':
                self.calcexpenses()
            elif choice == 'cashflow':
                self.calccashflow()
            elif choice == 'roi':
                self.calcroi()
            else:
                print('what would you like to see income/expenses/cashflow/roi? ')
        
        
roi = Roi()
roi.run()