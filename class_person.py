class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def Full_Name(self):
        print(self.first_name +" "+ self.last_name) 
    

new_erson=Person("Yoni","Rosis")
new_erson.Full_Name()