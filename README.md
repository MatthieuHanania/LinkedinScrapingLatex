# LinkedinScrapingLatex
This tool extracts experience data from a LinkedIn profile and saves it as a LaTeX file.

## Setup
- This tool relies on the Firefox web driver. Ensure `geckodriver.exe` is placed in the project folder before executing the script. It can be downloaded [here](https://github.com/mozilla/geckodriver/releases).
- Install the dependencies with:
  ```pip install requirements.txt```
- Specify the names of the users whose experience you wish to extract in the `LinkedInUsersNames.json` configuration file as follows:
  ```json
  "user_ids": {"Matthieu": "matthieu-hanania-6835ba177", ...}


## Execution
To execute the tool, run:
```python
python Linkedin_scraping_Latex.py
```
You will then be prompted in the console to enter your LinkedIn username and password:
```
Please enter your LinkedIn email: test@mail.com
Please enter your LinkedIn password: password
```

## Output
The output is a LaTeX file containing the experience data of the specified LinkedIn users:
```
documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{enumitem}
\begin{document}
\section*{NAME}
\begin{itemize}
    \item LAST JOB TITLE
    \item COMPANY
    \item JOB DURATION
    \item LOCATION
\end{itemize}

```




