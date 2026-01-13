username = input("Enter your Username: ")

def valid_user(username:str)->bool:
    length = len(username) >= 6
    if length and username[0].isalpha() and username[-1].isdigit():
        return True    
    return False

is_valid = valid_user(username)

if is_valid:
    print("Username is Valid")
else:
    print("Username is Invalid")
    
    
class PasswordValidator():
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(self.name)

if __name__=="__main__":
    validator = PasswordValidator("Ajit")
    validator.greet()
     
    
    
