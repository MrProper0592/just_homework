print("hello, let's write some thing about your animal")
class life_of_cat:
    def __init__(self, borg, cord, name, age, color, kg, fN, national, region):
        self.name = name
        self.age = age
        self.color = color
        self.kg = kg
        self.fN = fN
        self.national = national
        self.region = region
        self.cord = cord
        self.borg = borg
    def F(self):
        print("\n\n\ngender:", self.borg, "\nanimal:", self.cord, '\nname:',self.name,"\nage:",self.age,'\ncolor:',self.color,"\nkg:",self.kg,"\nfather's name:",self.fN,"\nfrom(country):",self.national,"\nfrom(region):",self.region)
cat1 = life_of_cat(input("gender:"), input("animal:"), input('name:'), int(input("age:")), input('color:'), int(input("kg:")), input("father's name:"), input("from(country):"), input("from(region):"))
cat1.F()