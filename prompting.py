class Prompt:
    # constructor method including all prompt parameter with default values
    def __init__(
        self,
        cv: str,
        job_adv: str,
        salary_expt="",
        language="en",
        availability="immediately",
        hours="full-time",
        max_length=350,
    ):
        self.cv = cv
        self.job_adv = job_adv
        self.salary_expt = salary_expt
        self.language = language
        self.availability = availability
        self.hours = hours
        self.max_length = max_length


class LetterPrompt(Prompt):
    # application counter
    application_counter = 0

    def __init__(
        self,
        cv: str,
        job_adv: str,
        salary_expt="",
        language="en",
        availability="immediately",
        hours="full-time",
        max_length=350,
    ):
        super().__init__(
            cv,
            job_adv,
            salary_expt,
            language,
            availability="immediately",
            hours="full-time",
            max_length=350,
        )
        LetterPrompt.application_counter += 1

    def write_application_letter(self):
        if self.language == "en":
            return f"""Compile application letter for {self.job_adv}, based on this CV: {self.cv}. 
                    Include information on {self.hours}, salaryexpecatations{self.salary_expt}, availability:{self.availability}.
                    The letter should not be longer than {self.max_length} words."""
        if self.language == "de":
            return f"""Entwerfe ein Anschreiben für den Job {self.job_adv}, basierend auf diesem CV {self.cv}.
                    Die folgenden Information müssen enthalten sein: {self.hours},Gehaltsvorstellungen:{self.salary_expt},Verfügbarkeit:{self.availability}.
                    Das Anschreiben sollte nicht länger als {self.max_length} Wörter sein."""


class CheatSheetPrompt(Prompt):
    def __init__(self, job_adv, language="en"):
        super().__init__(job_adv, language)

    def write_cheat_sheet(self):
        if self.language == "en":
            return f"Compile a cheatsheet for a job interview for this job {self.job_adv}. Include information on the company and average salaries."
        if self.language == "de":
            return f"""Stelle einen Spickzettel für ein Bewerbungsgespräche für diese Stelle zusammen {self.job_adv},
            der relevante Informationen zum Unternehmen, zur Branche und zu den Gehältern in der Branche enthält."""


class CvPointersPrompt(Prompt):
    def __init__(self, job_adv, cv, language="en"):
        super().__init__(job_adv, cv, language="en")

    def write_cv_pointers(self):
        if self.language == "en":
            return f"Based on {self.job_adv} point out if anything could be improved on {self.cv}."
        if self.language == "de":
            return f"""Mache Verbesserungsvorschläge für den CV {self.cv} basierend auf der Stellenausschreibung {self.job_adv}."""


# Test without AI link
if __name__ == "__main__":
    letter = LetterPrompt(
        cv="I was a farmer for 20 years", job_adv="Farmhand", salary_expt=20000
    )

    print(letter.write_application_letter())
    print(letter.application_counter)

    cheat_sheet = CheatSheetPrompt("farmhand")

    print(cheat_sheet.write_cheat_sheet())

    cv_pointers = CvPointersPrompt(
        language="en", job_adv="farmhand", cv="worked on a farm"
    )

    print(cv_pointers.write_cv_pointers())
