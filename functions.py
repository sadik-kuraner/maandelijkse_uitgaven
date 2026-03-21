import json


def overzicht_tonen(uitgaven_lijst):
    """
    Geeft een overzicht van alle maandelijkse uitgaven in de vorm: naam: €bedrag - betaald.

    Parameters:
    uitgaven_lijst (dict): Een dictionary waarin de keys de uitgaven namen zijn
    en de values een dictionary met:
    - 'bedrag' (int of float): het bedrag van de uitgave
    - 'betaald' (bool of None): True als betaald, False als openstaand, None als n.v.t.

    Returns:
    dict: dezelfde dictionary die is meegegeven.
    """
    for naam, gegevens in uitgaven_lijst.items():
        bedrag = gegevens["bedrag"]
        betaald = gegevens["betaald"]
        print(f"{naam}: €{bedrag} - betaald: {betaald}")
    return uitgaven_lijst


def totale_uitgaven_berekenen(alle_uitgaven):
    """
    Berekend de totale uitgaven door alle bedragen in de nested dict bij elkaar op te tellen.

    Parameter:
    alle_uitgaven (dict): Dictionary waarin de keys de uitgaven namen zijn en de values een
    dictionary met:
    - 'bedrag' (int of float): het bedrag van de uitgave
    - 'betaald' (bool of None): True als betaald, False als openstaand, None als n.v.t.

    Returns:
    int: de som van alle uitgaven.
    """
    totale_uitgaven = 0
    for gegevens in alle_uitgaven.values():
        totale_uitgaven += gegevens["bedrag"]
    return totale_uitgaven


def nieuwe_uitgave_toevoegen(huidige_lijst, nieuwe_uitgave):
    """
    Voegt een nieuwe uitgave toe aan een bestaande uitgavenlijst.

    Parameters:
    huidige_lijst (dict): Bestaande dictionary met uitgaven, waarin de keys de uitgaven namen zijn
    en de values een dictionary met:
    - 'bedrag' (int of float)
    - 'betaald' (bool of None)
    nieuwe_uitgave (dict): Nieuwe uitgave in dezelfde vorm als hierboven.

    Returns:
    dict: De complete dict inclusief de laatst toegevoegde uitgave.
    """
    huidige_lijst.update(nieuwe_uitgave)
    return huidige_lijst


def uitgave_verwijderen(huidige_lijst, te_verwijderen_uitgave):
    """
    Verwijdert een uitgave uit een bestaande uitgavenlijst.

    Parameters:
    huidige_lijst (dict): Bestaande dictionary met uitgaven, waarin de keys de uitgaven namen zijn
    en de values een dictionary met:
    - 'bedrag' (int of float)
    - 'betaald' (bool of None)
    te_verwijderen_uitgave (str): Naam van uitgave die verwijderd moet worden. Als de uitgave
    niet bestaat, gebeurt er niets (None).

    Returns:
    dict: De dictionary na verwijdering van de uitgave.
    """
    huidige_lijst.pop(te_verwijderen_uitgave, None)
    return huidige_lijst


def bestand_opslaan(data, bestandsnaam):
    """
    Slaat een dictionary op in een JSON bestand.

    Parameters:
    data (dict): De dicts die je wilt opslaan.
    bestandsnaam (str): de naam van het bestand.
    """
    with open(bestandsnaam, "w") as f:
        json.dump(data, f, indent=4)


def bestand_laden(bestandsnaam):
    """
    Laad een JSON bestand en zet het om naar een Python object.

    Parameters:
    bestandsnaam (str): Naam van JSON-bestand die je wilt inladen in Python.

    Returns:
    object: De data uit het JSON-bestand, meestal een dictionary of list.
    """
    with open(bestandsnaam, "r") as f:
        data = json.load(f)
    return data


def overzicht_betaald_status(uitgaven_lijst):
    """
    Splitst uitgaven op basis van betaalstatus en print een overzicht per categorie.

    Parameters:
    uitgaven_lijst (dict): een dictionary waarin de keys de uitgaven namen zijn
    en de values een dictionary met:
    - 'bedrag' (int of float): het bedrag van de uitgave
    - 'betaald' (bool of None): True als betaald, False als openstaand, None als n.v.t.

    Returns:
    betaald (lijst van tuples): lijst met (naam, gegevens) van betaalde uitgaven.
    openstaand (lijst van tuples): lijst met (naam, gegevens) van openstaande uitgaven.
    niet_van_toepassing (lijst van tuples): lijst met (naam, gegevens) van overige uitgaven.
    """
    betaald = []
    openstaand = []
    niet_van_toepassing = []
    for naam, gegevens in uitgaven_lijst.items():
        if gegevens["betaald"] == True:
            betaald.append((naam, gegevens))
        elif gegevens["betaald"] == False:
            openstaand.append((naam, gegevens))
        else:
            niet_van_toepassing.append((naam, gegevens))

    if betaald:
        print("Betaalde maandelijkse uitgaven:")
        for naam, gegevens in betaald:
            print(f"- {naam}: €{gegevens['bedrag']}")
        print()
    if openstaand:
        print("Openstaande maandelijkse uitgaven:")
        for naam, gegevens in openstaand:
            print(f"- {naam}: €{gegevens['bedrag']}")
        print()
    if niet_van_toepassing:
        print("Overige maandelijkse uitgaven:")
        for naam, gegevens in niet_van_toepassing:
            print(f"- {naam}: €{gegevens['bedrag']}")
        print()

    return betaald, openstaand, niet_van_toepassing


def keuze_uitgaven_gebruiker(
    persoonlijke_uitgaven_lijst, zakelijke_uitgaven_lijst, overige_uitgaven_lijst
):
    """
    Laat de gebruiker kiezen welke soort uitgaven hij/zij wil bekijken: Persoonlijk,
    Zakelijk of Overig.
    Toont een overzicht van betaalde en openstaande bedragen (voor Persoonlijk en Zakelijk)
    of totaalbedrag (voor Overige uitgaven).

    Parameters:
    persoonlijke_uitgaven_lijst (dict): dictionary met persoonlijke uitgaven
    zakelijke_uitgaven_lijst (dict): dictionary met zakelijke uitgaven
    overige_uitgaven_lijst (dict): dictionary met overige uitgaven

    Returns:
    keuze_uitgaven (int): het getal dat de gebruiker heeft gekozen
    (1 = Persoonlijke uitgaven, 2 = Zakelijke uitgaven, 3 = Overige uitgaven)
    """
    while True:
        try:
            keuze_uitgaven = int(
                input(
                    "Welke uitgaven wil je bekijken? Voer een getal in van 1 t/m 3:\n"
                    "\n- Kies 1 voor Persoonlijke Uitgaven.\n"
                    "- Kies 2 voor Zakelijke Uitgaven.\n"
                    "- Kies 3 voor Overige Uitgaven.\n"
                )
            )

            if keuze_uitgaven == 1:
                print(
                    "\nJe hebt gekozen voor Persoonlijke Uitgaven. Hieronder vind je een overzicht.\n"
                )
                betaald, openstaand, _ = overzicht_betaald_status(
                    persoonlijke_uitgaven_lijst
                )

            elif keuze_uitgaven == 2:
                print(
                    "\nJe hebt gekozen voor Zakelijke Uitgaven. Hieronder vind je een overzicht.\n"
                )
                betaald, openstaand, _ = overzicht_betaald_status(
                    zakelijke_uitgaven_lijst
                )

            elif keuze_uitgaven == 3:
                print(
                    "\nJe hebt gekozen voor Overige Uitgaven. Hieronder vind je een overzicht.\n"
                )
                _, _, niet_van_toepassing = overzicht_betaald_status(
                    overige_uitgaven_lijst
                )
                totaal_overige_uitgaven = sum(
                    gegevens["bedrag"] for _, gegevens in niet_van_toepassing
                )
                print(
                    f"Totaal overige maandelijkse uitgaven: €{totaal_overige_uitgaven}"
                )
                return keuze_uitgaven

            else:
                print("Ongeldige invoer. Voer een getal in tussen 1 t/m 3.")
                continue

            # Deze hoort bij keuze 1 en 2
            totaal_betaald = sum(gegevens["bedrag"] for _, gegevens in betaald)
            totaal_openstaand = sum(gegevens["bedrag"] for _, gegevens in openstaand)
            print(f"Totaal betaalde maandelijkse uitgaven: €{totaal_betaald}")
            print(f"Totaal openstaande maandelijkse uitgaven: €{totaal_openstaand}")

            return keuze_uitgaven

        except ValueError:
            print("Ongeldige invoer. Je moet een getal invoeren.")


def lijst_keuze(
    keuze_uitgaven,
    persoonlijke_uitgaven_lijst,
    zakelijke_uitgaven_lijst,
    overige_uitgaven_lijst,
):
    """
    Bepaalt de juiste uitgavenlijst op basis van de keuze van de gebruiker.

    Parameter:
    keuze_uitgaven (int): het getal dat de gebruiker heeft gekozen in de
    functie 'keuze_uitgaven_gebruiker'.
    persoonlijke_uitgaven_lijst (dict): dictionary met persoonlijke uitgaven
    zakelijke_uitgaven_lijst (dict): dictionary met zakelijke uitgaven
    overige_uitgaven_lijst (dict): dictionary met overige uitgaven

    Returns:
    huidige_lijst (dict): De gekozen uitgavenlijst (persoonlijk, zakelijk of overig)
    """
    if keuze_uitgaven == 1:
        huidige_lijst = persoonlijke_uitgaven_lijst
    elif keuze_uitgaven == 2:
        huidige_lijst = zakelijke_uitgaven_lijst
    elif keuze_uitgaven == 3:
        huidige_lijst = overige_uitgaven_lijst
    else:
        raise ValueError("Ongeldige keuze")

    return huidige_lijst


def uitgave_toevoegen_verwijderen(huidige_lijst):
    """
    Laat de gebruiker een uitgave toevoegen, verwijderen of overslaan
    in de uitgavenlijst die is gekozen in de functie 'lijst_keuze'.

    Parameter:
    huidige_lijst (dict): de uitgavenlijst van de gekozen categorie.

    Returns:
    huidige_lijst (dict): de bijgewerkte uitgavenlijst met eventuele toevoegingen
    of verwijderingen.
    """
    while True:
        actie = int(
            input(
                "\nWil je een uitgave toevoegen of verwijderen?\n"
                "Kies 1 voor toevoegen, 2 voor verwijderen of 3 voor overslaan: "
            )
        )

        if actie == 1:
            print("\nUitgave toevoegen gekozen.\n")
            naam_uitgave = input(
                "Wat is de naam van de uitgave die je wilt toevoegen? \n"
            ).title()

            while True:
                try:
                    bedrag_uitgave = int(
                        input(
                            "Wat is het bedrag van de uitgave die je wilt toevoegen?"
                            " LET OP: rond het bedrag af naar een rond bedrag zonder komma's: \n"
                        )
                    )
                except ValueError:
                    print("Ongeldige invoer. Voer een afgerond getal in.\n")
                    continue
                else:
                    break
            nieuwe_uitgave_toevoegen(
                huidige_lijst,
                {naam_uitgave: {"bedrag": bedrag_uitgave, "betaald": False}},
            )
            print(
                f"De maandelijkse uitgave {naam_uitgave} met bedrag €{bedrag_uitgave} is toegevoegd aan de uitgaven lijst.\n"
            )

        elif actie == 2:
            print("\nUitgave verwijderen gekozen.")

            while True:
                naam_uitgave = (
                    input(
                        "\nWat is de naam van de uitgave die je wilt verwijderen?: \n"
                    )
                    .strip()
                    .title()
                )

                if not naam_uitgave.isalpha():
                    print(
                        "Voer een woord in, dus geen getallen. Probeer het opnieuw.\n"
                    )
                    continue

                if naam_uitgave in huidige_lijst:
                    uitgave_verwijderen(huidige_lijst, naam_uitgave)
                    print(
                        f"De maandelijkse uitgave {naam_uitgave} is succesvol verwijderd.\n"
                    )
                    break
                else:
                    print(
                        "Deze uitgave bestaat niet in de lijst. Probeer het opnieuw.\n"
                    )
                    continue

        elif actie == 3:
            print("\nGeen uitgave toevoegen gekozen.\n")
            break
        else:
            print("Incorrecte invoer. Probeer het opnieuw.\n")
            continue

    return huidige_lijst


def get_default_uitgaven():
    """
    Geeft een overzicht van alle standaard maandelijkse uitgaven.
    Deze waarden worden gebruikt wanneer er geen JSON-bestand geladen kan worden.

    Returns:
        dict: Main-dictionary met drie categorieën van uitgaven:
            - "persoonlijk": persoonlijke uitgaven
            - "overig": overige uitgaven
            - "zakelijk": zakelijke uitgaven

        Elke uitgave bevat:
            bedrag (int): het maandbedrag
            betaald (bool | None): betaalstatus
    """
    persoonlijke_uitgaven_lijst = {
        "Vodafone": {"bedrag": 54, "betaald": False},
        "iCloud": {"bedrag": 1, "betaald": False},
        "Schenken": {"bedrag": 25, "betaald": False},
        "Zorgverzekering": {"bedrag": 162, "betaald": False},
        "Spotify": {"bedrag": 13, "betaald": False},
        "Ziggo": {"bedrag": 64, "betaald": False},
        "ING": {"bedrag": 4, "betaald": False},
        "F1TV": {"bedrag": 12, "betaald": False},
        "Chatgpt": {"bedrag": 8, "betaald": False},
        "Fitness": {"bedrag": 46, "betaald": False},
        "Parkeren": {"bedrag": 25, "betaald": True},
        "Autoverzekering": {"bedrag": 91, "betaald": False},
        "Wegenbelasting": {"bedrag": 19, "betaald": False},
    }

    overige_uitgaven_lijst = {
        "Boodschappen": {"bedrag": 250, "betaald": None},
        "Benzine": {"bedrag": 100, "betaald": None},
    }

    zakelijke_uitgaven_lijst = {
        "Accountant": {"bedrag": 121, "betaald": False},
        "Microsoft": {"bedrag": 6, "betaald": False},
    }

    # Return de volledige hoofd-dictionary
    alle_uitgaven = {
        "persoonlijk": persoonlijke_uitgaven_lijst,
        "overig": overige_uitgaven_lijst,
        "zakelijk": zakelijke_uitgaven_lijst,
    }

    return alle_uitgaven
