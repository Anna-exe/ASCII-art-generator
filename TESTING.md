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

## **Unfixed Bugs**