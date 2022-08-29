class Property():
    def __init__(self):
        self.income = 2000.00
        self.deductions()
        self.cash()
        self.roi()
    
    def total(self):
        print(f"Your total monthly income is {self.income} dollars!")


    def deductions(self):
        tax = 150.00
        insurance = 100.00
        repairs = 100.00
        capex = 100.00
        vacancy = 100.00
        manager = 200.00
        mortage = 860.00
        self.expense = tax + insurance + repairs + capex + vacancy + manager + mortage
        print(f"Your expenses are {self.expense}")
        
    def cash(self):
        cashflow = self.income - self.expense
        print(f"Your total profit is {cashflow}")
        
    def roi(self):
            down_payment = 40000.00
            closing_cost = 3000.00
            rehab_budget = 7000.00
            total_investment = down_payment + closing_cost + rehab_budget
            annual_profit = 390.00 * 12.00
            cashoncash = annual_profit / total_investment
            print(cashoncash)
            print("Your Property is bringing you in a ROI of 9.38%")
    
    
my_property = Property()
my_property.total()
my_property.deductions()
my_property.cash()
my_property.roi()

        

        
        
        



        
        
        