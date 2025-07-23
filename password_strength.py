def password_strength(password):
    count_points=0#סופר את הנקודות על כל פרמטר
    if(len(password)>=8 and len(password)<=11):
        count_points+=1
    if(len(password)>=12):
        count_points=+2
    common_passwords=["password","123456","1234","admin","000000","111111","abc123","qwerty"]
    common=password.lower() in common_passwords
    if(common==True):
        count_points-=2
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    if(has_lower):
        count_points+=1
    if(has_upper):
        count_points+=1
    if(has_digit):
        count_points+=1
    if(has_special):
        count_points+=1

    if(count_points<=0):
        return("Weak password, Try a new one!")
    if(count_points<=3 and count_points>=1):
        return("Mid password")
    if(count_points>3):
        return("Strong password, Nice job!!!") 

password=input("Enter a password please: ")
print(password_strength(password))