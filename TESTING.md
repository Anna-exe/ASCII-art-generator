# Testing Page Table of Contents
* [**During Development Testing**](#during-development-testing)
    * [Manual Testing](#manual-testing)
    * [Bugs and Fixes](#bugs-and-fixes)
* [**Post Development Testing**](#post-development-testing)

* [**Unfixed Bugs**](#unfixed-bugs)


## **During Development Testing**
During the development process, I was manually testing in the following ways:

### **Manual testing**
Manually testing each function by running it in Github workspace with
```Bash
python3 run.py
```

### **Bugs and fixes**

- I was struggling to set up the project on Heroku's platform
    - Reached out to Google, Slack, and Copilot AI
    - Watched the Love Sanwiches example project throughout to find all the required steps
    - Reached out to online tutoring

Eventually, I realised that I didn't installed the Config Variables in Heroku's settings
![Screenshot of Config Vars](/assets/images/config-vars.jpg)

Also, my requirements.txt file contents had to be secured with command:
```Bash
pip freeze > requirements.txt
```

## **Post Development Testing**
### PEP8 Code Validation
The PEP8 style guide was used to check the code for any formatting errors or issues. The code was tested using the [PEP8CI tool](https://pep8ci.herokuapp.com/#) to ensure it follows Python's best practices.
No major errors found in PEP8 validator:
![Screenshot of PEP8 result](/assets/images/p8-report.jpg)

### Pylint rating
To check my codes score with pylint validator, I ran a command:
```Bash
pylint run.py
```
Which gave me a result of 7.18 out of  10
![Screenshot of pylint score](/assets/images/pylint-report1.jpg)

- Error: *Missing module docstring*
    - My functions were commented with inline comments. Fixed the the errors by changing inline comments into docstrings

- Error: *Line too long*
    - The hint message was too long, so I wrapped it into a multiline string.
    ![Screenshot of multiline string result](/assets/images/identation-issue.jpg)
    After that, the hint message printed with indentation, but I found out that it can be fixed just by removing any indentation from a multiline string up to the very beginning of line in code.

- Error: *Function already defined*
    - removed the duplicate of slow_print() function

- Error: *Too general exeption*
    - Replaced "break" with sys.exit() function

- Error: *standard import "random" should be placed before third party import "pyfiglet"*
    - Reordered import of libraries

- Error: *Unused Style imported from colorama*
    - Removed an unused "style" module

- Error: *C0114: Missing module docstring*
    - The error wasn't related to line 114, but to the whole code.
    Fixed error by adding a descriptive docstring at the beginning of python code about all modules and functions.

- Error: *run.py:155:15: W0718: Catching too general exception Exception*
    - Replaced too general "Exception" with more specific exception "TypeError"

After resolving all errors noted by pylint, my score now is 10/10

![Screenshot of pylint result 2](/assets/images/pylint-report2.jpg)

## **Unfixed Bugs**
- There is an issue if user is pressing the "Enter" key:

![Screenshot with unfixed bug](/assets/images/unfixed-bug.jpg)

    The print messages are returning on a new line, and, if pressed continuously, the app crashes and doesn't react at all.
    Might fix it by blocking the app from any input before messages are fully printed, but I am short of time now.