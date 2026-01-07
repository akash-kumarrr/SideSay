from server import *
from security import *

def enable_developement_memeber(user):
    try:
        if not is_new_username(user):
            db.collection("users").document(user).update({
                'development_member' : True
            })
            disable_premium_badge(user)
            disable_verification_badge(user)
            print(f"Message : @{user} is now a verified_development_member")
            return True
        else:
            print(f"@{user} does not exist")
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False

def disable_developement_memeber(user):
    try:
        if not is_new_username(user):
            db.collection("users").document(user).update({
                'development_member' : False
            })
            print(f"Message : @{user} is not a verified_development_member")
            return True
        else:
            print(f"@{user} does not exist")
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False
    
def enable_verification_badge(user):
    try:
        if not is_new_username(user):
            db.collection("users").document(user).update({
                'verified_badge' : True
            })
            disable_premium_badge(user)
            disable_developement_memeber(user)
            print(f"Message : @{user} is now a verified_user")
            return True
        else:
            print(f"@{user} does not exist")
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False
    
def disable_verification_badge(user):
    try:
        if not is_new_username(user):
            db.collection("users").document(user).update({
                'verified_badge' : False
            })
            print(f"Message : @{user} is now not a verified_user")
            return True
        else:
            print(f"@{user} does not exist")
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False
    
def disable_premium_badge(user):
    try:
        if not is_new_username(user):
            db.collection("users").document(user).update({
                'premium_badge' : False
            })
            print(f"Message : @{user} is now not a premium_user")
            return True
        else:
            print(f"@{user} does not exist")
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False
    
def enable_premium_badge(user):
    try:
        if not is_new_username(user):
            db.collection("users").document(user).update({
                'premium_badge' : True
            })
            disable_developement_memeber(user)
            disable_verification_badge(user)
            print(f"Message : @{user} is now a premium_user")
            return True
        else:
            print(f"@{user} does not exist")
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False 
    
if __name__ == "__main__":
    while True:
        print("----PRIVALK PROMPT-CONTROL UNIT")
        print("\t1. Enable Development Member")
        print("\t2. Disable Development Member")
        print("\t3. Enable Verification Badge")
        print("\t4. Disable Verification Badge")
        print("\t5. Enable Premium Badge")
        print("\t6. Disable Premium Badge")
        print("\t7. Exit")
        action = input()
        if action == "1":
            username = str(input("Enter the username : "))
            print(enable_developement_memeber(username))
        if action == "2":
            username = str(input("Enter the username : "))
            print(disable_developement_memeber(username))
        if action == "3":
            username = str(input("Enter the username : "))
            print(enable_verification_badge(username))
        if action == "4":
            username = str(input("Enter the username : "))
            print(disable_verification_badge(username))
        if action == "5":
            username = str(input("Enter the username : "))
            print(enable_premium_badge(username))
        if action == "6":
            username = str(input("Enter the username : "))
            print(disable_premium_badge(username))
        if action == "7":
            exit()
        
