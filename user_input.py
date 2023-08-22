def userinput():
    # text snippets to re-use
    valid_choice = "Please make a valid choice."
    auswahl = "Bitte wähle eine gültige Optionen."

    salary_expt = ""  # empty until input from webscraping on glassdoor?

    # First User Choice
    language = input(
        "Please pick a language. Press 'Enter' for english and type 'd' for deutsch. "
    )

    if language == "":
        language = "en"
        # request full or part-time
        hours = input("Enter 'p' for Part-Time or press 'Enter' for 'Full-Time'")
        if hours == "":
            hours = "full-time"
        elif hours.lower() == "p":
            hours = "part-time"
        else:
            print(valid_choice)

        # input on availability
        availability = input(
            """When are you available to start your new challenge?\nEnter a start date or press 'Enter' for immediately. """
        )
        if not availability:
            availability = "immediately"  # change to immediately if no value is given, otherwise take string entered by user - calender/dropdown in tkinter?

        # input on letter length
        max_length = input(
            """How many words should the application letter have at a maximum?\nEnter a number between 250 and 400.\nPress 'Enter' to go with the recommended 350 words."""
        )
        if max_length:
            max_length = int(max_length)
        else:
            max_length = 350

        # copy and past the job ad unless webscraping, then copy, paste link
        job_adv = input("Copy and paste the job ad. ")

        # salary expectation
        salary_expt = input(
            """ How much would you like to earn?\nEnter a range, press 's' if you want a suggestion or 'Enter' to skip."""
        )
        if salary_expt.lower() == "s":
            salary_expt = ""  # empty until webscraping from glassdoor is finished

        # German language option
    elif language.lower() == "d":
        language = "de"
        hours = input("Drücke 't' für Teilzeit oder 'Enter' für 'Vollzeit'")
        if hours == "":
            hours = "Vollzeit"
        elif hours.lower() == "t":
            hours = "Teilzeit"
        else:
            print(auswahl)

        # input on availability
        availability = input(
            """Wann kannst du frühstens im neuen Job durchstarten?\nGebe ein Datum ein oder drücke 'Enter' für sofort. """
        )
        if not availability:
            availability = "sofort"  # change to immediately if no value is given, otherwise take string entered by user - calender/dropdown in tkinter?

        # input on letter length
        max_length = input(
            """Wie lang soll das Anschreiben maximal sein?\nWähle eine Zahl zwischen 200 und 400.\nDrücke 'Enter' für die empholenen 350 Wörter."""
        )
        if max_length:
            max_length = int(max_length)
        else:
            max_length = 350

        # copy and past the job ad unless webscraping, then copy, paste link
        job_adv = input("Füge hier die Stellenanzeige ein. ")

        # salary expectation
        salary_expt = input(
            """ Was sind deine Gehaltvorstellungen?\nGebe eine Zahl ein, drücke 'v' für einen Vorschlag oder \n'Enter', wenn du keine Angaben dazu machen möchtest. """
        )
        if salary_expt.lower() == "v" or not salary_expt:
            salary_expt = ""  # empty until webscraping from glassdoor is finished
        
    else:
        print(valid_choice)

    return [job_adv, salary_expt, language, availability, hours, max_length]


if __name__ == "__main__":
    print(userinput())
