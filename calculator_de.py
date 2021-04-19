#Python by ssk 838375
print("Python Taschenrechner")

while True:
    
  o = int(input("1 = +, 2 = -, 3 = *, 4 = /: "))

  if o == 1:
      a = int(input("A eingeben: "))
      print ("adieren mit")
      b = int(input("B eingeben: "))
      x = (a) + (b)
      print ("")
      print ("")
      print ("Ergebnis ist ", x)
      print ("")
      print ("")
    
  if o == 2:
      a = int(input("A eingeben: "))
      print ("subtrahieren mit")
      b = int(input("B eingeben: "))
      x = (a) - (b)
      print ("")
      print ("")
      print ("Ergebnis ist ", x)
      print ("")
      print ("")
    
  if o == 3:
      a = int(input("A eingeben: "))
      print ("multiplizieren mit")
      b = int(input("B eingeben: "))
      x = (a) * (b)
      print ("")
      print ("")
      print ("Ergebnis ist ", x)
      print ("")
      print ("")
    
  if o == 4:
      a = int(input("A eingeben: "))
      print ("diffidieren mit")
      b = int(input("B eingeben: "))
      x = (a) / (b)
      print ("")
      print ("")
      print ("Ergebnis ist ", x)
      print ("")
      print ("")
  
  print("Neue Berechnung*******")
  print ("")
  print ("")
