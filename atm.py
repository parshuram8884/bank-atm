class atm(object);
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin1

    def balanceinquiry(self):
        print("Your balance is 1000")

    def cashwidthdrawal(self,amount):
        new_amount = 100-amount
        print("you withdrawed: " + str(amount) + "your remaining balance is :" + str(new_amount))


