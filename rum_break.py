import random

# Lägg till en huvudmeny med minst "Starta spelet" och "Avsluta"
# Ett hinder mot målet (t.ex. en låst dörr ett pussel eller en fiende) 
# - Möjlighet att fly från fiender, t.ex. simulera ett tärningskast 1-3 du flyr, 4-6 du blir dödad 
# minst 2 funktioner

def huvudmeny():
    print("Välkommen till äventyrsspelet!")
    print("1. Starta spelet")
    print("2. Avsluta")
    val = input("Välj ett alternativ: ")
    if val == "1":
        starta_spelet()
    elif val == "2":
        print("Tack för att du spelade!")
    else:
        print("Ogiltigt val. Försök igen.")
        huvudmeny()

def losa_pussel():
    print("Du hittar en låst dörr. För att öppna den måste du lösa ett pussel.")
    
    problem = [
        ("Vad är 7 + 5?", "12"),
        ("Vad är 15 - 9?", "6"),
        ("Vad är gånger av 6 och 7?", "42"),
        ("Vad är roten ur  36", "6")
    ]
    
    val = random.choice(problem)
    fråga, rätt_svar = val
    
    print(fråga)
    svar = input("Skriv ditt svar: ")
    
    if svar == rätt_svar:
        print("Rätt! Dörren är nu öppen.")
        input("Tryck på enter för att fortsätta")
        return True
    else:
        print("Fel svar! Du kan inte öppna dörren.")
        return False

def fly_fran_fiende():
    print("En fiende dyker upp!")
    print("Du försöker fly...")
    tarning = random.randint(1, 6)
    print(f"Du slog en {tarning}.")
    if tarning <= 5:
        print("Du lyckades fly!")
        return True
    else:
        print("Du blev dödad av fienden.")
        return False

def starta_spelet():
    print("Du vaknar upp i ett tomt rum med två dörrar.")

    # Första valet
    spelarens_val = input("Välj dörr 1 eller 2: ")
    if spelarens_val == "1":
        print("Du valde dörr 1 och blev uppäten av en ko.")
        return
    elif spelarens_val == "2":
        print("Du valde dörr 2 och överlevde.")
    else:
        print("Ogiltigt val. Spelet avslutas.")
        return

    # Andra scenen med ett hinder
    if not losa_pussel():
        print("Du sitter fast i rummet. Spelet avslutas.")
        return

    # Fiende dyker upp
    if not fly_fran_fiende():
        print("Spelet är över.")
        return

    # Sista valet
    spelarens_val = input("Rummet är nu blått. Välj dörr 1 eller 2: ")
    if spelarens_val == "1":
        print("Du flydde grattis!")
    else:
        björn = input("Framför dig står det en björn med ett svärd, vill du fly? Ja nej ").lower()
        if (björn == "ja"):
            print("Du lyckades fly och klarade spelet, grattis")
        else:
            print("Du dog av svärdet men björnen åt upp dig också.")

# Starta spelet från huvudmenyn
huvudmeny()
