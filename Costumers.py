from datetime import datetime, date
import pickle

def saveState(state, tag="W_"):
    with open(f'{tag}state.pkl', 'wb') as fp:
        pickle.dump(state, fp)

def getState(tag="W_"):
    with open(f'{tag}state.pkl', 'rb') as fp:
        return pickle.load(fp)

class Purchase:
    def __init__(self,
                 purchaseId = "0000",
                 purchaseDate="dd-MM-yyyy",
                 itemsPurchased=[],
                 price=1,
                 payed=0):
        self.purchaseId = purchaseId
        self.purchaseDate = purchaseDate
        self.itemsPurchased = itemsPurchased
        self.price = price
        self.payed = payed

    def addPay(self, pay):
        assert type(pay) == float
        self.payed += pay
        return self.price - self.payed

    def __eq__(self, other):
        if type(other) == str:
            return self.purchaseId == other

        if type(other) == type(self):
            return self.purchaseId == other.purchaseId

        return False

    def __str__(self):
        return f'-[{self.purchaseId}] PurchaseDate: {self.purchaseDate}; items:{str(self.itemsPurchased)}; Price:{self.price}; Payed:{self.payed}-'

    def __repr__(self):
        return str(self)
    

class Costumer:
    def __init__(self,
                 costumerId="0000",
                 name="Jane",
                 status="Inactive",
                 dob="dd-MM-yyyy",
                 purchases=None):
        self.costumerId = costumerId
        self.name = name
        self.status = status
        self.dob = dob
        if purchases:
            self.purchases = purchases
        else:
            self.purchases = []

        
    def __iadd__(self, other):
        
        if type(other) == Purchase:
            self.purchases += [other]
        return self

    def registerPurchase(self, itemsPurchased, price, payed):
        
        newId = str(len(self.purchases)+1)
        np = Purchase(newId, str(datetime.now()), itemsPurchased, price, payed)
        self.purchases += [np]
        
        return True
        

    def getBoughtBooksIds(self):
        return sum([p.itemsPurchased for p in self.purchases], [])
    
    def __str__(self):
        return f'-[{self.costumerId}] name: {self.name}; status:{str(self.status)}; dob:{self.dob}; purchases:{str(self.purchases)}-'

    def __repr__(self):
        return str(self)


class Costumers:
    def __init__(self, tag="", resetState=False):
        self.tag = tag
        self.costumers = []

    def saveState(self):
        saveState(self, self.tag+"costumers_")

    def getCustomersState(tag):
        return getState(tag+"costumers_")

    def getCostumersDict(self):
        return [{
                "id":c.costumerId,
                "name": c.name,
                "dob": c.dob,
                "status": c.status,
                "purchases": c.purchases
                    }
                for c in self.costumers]

    def findCostumersByName(self, name):
        return list(filter(lambda c: c.name.lower() == name.lower(), self.costumers))
    
    def addCostumer(self, name, dob):
        if len(self.findCostumersByName(name)) > 0:
            raise Exception(f'Customer name [{name}] already exists')

        newId = str(len(self.costumers)+1)

        newCostumer = Costumer(newId, name, "Active", dob)
        self.costumers += [newCostumer]

        self.saveState()

        return True

    def addPurchaseByName(self, name, itemsPurchased, price, payed):
        currentCostumer = self.findCostumersByName(name)
        if len(currentCostumer) == 0:
            raise Exception(f"Costumer {name} does not exist. Cannot register purchase")

        currentCostumer = currentCostumer[0]
        currentCostumer.registerPurchase(itemsPurchased, price, payed)
        self.saveState()
        return True
    
        
        
        

    

if __name__=="__main__":
    pass
##    cs0 = Costumers.getCustomersState("test_")
##    p0 = Purchase()
##    p1 = Purchase("1", "10-10-2002", ["2","3","2"], 100.1, 100.1)
##    p2 = Purchase("2", "11-10-2002", ["2","3", "4", "5","2"], 222.1, 222.1)
##    p3 = Purchase("3", "11-10-2002", ["6","10"], 300.21, 0)
##    p3.addPay(300.21)
##    c0 = Costumer()
##    c1 = Costumer("1", "Fred", "Active", "10-10-2000", [p1, p2])
##    c1 += p3
##    cs0 = Costumers("test_")
##    cs0.addCostumer("Fred", "10-10-2000")
##    cs0.addPurchaseByName("Fred", ["2","3", "4", "5","2"], 222.1, 222.1)
##    cs0.addPurchaseByName("Fred",["6","10"], 300.21, 0)
