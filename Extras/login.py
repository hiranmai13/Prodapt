username="Pinky"
password="123"
i=0
while i<3:
    uname=input("Enter Username : ")
    p=input("Enter Password : ")

    if p==password and uname==username:
        print("Login successful")
        break
    if p!=password or uname!=username:
        print("Invalid Credentials")
    i=i+1
print("You have reached maximum attempts")