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
    - My functions were commented with an inline comments. Fixed the the errors by changing inline comments into docstrings

- Error: *Line too long*
    - The hint message was too long, so I wrapped it into multiline string.
    ![Screenshot of multiline string result](/assets/images/identation-issue.jpg)
    After that, the hint message printed with identation, but I found out that it can be fixed just by removing any identation from a multiline string up to the very beginning of line in code.

- Error: *Function already defined*
    - removed the duplicate of slow_print() function

- Error: *Too general exeption*
    - Replaced "break" with sys.exit() function

- Error: *standard import "random" should be placed before third party import "pyfiglet"*
    - Reordered import of libraries

- Error: *Unused Style imported from colorama*
    - Removed an unused "style" module
## **Unfixed Bugs**