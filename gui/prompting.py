from abc import ABC, abstractmethod


class PromptMixin(ABC):
    # constructor method including all prompt parameter with default values
    def __init__(self, job_adv: str, language: str):
        self.job_adv = job_adv
        self.language = language


    @abstractmethod
    def prompt(self):
        pass


class LetterPrompt(PromptMixin):
    # application counter
    application_counter = 0

    def __init__(
        self,
        cv: str,
        job_adv: str,
        salary_expt,
        availability,
        hours,
        max_length,
        language
    ):
        super().__init__(job_adv, language)
        self.cv = cv
        self.salary_expt = salary_expt
        self.availability = availability
        self.hours = hours
        self.max_length = max_length

        LetterPrompt.application_counter += 1

    def prompt(self):
        if self.language == "en":
            return f"""Compile an application letter for the following job ad'{self.job_adv}', based on this CV '{self.cv}'. Include the information on {self.hours} working hours and the earliest possible start date {self.availability}.If given include the annual salary expecatation of {self.salary_expt} €, else call it "competitive". The letter should not be longer than {self.max_length} words."""
        if self.language == "de":
            return f"""Entwerfe ein Anschreiben für den Job {self.job_adv}, basierend auf diesem CV {self.cv}. Die folgenden Information müssen enthalten sein: {self.hours},Gehaltsvorstellungen (pro Jahr):{self.salary_expt},Verfügbarkeit:{self.availability}. Das Anschreiben sollte nicht länger als {self.max_length} Wörter sein."""


class CheatSheetPrompt(PromptMixin):
    def __init__(self, job_adv, language):
        super().__init__(job_adv, language)

    def prompt(self):
        if self.language == "en":
            return f"Compile a cheatsheet for a job interview for this job {self.job_adv}. Provide information on the company, relevant industry information and average salaries."
        if self.language == "de":
            return f"""Stelle einen Spickzettel für ein Bewerbungsgespräch für die folgende Stelle zusammen {self.job_adv}, der relevante Informationen zum Unternehmen, zur Branche und zu den Gehältern in der Branche für die Position enthält."""

    def follow_up(self):
        if self.language == "en":
            return f"Compile a cheatsheet for a job interview for the job mentioned. Include information on the company and average salaries."
        if self.language == "de":
            return f"""Stelle einen Spickzettel für ein Bewerbungsgespräch für die genannte Stelle mit relevanten Infos zum Unternehmen,zur Branche und zu Gehältern."""


class CvPointersPrompt(PromptMixin):
    def __init__(self, job_adv, language, cv):
        super().__init__(job_adv, language)
        self.cv = cv

    def prompt(self):
        if self.language == "en":
            return f"Based on this job ad: {self.job_adv}improve the CV {self.cv}."
        if self.language == "de":
            return f"""Mache Verbesserungsvorschläge für den CV {self.cv} basierend auf der Stellenausschreibung {self.job_adv}. Stelle sicher die relevanten Schlagwörter zu verwenden."""

    def follow_up(self):
        if self.language == "en":
            return f"Based on the previous information improve the CV. Make sure relevant Keywords are included."
        if self.language == "de":
            return f"""Mache Verbesserungsvorschläge für den Lebenslauf basierend auf den vorherigen Informationen. Stelle sicher dass relevante Schlagwörter verwendet werden."""

