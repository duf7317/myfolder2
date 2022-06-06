class Dog: #클래스선언
    name = "삼식이" #속성선언
    age = 12
    bread = "골든 리트리버"
    
    def bark(self): #self는 this
        print(self.name + "가 멍멍하고 짓는다")


newdog = Dog()

newdog.name = "응애"

print(newdog.age)

newdog.bark()

#클래스