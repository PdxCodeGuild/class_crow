import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
p3 = Point()
p2 = Point(5,2)
# p2 = Point(8,4)
dist = p3.distance(p2) # or p2.distance(p1), either works

class Dish:
    def __init__(self, name, clean='clean', location='cabinet', value=0):
        self.name = name
        self.clean = clean
        self.location = location
        self.value = value

    def useDish(self):
        if self.location == 'cabinet':
            self.location = 'out'
            self.clean = 'dirty'
        else:
            self.location = 'still out'
        return self.location
    def putAway(self):
        if self.clean == 'clean':
            self.location =='cabinet'
        else: 
            self.location = self.location
        return self.location
    def valueCheck(self, amount):
        if self.value > amount: 
            return True 
        else: 
            return False
    def decreaseValue(self, amount):

        if self.valueCheck(amount) == True:
            self.value -= amount
        return self.value

bowl = Dish('bowl')
# print(bowl.location)

# print(bowl.useDish())
# print(bowl.clean)
# print(bowl.putAway())
# print(bowl.location)

# pan = Dish('pan', 'diry', 'stove', 100)
# print(pan.location)
# print(pan.decreaseValue(10))
# print(pan.decreaseValue(10))

# print(pan.value)

class Animal: 
    def __init__(self, kind, size):
        self.kind = kind
        self.size = size
    def whatKind(self):
        print(self.kind)

class Pet(Animal):
    def __init__(self):
        Animal.__init__(self, 'dog', 'small')
    def bark(self):
        print('bark')


Otter = Animal('otter', 'medium')
print(Otter.whatKind())

Vivi = Pet()

print(Vivi.whatKind())
Vivi.bark()
Otter.bark()