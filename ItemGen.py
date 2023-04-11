import random

class ItemGen:
    def ItemNameGen(self):
        # Define empty string
        itemName = ""
        
        # Generate a random number between 1 and 40
        length = random.randint(1,40)
        
        # Loop through the length of the item name
        for i in range(length):
        
            # Generate a random char from the alphabet
            char = chr(random.randint(97,122))
            
            # If the random number is divisable by 9, add a space to the item name
            if(i % 9 == 0):
                itemName += " "
            else:
                itemName += char
        
        # Return the randomly generated item name
        return itemName
    
    def DescriptionGen(self):
        # Define empty string
        desName = ""
        
        # Generate a random number between 1 and 40
        length = random.randint(60,256)
        
        # Loop through the length of the item name
        for i in range(length):
        
            # Generate a random char from the alphabet
            char = chr(random.randint(97,122))
            
            # If the random number is divisable by 9, add a space to the item name
            if(i % 9 == 0):
                desName += " "
            else:
                desName += char
        
        # Return the randomly generated item name
        return desName

    def PriceGen(self):
        min = 1.00
        max =1000000.00
        #return the generated price
        price = round(random.uniform(min, max), 2)

        return price
    
    def CreateItemData(self):
        # Generate a random item name
        itemName = self.ItemNameGen()
        # Generate a random description
        desName = self.DescriptionGen()
        # Generate a random price
        price = self.PriceGen()

        return [(itemName, desName ,price)]
