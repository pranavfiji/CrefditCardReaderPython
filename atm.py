class Atm(object):
    def _init_ (self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def cashWithDrawal(self):
        print("Your cash has been withdrawed")

    def balanceInquiry(self):
        print("Your credit card has $100")
        