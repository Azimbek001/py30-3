class Asset:
    pass

class InsurableItem:
    pass

class InterestBearingItem:
    pass

class BankAccount(InsurableItem, Asset, InterestBearingItem):
    pass

class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass

class Security(InterestBearingItem, Asset):
    pass

class Stock(Security):
    pass

class RealEstate(Asset, InsurableItem):
    pass

class Bond(Security):
    pass

