# ProjectExam_Bdd
Testare site (https://www.saucedemo.com/)

Proiectul are ca scop testarea funcționalității și comportamentului site-ului "saucedemo" prin metoda BDD. Scenariile sunt descrise printr-un limbaj simplu de înțeles folosind sintaxa Gherkin.

Cerințe preliminare:

Instalare Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
Instalare Python: https://www.python.org/downloads/
Instalare Browser Chrome: testele sunt concepute pentru a rula în Chrome.
Instalare:

Clonare repository prin introducere comandă în Git Bash: git clone [https://github.com/AndreeaPopa9/ExamProject_BDD](https://github.com/LucianoFlorea/ProjectExam_Bdd.git).
Instalare librăria Selenium prin introducere în terminal a comenzii: pip install selenium sau sau pip install -U selenium (pentru update la zi)
Instalare WebDriver prin introducere în terminal a comenzii: pip install webdriver-manager
Instalare librăria Behave prin introducere în terminal a comenzii: pip install behave
Pentru a genera rapoarte BDD se introduce următoarea comandă în terminal: pip install behave-html-formatter

Rulare:
Rularea completă a testelor se realizează prin introducere în terminal a comenzii: -behave
Rularea unui singur test se realizează prin introducerea în terminal a comenzii: -behave -i urmată de fișierul feature dorit -> -behave -i signin.feature
Rularea unui tag dintr-un test se realizează prin introducerea în terminal a comenzii: -behave --tags=nume_tag

Generare rapoarte:
Pentru toate testele se folosește comanda: behave -f html -o behave-report.html
Pentru un anumit test se folosește comanda: behave -f html -o behave-report.html -i urmată de fișierul feature dorit
Pentru un anumit tag se folosește comanda: behave -f html -o behave-report.html --tags=nume_tag
Accesare rapoarte:

Click pe fișierul behave-report.html
Click pe icon-ul din dreapta a paginii pentru a se deschide în browser-ul dorit sau pe icon-ul Python pentru a se deschide în Python
