from prompting import *
import PDFquery

# text snippets to re-use
valid_choice = "Please make a valid choice."
auswahl = "Bitte wähle eine gültige Optionen."

cv = PDFquery.text
job_adv = "" # empty until input from webscraping is available
salary_expt = "" # empty until input from webscraping on glassdoor?

# First User Choice
language = input("Please pick a language. Press 'Enter' for english and type 'd' for deutsch. ")

if language == "":
        language = "en"
        # request full or part-time
        hours = input ("Enter 'p' for Part-Time or press 'Enter' for 'Full-Time'")
        if hours == "":
                hours = "full-time"
        elif hours == "p":
                hours = "part-time"
        else:
                print(valid_choice)
      
        # input on availability
        availability = input(
                """When are you available to start your new challenge?/n
                Enter a start date or press 'Enter' for immediately. """)
        if availability == "":
                availability = "immediately" # change to immediately if no value is given, otherwise take string entered by user - calender/dropdown in tkinter?

        # input on letter length

        max_length = input ("""How many words should the application letter have at a maximum? 
                            Enter a number between 250 and 400. 
                            Press 'Enter' to go with the recommended 350 words.""")
        if max_length:
                max_length = int(max_length)
        else:
                max_length = 350

        # salary expectation
        salary_expt = input (""" How much would you like to earn?
                             Enter a range, press 's' if you want a suggestion or 'Enter' to skip.""")
        if salary_expt == "s":
                salary_expectation = "" # empty until webscraping from glassdoor is finished
      
        # German language option
elif language == "d":
        language = "de"
        hours = input ("Drücke 't' für Teilzeit oder 'Enter' für 'Vollzeit'")
        if hours == "":
                hours = "Vollzeit"
        elif hours == "t":
                hours = "Teilzeit"
        else:
                print(auswahl)
        
        # input on availability
        availability = input(
                """Wann kannst du frühstens im neuen Job durchstarten?
                Gebe ein Datum ein oder drücke 'Enter' für sofort. """)
        if availability == "":
                availability = "sofort" # change to immediately if no value is given, otherwise take string entered by user - calender/dropdown in tkinter?
        
        #input on letter length

        max_length = input ("""Wie lang soll das Anschreiben maximal sein? 
                            Wähle eine Zahl zwischen 200 und 400. 
                            Drücke 'Enter' für die empholenen 350 Wörter.""")
        if max_length:
                max_length = int(max_length)
        else:
                max_length = 350
        
        # salary expectation
        salary_expt = input (""" Was sind deine Gehaltvorstellungen?
                             Gebe eine Zahl ein, drücke 'v' für einen Vorschlag oder 'Enter',
                             wenn du keine Angaben dazu machen möchtest. """)
        if salary_expt == "v":
                salary_expectation = "" # empty until webscraping from glassdoor is finished
else:
        print(valid_choice)
