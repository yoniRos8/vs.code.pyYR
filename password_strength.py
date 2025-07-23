def password_strength(password)
    count_points=0#סופר את הנקודות על כל פרמטר
    if(len(password)>=8 and len(password)<=11):
        count+=1
    if(len(password)>=12):
        count=+2
    common_passwords=["password","123456","1234","admin","000000","111111","abc123","qwerty"]
    common=password.lower() in common_passwords
    if(common):
        count-=2
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    if(has_lower):
        count+=1
    if(has_upper):
        count+=1
    if(has_digit):
        count+=1
    if(has_special):
        count+=1

    if(count<=0):
        print("Weak password, Try a new one!")
    if(count<=3 and count>=1):
        print("Mid password")
    if(count>3):
        print("Strong password, Nice joob!!!") 

    