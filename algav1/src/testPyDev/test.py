'''
Created on 27 nov. 2024

@author: diamanka
'''

print("bienvenue à pydev")
v="je ne peut me permettre de tout dire"
print(v)

class animal(object):
    age = 0
    nb_patte = 0
    
    def __init__(self, age, patte):
        self.age = age
        self.nb_patte= patte
        
    def affiche(self):
        print("animal :  agé de ")