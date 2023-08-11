from ai_example2_Class import ChatGPT

class Prompt:

    # application counter
    application_counter = 0
    #constructor method including all prompt parameter with some default values
    def __init__(self, language = "en", availability = "immediately", hours = "full-time", max_length = 350, cv, job_adv, salary_expt):
        self.language = language
        self.availability = availability
        self.hours = hours
        self.max_length = max_length
        self.cv = cv
        self.job_adv = job_adv
        self.salary_expt = salary_expt
        Prompt.application_counter +=1


    
    def write_application_letter(self):
        if self.language == "en":
            return f"""Compile application letter for {self.job_adv}, based on this CV {self.cv}. 
                    Include information on {self.hours},salaryexpecatations{self.salary_expt}, availability:{self.availability}. 
                    The letter should not be longer than {self.max_length} words."""
        if self.language == "de":
            return f"""Entwerfe ein Anschreiben für den Job {self.job_adv}, basierend auf diesem CV {self.cv}. 
                    Die folgenden Information müssen enthalten sein: {self.hours},Gehaltsvorstellungen:{self.salary_expt},Verfügbarkeit:{self.availability}. 
                    Das Anschreiben sollte nicht länger als {self.max_length} Wörter sein."""
    
    def write_cheat_sheet(self):
        if self.language == "en":
            return f"""Compile a cheatsheet for a job interview for this job {self.job_adv}.
                    Include information on the company and average salaries."""
        if self.language == "de":
            return f"""Stelle einen Spickzettel für ein Bewerbungsgespräche für diese Stelle zusammen {self.job_adv}, 
            der relevante Informationen zum Unternehmen, zur Branche und zu den Gehältern in der Branche enthält."""
    
    def write_cv_pointers(self):
        if self.language == "en":
            return f"Based on {self.job_adv} point out if anything could be improved on {self.cv}."
        if self.language == "de":
            return f"""Mache Verbesserungsvorschläge für den CV {self.cv} basierend auf der Stellenausschreibung {self.job_adv}."""



