# Linjer der starter med "#" kaldes kommentarer, de læses ikke af computereren, 
# men kan bruges af mennesker til at forklare hvad koden gør


# Linjen "def setup():" svarer til blokken "når der klikkes på det grønne flag" i scratch
# det vil sige den kører når programmet startes. De linjer som er "rykket ind" neden under svarer til
# at man i scratch sætter en blok sammen med "når der klikkes på det grønne flag" i scratch
def setup():
    # linjen herunder sætter størrelsen på vinduet, som programmet er i, det første tal bestemmer bredden, det andet bestemmer højden.
    # Prøv at leg lidt med de her tal for at se hvad de gør
    size(1000, 600) 
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
    # denne linje ligner meget den ovenover. heigth er altid højden på vinduet programmet kører i, det betyder at vi her får en tilfælig værdi mellem 0 og højden på vinduet.
    # Vi laver også endnu en variabel, denne hedder y, og vi kan derfor skrive y længere nede i koden, hvis vi har brug tallet
    y = random(0, height)
    # her sætter vi endnu en variabel til et tilfældigt tal. Men her er det tilfældige tal mellem 10 og 100
    radius = random(10, 100)
    farve = random(0, 255)
    # fill bruges til at sætte en farve der skal bruges til at udfylde de figurer der skal tegnes, figurer kan for eksempel være firkanter, cirkler eller stjerner
    # til at sætte farven bruges 3 tal, alle tallene skal være mellem 0 og 255, lige nu vil vi kun kikke på det første tal, det tal kan ændre farven, for eksempel giver 0 en rød farve, 40 giver en gul farve, og 150 giver en blå farve
    # Da "farve" er sat til en tilfældig værdi ovenfor vil denne linje sørge for at alle cirklerne vi tegner får en tilfældig farve.  
    fill(farve,255,255)
    # alle figurer får tegnet en strej rundt om sig, ligesom fill kan bruges til at bestemme hvilken farve figuren skal udfyldes med, kan stroke bruges til at bestemme farven på strejen rundt om figuren
    stroke(farve,255,255)
    # ellipse bruges til at tegne cirkler eller ellipser (aflange cirkler). x og y bestemmer hvor på skærmen cirklen skal tegnes, ligesom et koordinatsystem, jo større x er jo længere til højre på skærmen tegnes cirklen
    # jo større y er jo længere nede på skærmen tegnes cirklen. radius og radius bestemmer størrelsen på cirklen, hvis disse er ens bliver der tegnet en cirkel, hvis de er forskellige får man en aflang cirkel
    # Da alle tallene er tilfældige, får vi her en cirkel et tilfældigt sted på skærmen, med en tilfældig størrelse.
    ellipse(x,y,radius,radius)
