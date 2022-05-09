class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        #print(ingredients,toppings)
        
    def scoops(self):
        ingredients = self.ingredients
        toppings = self.toppings
        l = []
        for i in ingredients:
            for j in toppings:
                l.append([i,j])
        return(l)

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]