# Testing Page Table of Contents
* [**During Development Testing**](#during-development-testing)
    * [Manual Testing](#manual-testing)
    * [Bugs and Fixes](#bugs-and-fixes)
* [**Post Development Testing**](#post-development-testing)
  * [**Validators**](#validators)
      * [HTML](#html)
      * [CSS](#css)
      * [JavaScript](#JS)
  * [**Lighthouse Scores**](#lighthouse-scores)
  * [**Accessability**](#accessability)
  * [**Unfixed Bug**](#unfixed-bug)


## **During Development Testing**
During the development process, I was manually testing in the following ways:-

1. Manually testing each function by running it in Github workspace with
```Bash
python3 run.py
```
    
2. Published the page via GitHub pages and shared with my friends.

### **Manual Testing:**
* During testing, I used four different browsers to ensure cross-compatibility. The desktop browsers used by myself were:

  1. Chrome
  2. Firefox  
  3. Opera
  4. Edge

* I then used the devtools to simulate different screen sizes from 280px up to 1920px in width. 
* In addition to this, I also tested it on my smartphone.

### **Bugs and Fixes:**

* No bugs found during development


## **Post Development Testing**

### **Validators**

#### **HTML** - https://validator.w3.org/nu/

* No errors found

![HTML validator](/assets/images/readme-images/html-val.png)


#### **CSS** - https://jigsaw.w3.org/css-validator/

* No errors found

![CSS validator](/assets/images/readme-images/css-val.png)


#### **JS** - https://jshint.com//
* Few missing semicolons, fixed
* One undefined variable on line 28 "game", fixed it by moving variable definition to global scope


### **Accessability**
* [Web accessibility evaluation tool](https://wave.webaim.org/) returned no errors

![Wave accessibility](/assets/images/readme-images/accessability.png)

### **Lighthouse Scores**
* I did all lighthouse tests in incognito mode to avoid interference from browser extensions. 
* I ran the tests for both mobile and desktop. 
- No errors found
- Got performance scores of 60-69 with the main issue being **Largest Contentful Paint element 13,430 ms**

![Desktop lighthouse](/assets/images/readme-images/lighthouse.png)
![Mobile lighthouse](/assets/images/readme-images/lighthouse-mobile.png)

  - Asked help on slack
  
  - Resolved desktop score by changing card image sources to local files with smaller sizes
  ![Desktop lighthouse after](/assets/images/readme-images/desktop-after.jpg)

  - But score on mobile devices is only 70, unfortunately don't have time to look into that
  ![Mobile lighthouse after](/assets/images/readme-images/mobile-after.jpg)

### **Unfixed bugs**

- When doing a hard refresh, the user can see the face of cards for a short moment, it could be resolved by following the performance issue advice from lighthouse.
- To resolve performance issues I could display all card images in an HTML page, but this project was specifically JavaScript, so with the advice of my mentor and slack community, I displayed images with help of JS array.


[return to README.md](README.md)