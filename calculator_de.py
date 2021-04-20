#Python by ssk 838375
#Python Rechner für zwei Zahlen zur Berechnung mit Grundrechenarten

print("Python Taschenrechner um 2 Zahlen zu berrechnen. Zahlen und Operator einzeln eingeben und mit Enter-Taste weiter...")


while True:
        a = int(input("1. Zahl: "))
        o = input("+, -, *, : ?")
        b = int(input("2. Zahl: "))

        if o == "+":
           x = (a) + (b)
           print ("")
           print ("Ergebnis ist ", x)
           print ("")
    
        if o == "-":
           x = (a) - (b)
           print ("")
           print ("Ergebnis ist ", x)
           print ("")
    
        if o == "*":
           x = (a) * (b)
           print ("")
           print ("Ergebnis ist ", x)
           print ("")
    
        if o == "/":
           x = (a) / (b)
           print ("")
           print ("Ergebnis ist ", x)
           print ("")
  
        print("Neue Berechnung*******")
        print ("")
  
else:  
    print("Falsche Eingabe")
