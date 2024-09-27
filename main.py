highschool = int(input("Would you like to join the berry avenue high school? 1.yes 2.no thank you"))
attend = int(input("Enter your past exam notes please:"))
if highschool==1:
    print("Allowed to join")
else:
    if attend>=75:
      print("Allowed to join") 
    else:
       print("Not allowed becouse you have bad notes")   