from prompting import Prompt
import PDFquery

valid_choice = "Please make a valid choice."

language = input("Please pick a language. Enter 1 for english and 2 for deutsch.")
if language == "1":
        language = "en"
elif language == "2":
        language = "de"
else:
        print(valid_choice)
cv = PDFquery.text

hours = input ("Enter 'p' for Part-Time or press 'Enter' for 'Full-Time'")
if hours == "":
        hours = "full-time"
elif hours == "p":
        hours = "part-time"
else:
        print(valid_choice)

max_length = input ("How long should the letter be? Enter a number between 250 and 400 words. (350 is the default value)")





availability

        self.hours = hours
        self.max_length = max_length
        self.cv = cv
        self.job_adv = job_adv
        self.salary_expt = salary_expt
        Prompt.application_counter +=1