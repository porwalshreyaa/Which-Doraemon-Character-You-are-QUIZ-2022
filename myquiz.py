print("Which Doraemon Character You are? QUIZ 2022")
name= input("Enter your name: ")
print("""--answer the questions below, Y or N, 'in uppercase'--""")
lens= input("Do you wear eye lens?: ")
if lens == "Y":
  teach= input("Do you like teaching?: ")
  if teach == "Y":
    print("GOT IT", name+"!", "You are Nobita's class teacher.")
  else:
    study= input("Do you like reading books?: ")
    if study == "Y":
      comics= input("Do you like reading coics?: ")
      if comics == "Y":
        print("GOT IT", name+"!", "You are Nobita.")
      else:
        print("sorry", name, "we couldn't recognise you.")
    else:
      problems= input("Do you like helping others?: ")
      if problems == "Y":
        print("GOT IT", name+"!", "You are Nobita's Mom.")
      else:
        print("sorry", name, "we couldn't recognise you.")

else:
  skirt= input("Do you wear skirt?: ")
  if skirt == "Y":
    brother= input("Do you have a brother?: ")
    if brother == "Y":
      print("GOT IT", name+"!", "You are Jaiko.")
    else:
      print("GOT IT", name+"!", "You are Suzuka.")
  else:
    sing= input("Do you like singing a lot?: ")
    if sing == "Y":
      strength= input("Are you the strongest among your friends?: ")
      if strength == "Y":
        print("GOT IT", name+"!", "You are Gian.")
      else:
        gadgets= input("Do you like technology a lot?: ")
        if gadgets == "Y":
          car= input("Do you have a car?: ")
          if car== "Y":
            print("GOT IT", name+"!", "You are Suneo.")
          else:
            problems= input("Do you like helping others?: ")
            if problems == "Y":
              print("GOT IT", name+"!", "You are Doraemon.")
            else:
              print("sorry", name, "we couldn't recognise you.")
        else:
            problems= input("Do you like helping others?: ")
            if problems == "Y":
              print("GOT IT", name+"!", "You are Doraemon.")
            else:
              print("sorry", name, "we couldn't recognise you.")
    else:
        gadgets= input("Do you like technology a lot?: ")
        if gadgets == "Y":
          car= input("Do you have a car?: ")
          if car== "Y":
            print("GOT IT", name+"!", "You are Suneo.")
          else:
            problems= input("Do you like helping others?: ")
            if problems == "Y":
              print("GOT IT", name+"!", "You are Doraemon.")
            else:
              print("sorry", name, "we couldn't recognise you.")
        else:
            problems= input("Do you like helping others?: ")
            if problems == "Y":
              print("GOT IT", name+"!", "You are Doraemon.")
            else:
              print("sorry", name, "we couldn't recognise you.")          

