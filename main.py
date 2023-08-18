from prompting import LetterPrompt, CheatSheetPrompt, CvPointersPrompt
from user_input import userinput
from PDFquery import *
from ai_response_modified import ChatGPTCompletion
from ai_example2_Class import ChatGPTChat
from stringcolor import *




if __name__== "__main__":

    cv = text
    # contruct Prompt with given information, function userinput returning all necessary variables
    job_adv, salary_expt, language, availability, hours, max_length = userinput()
    print(language)
    # instantiate Prompt classes
    letter = LetterPrompt(cv, job_adv, salary_expt, language, availability, hours, max_length)

    #cheat_prompt = CheatSheetPrompt(job_adv, language)

    #cv_pointers = CvPointersPrompt(job_adv, cv, language)

    prompt = letter.write_application_letter()

    print(prompt)
    # enable AI    
    completion = ChatGPTCompletion()

    #completion.chat_interface(prompt)
    #chat = ChatGPTChat()




