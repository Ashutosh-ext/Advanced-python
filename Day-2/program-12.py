class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

#create an instance of a person
person = Person("John",18)

#getattr to get the value of attribute
name = getattr(person,"name")
print(f"Name:{name}")

#setattr to set value of attribute
setattr(person,"age","31")
print(f"Updated age:{person.age}")

#hasattr to check if attribute exists
has_name = hasattr(person,"name")
print(f"Has attribute name:{has_name}")

#delattr to delete an attribute
delattr(person,"age")
#to check if attribute still exists
has_age = hasattr(person,"age")
print(f"Has attribute 'age' after deletion: {has_age}")
