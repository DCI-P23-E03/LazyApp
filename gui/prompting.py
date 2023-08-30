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
            return f"""Compile an application letter for the job ad'{self.job_adv}', based on this CV: '{self.cv}'. Include information on {self.hours} working hours, salaryexpecatations{self.salary_expt} and availability {self.availability}. The letter should not be longer than {self.max_length} words."""
        if self.language == "de":
            return f"""Entwerfe ein Anschreiben für den Job {self.job_adv}, basierend auf diesem CV {self.cv}. Die folgenden Information müssen enthalten sein: {self.hours},Gehaltsvorstellungen:{self.salary_expt},Verfügbarkeit:{self.availability}. Das Anschreiben sollte nicht länger als {self.max_length} Wörter sein."""


class CheatSheetPrompt(PromptMixin):
    def __init__(self, job_adv, language):
        super().__init__(job_adv, language)

    def prompt(self):
        if self.language == "en":
            return f"Compile a cheatsheet for a job interview for this job {self.job_adv}. Include information on the company and average salaries."
        if self.language == "de":
            return f"""Stelle einen Spickzettel für ein Bewerbungsgespräche für diese Stelle zusammen {self.job_adv}, der relevante Informationen zum Unternehmen, zur Branche und zu den Gehältern in der Branche enthält."""

    def cheat_sheet_followup(self):
        if self.language == "en":
            return f"Compile a cheatsheet for a job interview for the job. Include information on the company and average salaries."
        if self.language == "de":
            return f"""Stelle einen Spickzettel für ein Bewerbungsgespräch für diese Stelle mit relevanten Infos zum Unternehmen,zur Branche und zu Gehältern."""


class CvPointersPrompt(PromptMixin):
    def __init__(self, job_adv, language, cv):
        super().__init__(job_adv, language)
        self.cv = cv

    def prompt(self):
        if self.language == "en":
            return f"Based on {self.job_adv} point out if anything could be improved on {self.cv}."
        if self.language == "de":
            return f"""Mache Verbesserungsvorschläge für den CV {self.cv} basierend auf der Stellenausschreibung {self.job_adv}."""

    def cv_pointers_followup(self):
        if self.language == "en":
            return f"Based on the previous point out what could be improved on the CV."
        if self.language == "de":
            return f"""Mache Verbesserungsvorschläge für den Lebenslauf basierend auf den vorherigen Infos."""

