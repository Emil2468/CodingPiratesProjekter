# Linjer der starter med "#" kaldes kommentarer, de læses ikke af computereren, 
# men kan bruges af mennesker til at forklare hvad koden gør


# Linjen "def setup():" svarer til blokken "når der klikkes på det grønne flag" i scratch
# det vil sige den kører når programmet startes. De linjer som er "rykket ind" neden under svarer til
# at man i scratch sætter en blok sammen med "når der klikkes på det grønne flag" i scratch
def setup():
    # linjen herunder sætter størrelsen på vinduet, som programmet er i, det første tal bestemmer bredden, det andet bestemmer højden.
    # Prøv at leg lidt med de her tal for at se hvad de gør
    size(400, 300) 
    # Denne linje er ikke så vigtig, den gør at farverne bliver lidt pænere    
    colorMode(HSB)
    # Denne linje sætter baggrunden til at være sort, man kan også sætte den til hvid ved at skrive 255 i stedet for 0
    # eller en mørk eller lys grå farve, ved at skrive et tal mellem 0 og 255. Du kan lege lidt med tallet for at finde en pæn baggrund
    background(0)
    
# "def draw():" svarer til blokken "gør for evigt" i scratch. Det vil sige at de linjer der er rykket ind under denne linje
# vil blive kørt så længe programmet kører
def draw():
    # "random" giver os et tilfældig tal der ligger imellem de to tal i parenteserne. "width" er altid bredden på vinduet programmet kører i
    # Det vil sige at random her giver os et tilfældigt tal, der er mellem 0 og bredden på vinduet. 
    # Når vi skriver "x = random(0, width)" betyder det at x sættes til den tilfældige værdi vi får fra "random". Det vil sige at hvis vi senere skal bruge det tilfældige tal, kan vi skrive x i stedet. x kaldes for en variabel 
    x = random(0, width)
    # Her sætter vi y til at være halvdelen af højden på vinduet. heigth er altid sat til højden på vinduet
    y = height / 2
    # her sætter vi endnu to variabler til et tilfældigt tal.
    radius = random(0, 100)
    farve = random(0, 255)
    # fill bruges til at sætte en farve der skal bruges til at udfylde de figurer der skal tegnes, figurer kan for eksempel være firkanter, cirkler eller stjerner
    # til at sætte farven bruges 3 tal, alle tallene skal være mellem 0 og 255, lige nu vil vi kun kikke på det første tal, det tal kan ændre farven, for eksempel giver 0 en rød farve, 40 giver en gul farve, og 150 giver en blå farve
    # Da "farve" er sat til en tilfældig værdi ovenfor vil denne linje sørge for at alle cirklerne vi tegner får en tilfældig farve.  
    fill(farve,255,255)
    # alle figurer får tegnet en strej rundt om sig, ligesom fill kan bruges til at bestemme hvilken farve figuren skal udfyldes med, kan stroke bruges til at bestemme farven på strejen rundt om figuren
    stroke(farve,255,255)
    # ellipse bruges til at tegne cirkler eller ellipser (aflange cirkler). x og y bestemmer hvor på skærmen cirklen skal tegnes, ligesom et koordinatsystem, jo større x er jo længere til højre på skærmen tegnes cirklen
    # jo større y er jo længere nede på skærmen tegnes cirklen. radius og radius bestemmer størrelsen på cirklen, hvis disse er ens bliver der tegnet en cirkel, hvis de er forskellige får man en aflang cirkel
    # Da alle tallene undtaget y er tilfældige, får vi her en cirkel et tilfældigt sted på skærmen, med en tilfældig størrelse.
    ellipse(x,y,radius,radius)
    
# OPGAVE 1
# Det er lidt kedeligt at cirklerne altid er i midten af skærmen, ændre koden så cirklerne kan komme overalt på skærmen.
# Hint 1: Det er kun linje 26 der behøver at blive ændret
# Hint 2: Du kan for eksempel bruge "random" til at sætte y til et tilfældig tal, ligesom x sættes til et tilfældigt tal

# OPGAVE 2
# Billedet er lidt lille. Ændr størrelsen på vinduet så det er 1000 i bredden og 600 i højden
# Hint: Det er kun linje 11 der skal ændres

# OPGAVE 3 (Lidt svær)
# Nogle af cirklerne bliver så små at man nærmest ikke kan se dem. Ændr i koden så cirklerne er mellem 10 og 100 i størrelsen.
# Hint: Det er kun nødvendigt at ændre på linje 28
