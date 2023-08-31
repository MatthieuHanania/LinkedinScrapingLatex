#####
# THIS PROGRAM WILL EXTRACT EXPERIENCE DATA OF SPECIFIED USER FROM LINKEDIN AND SAVE THEM INTO A LATEX FILE
####
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import time
import random

class LinkedInToLatex:

    def __init__(self) -> None:
        self.driver = webdriver.Firefox() #with the version 4.11.2, no needs to specify the path of firefox
        self.driver.get("https://www.linkedin.com")

        self.user_to_extract = {}

        #ask the user for the credentials
        self.EMAIL = input("Please enter your linkedin email : ")
        self.PASSWORD = input("Please enter your linkedin password : ")


    def read_config(self,filename):
        """Read the configuration file"""

        with open(filename, 'r') as f:
            config = json.load(f)
            self.user_to_extract = config["user_ids"]
        return True


    def wait_until_element_displayed(self,by,element):
        try:
            WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located((by, element)))
            time.sleep(random.randint(2,3))
        except:
            pass
    

    def login(self):    
        """Login to Linkedin"""
        
        print("login")
        self.wait_until_element_displayed(By.ID,"session_key")

        self.driver.find_element(By.ID, "session_key").send_keys(self.EMAIL)
        password = self.driver.find_element(By.ID, "session_password")
        
        password.send_keys(self.PASSWORD)

        time.sleep(random.randint(1,2))
        password.send_keys(Keys.RETURN)

        print("wait for the home page")
        self.wait_until_element_displayed(By.ID,"voyager-feed")
        print("home page printed")

        time.sleep(random.randint(3,5))



    def get_experiences(self):
        """Get the experiences of specified users"""

        baseUrl = "https://www.linkedin.com/in/user_id/details/experience/"

        self.user_experiences = {}
        for user,user_id in self.user_to_extract.items():

            self.driver.get(baseUrl.replace("user_id",user_id))

            print("start wait")
            self.wait_until_element_displayed(By.CLASS_NAME,"scaffold-finite-scroll__content")
            print("finish wait")
            
            experiences = self.driver.find_elements(By.CLASS_NAME,"pvs-entity")

            self.user_experiences[user]=[]
            for experience in experiences:
                self.user_experiences[user].append(experience.text.split("\n")[::2][:4])
            
            time.sleep(random.randint(3,5))

    def save_to_latex(self, filename):
        """Save Data to latex"""

        with open(filename, 'w') as f:
            # Écrire l'en-tête du document
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage[utf8]{inputenc}\n")
            f.write("\\usepackage[T1]{fontenc}\n")
            f.write("\\usepackage{enumitem}\n")
            f.write("\\begin{document}\n")

            # Écrire les données
            for name, experiences in self.user_experiences.items():
                f.write("\\section*{%s}\n" % name)
                for exp in experiences:
                    f.write("\\begin{itemize}\n")
                    for detail in exp:
                        f.write("    \\item %s\n" % detail)
                    f.write("\\end{itemize}\n")
                    f.write("\\vspace{1em}\n")

            # Fin du document
            f.write("\\end{document}\n")

    def run(self):

        #read the config file to get the users 
        self.read_config("LinkedInUsersNames.json")

        #Login to linkedin
        self.login()

        #Get the profiles
        self.get_experiences()

        #Save data to latex
        self.save_to_latex("output.tex")



if __name__ == "__main__":
    bot = LinkedInToLatex()
    bot.run()
    