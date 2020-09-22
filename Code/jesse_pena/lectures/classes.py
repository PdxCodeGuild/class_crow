class Dish:
    def __init__(self, name, clean='clean', location='cabinet'):
        self.name = name
        self.clean = clean
        self.location = location
    def useDish(self):
        if self.location == 'cabinet':
            self.location = 'out'
            self.clean = 'dirty'
        else:
            self.location = 'still out'
        return self.location
    def putAway(self):
        if self.clean == 'clean':
            self.location == 'cabinet'
        else: 
            self.location = self.location
        return self.location

bowl = Dish('bowl')

print(bowl.useDish())
print(bowl.clean)
print(bowl.putAway())
print(bowl.location)

pan = Dish('pan', 'dirty', 'stove')
print(pan.location)