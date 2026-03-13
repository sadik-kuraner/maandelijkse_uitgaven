import json

from functions import (
    keuze_uitgaven_gebruiker,
    lijst_keuze,
    uitgave_toevoegen_verwijderen,
    bestand_opslaan,
    bestand_laden,
    get_default_uitgaven,
)


def main():

    # Probeer het JSON bestand in te lezen
    try:
        maandelijkse_uitgaven = bestand_laden("maandelijkse_uitgaven_overzicht.json")
    except FileNotFoundError:
        print("Er bestaat nog geen bestand met data")
        maandelijkse_uitgaven = None
    except json.JSONDecodeError:
        print("De data is ongeldig")
        maandelijkse_uitgaven = None

    # Als er geen geldig bestand is, gebruik default hardcoded lijsten.
    if maandelijkse_uitgaven is None:
        maandelijkse_uitgaven = get_default_uitgaven()

    # Als het bestand succesvol geladen is, gebruik je ingelezen lijsten
    persoonlijke_uitgaven_lijst = maandelijkse_uitgaven["persoonlijk"]
    overige_uitgaven_lijst = maandelijkse_uitgaven["overig"]
    zakelijke_uitgaven_lijst = maandelijkse_uitgaven["zakelijk"]

    print("--- Maandelijkse Uitgaven ---\n\nWelkom bij de Maandelijkse Uitgaven app!\n")

    # Vraag gebruiker welke categorie hij/zij wil aanpassen
    gekozen = keuze_uitgaven_gebruiker(
        persoonlijke_uitgaven_lijst, zakelijke_uitgaven_lijst, overige_uitgaven_lijst
    )

    # Haal de juiste lijst op op basis van de keuze van gebruiker
    huidige_lijst = lijst_keuze(
        gekozen,
        persoonlijke_uitgaven_lijst,
        zakelijke_uitgaven_lijst,
        overige_uitgaven_lijst,
    )

    # Voeg uitgave toe of verwijder uitgave, afhankelijk van keuze van gebruiker
    huidige_lijst = uitgave_toevoegen_verwijderen(huidige_lijst)

    # Sla het bestand veilig op
    bestand_opslaan(maandelijkse_uitgaven, "maandelijkse_uitgaven_overzicht.json")


if __name__ == "__main__":
    main()
