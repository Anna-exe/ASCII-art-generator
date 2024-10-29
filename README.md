![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# ASCII art generator

This ASCII text art generator is a simple tool designed to transform standard text into intricate ASCII art representations. Users can easily input their desired text and select from a variety of styles, allowing for customization and creativity. The generator is user-friendly, making it accessible for both beginners and experienced artists. Ideal for enhancing digital communications, social media posts, or personal projects, this tool brings a unique artistic flair to any text-based content.

[View the live project here](https://ascii-art-generator-efa6a1fc5e98.herokuapp.com/)

## Table of contents
* [**User Experience**](#user-experience)
* [**Features**](#features)
* [**Future Enhancements**](#future-enhancements)
* [**Testing Phase**](#testing-phase)
* [**Deployment**](#deployment)
* [**Credits**](#credits)
* [**Forking the GitHub Repository**](#forking-the-gitHub-repository)
* [**Local Clone**](#local-clone)

### User experience
* Website goal:
    - Create an ASCII text art generator that offers a tool that can add visual, digital-style appeal to practical applications, business or design needs.

* Target audiences:
    - Individuals interested in creative digital expressions, including ASCII and text-based art, who want to generate custom designs for online art projects, websites, and social media posts.
    - Developers and Programmers:
        - People looking for fun or retro-style visuals for use in CLI tools, terminal banners, or readme files on GitHub to add a unique touch to their projects.

    - Social Media Enthusiasts:
        - Users who want eye-catching headers, posts, or signature blocks in forums, chat platforms, and social media profiles for added personality and flair.
    
    - Bloggers and Content Creators:
        - Writers and bloggers seeking creative visual elements for blog posts, newsletters, or personal branding to make their content more engaging and memorable.

    - Teachers and Educators:
        - Educators who can use ASCII art in educational resources, coding lessons, or tutorials, especially in introducing text-based art to students in programming or design.
    - Marketing Professionals:
        - Marketing teams looking for unique, low-cost ways to create memorable visual assets for email footers, promotional banners, or digital flyers.
    - Retro Enthusiasts and Gamers:
        - Fans of vintage aesthetics and retro gaming who enjoy recreating the feel of classic computer graphics or early digital culture art for use in online communities, game forums, and personal projects.
    - Hobbyists and DIY Creators:
        - Individuals who enjoy experimenting with text art in DIY projects, such as creating ASCII-inspired home décor, t-shirt designs, or printed art.

* As a user, I would expect:
    - Understanding what is the goal of the website from first seconds
    - Design that would please the eye
    - Understand what action is required from me
    - Easy to manipulate throughout the console
    - Receive a feedback messages on every input
    - Option to restart the generator and get a new transformed text

### Features
* Colored text
    - To increase the readability of console content I've implemented a color on text messages
    - The error messages are colored red so that user can understand that something is not right
    ![Screenshot of color feature](/assets/images/color-feature.jpg)

* Providing categories of font styles
    - Users can choose font from a list or it can be chosen randomly by the application
    ![Screenshot of categories choice feature](/assets/images/categories-feat.jpg)

* Desired text input
    - Ask for users desired text that will be transformed into ASCII art
    - Any characters are allowed, but if user input is empty, app will return an error message asking for valid input again
    ![Screenshot of desired text input feature](/assets/images/text-feat.jpg)

* Generated art
    - After users enter a valid input, their digital text art is generated in rainbow colors
    ![Screenshot of generated art feature](/assets/images/generated-art-feat.jpg)
    - I added a little feedback message that expresses a hope that users are happy with generated art

* Hint message
    - I implemented a hint message that explains to user how to paste the text art to other platforms so it doesn't distort.
    ![Screenshot of hint message](/assets/images/hint-msg.jpg)

* Choice to repeat the process or exit the console
    - Providing choice to users if they want to repeat the process or they are happy to exit the console
    - If user input is anything but "y" - provide a goodbye message. Otherwise, the app will start from the beginning.
    ![Screenshot of last feature](/assets/images/goodbye-msg.jpg)

### Future enhancements

* I would like to implement feature that allows user to choose the color of text art

* Also, for some users the slowly printing messages might be annoying, so to speed up the process, I would like user to have an option to press the "Enter" key or mouse button that will stop slow-print function and display the printed message fully.

* To make a digital art from uploaded pictures

### Testing phase
* Please find all details in [Testing page](/TESTING.md)