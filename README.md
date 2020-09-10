<p align="center">
  <img width="100%" height="90%" src="https://github.com/jimbobding/Bar-Hop-Uk/blob/master/assets/images/Bar Hop UK Logo Guy.png">
</p>



## Table of Contents
1. [My Idea](#myidea)
    - [User Stories](#user-stories)
    - [What the user wants](#design)
    - [Wireframes](#wireframes)

2. [Design](#design)
    - [Fonts](#fonts)
    - [Colours](#colours)
    - [Logo](#logo)
    - [Wireframe](#wireframe)

4. [Technologies Used](#technologies-used)

5.  [Features](#features)
    - [Fonts](#fonts)
    - [Features to add](#features-to-add)
    - [User guidance](#user-guidance)

6.  [Testing](#testing)
    - [Devices used for testing](#devices-used-for-testing)
    - [Validators](#validators)
    - [Compatibility and Responsiveness](#compatibility-and-responsiveness)

7. [Deployment](#deployment)
    - [Clone](#lclone)
    - [Heroku Deployment](#heroku-deployment)

8. [Credits](#credits)
    - [Code](#code)
    - [Websites](#websites)
    - [Images](#images)
   

    - [Acknowledgements](#acknowledgements)


**Demo**
----------
A live demo can be found [here](https://8000-e35317c9-c729-49c7-bdd6-a14b63318364.ws-eu01.gitpod.io/)

# My Idea

I would like to design an application that allows users to create, read, edit and delete cocktail recipes. It would serve as cocktail library that allows anyone to read the recipes but only users who are signed up to the app would be able to add to the library, users would only be able to edit and/or delete their own cocktail entries.

1. This app would serve the user who likes to drink cocktails but do not know the recipes to allow them to make them at home. In the current climate of people not going out as much but still wanting to enjoy cocktails I the comfort of their home.
2. This App would also serve to hospitality staff as it would hold an ever-growing library of recipes they could call up =on if they cannot remember how something is mad. It would also serve as a place to house their own creations.


### User stories

Jake T, a bartender from Wales, UK - "I work in a cocktail bar and am constantly making cocktails for customers, I have a lot of recipes stored in my head but sometimes customers ask
                                      for cocktails, I don’t quite know how to make I generally google the wanted cocktail to find the recipe. I would love to be able to have an ever growing
                                      recipe book that I could consult for recipes and a place in which I can store my own creations"

Adam R, a financial consultant from Melbourne, Aus - "I enjoy the weekends where I can go out and enjoy cocktails and experience drinks that I am unable to drink at home. But sometimes I would like to
                                                      avoid the crowds and invite my friends around to my house for drinks or to host a cocktail party to honour an occasion. I would like
                                                      a database of drinks with the steps that allow me recreate tehm at home."


### What the user wants

1. The user wants to easily navigate across all areas of the app. Users will bore quickly if they can find their way around from the moment they start
   interaction with the app.
2. The user wants to be able to view cocktail recipes without having to register.
3. The user wants to be able to register an account and have the information stored safely.
4. The user wants to be able to login it their account ad see their own recipes stored in a user page.
5. The user wants to be able to edit and delete their own recipes.
6. The user wants to be able to view all aspects of a recipe e/g not only the ingredient but also the amounts of said ingredient.
7. The user wants to be able to log out quickly and have the session terminated.
8. The user wants to be able to view the app on multiple platforms.

 
# Design

I wanted the look of the app to be simplistic but have the vibe of a classy cocktail menu.

For the framework of the app I used [Materialize](https://materializecss.com/). choose this front-end design framework as it has an ease of use 
and a look of effortless simplicity. I used this for my nav-bar, cards, grid system, icons and colour schemes.
[jquery](https://jquery.com/) was used for functionality of some of the materialize elements.

### Fonts

The main fonts I settled on was [Slabo](("https://fonts.googleapis.com/css2?family=Slabo+27px:100,300,400,700&display=swap")) which was used for the main body 
of the app, I choose this as I wanted it to look stylish but still approachable easy to read but with character.
The other font I used was [Fredericka the Great]("https://fonts.googleapis.com/css?family=Fredericka+the+Great:100,300,400,700&display=swap"),
this was used on the cocktail headings to give a slightly classier look, in keeping with an old school cocktail menu heading.

### Colours

The main colour scheme was to be of white, black and red being the look of old school bartenders, White shirt with a black waistcoat and a red bow tie.
I also wanted to use colours that would signify the use of functionality to user’s red being danger green being success and blue being neutral.
[flatui colorpicker](http://www.flatuicolorpicker.com)
[Materialize Color](https://materializecss.com/color.html)

### 0e9594 - Blue Chill 
grey darken-4

Was used for both header and footer of the app. The main colour of the app as it opens and closes the index page.
 
### Logo

The logo was used in the nav-bar as a route back to the home page. The logo itself is the face of a bar tender with the site name underneath.
[Canva](https://www.canva.com/) to design the logos.


## Wireframe

For my wireframes I first used pen and paper to jot down my original thoughts and then once I had a clearer picture in my head of
how I wanted the app to look I used [Balsamiq](https://balsamiq.com/) to mock it up. The design did change from the pen and pad to Balsamiq
to actual coding as certain things did not look at good as I hoped, but overall it stayed pretty much the same.

 [wireframes]()

## Features
### Existing Features
#### Navbar   

The nav-bar will be on every page of the app.

The nav-bar is set at the top of the screen and holds the links for users to navigate easily across the site. I choose black as the colour as it was 
in keeping with the colour scheme I was going for giving slick stylish look. In the lef hand corner of the nav bar is the logo for the app which also serves
as link, back to the home page. If the app is viewed on mobile devices the menu condense into a hamburger menu that slides the links out from the left, Jquery is
used to activate this.

If a user is logged in the nav-bar offers the links 

1. Home - Takes the user to the home page.
2. Spirit Categories - Takes the user a page with cards that are used to separate the cocktails into the different alcohol sections.
3. Add-cocktails - Takes user to the add cocktail form.
4. Profile - Takes the user to their profile page which displays their user name and the cocktail they have created (if they have created any)
5. Logout - Logs the user out and takes them to login page.

If user is not logged in 

1. Home.
2. Login - Takes user to the login page where they can log in if they are already registered.
3. register - Takes user to the register page allowing them to create an account.

If user is logged in as Admin

1. Home.
2. Spirit Categories.
3. Add-cocktails.
4. Profile.
5. Manage Categories - Takes the user to the category page where they can add and edit the soem of the drop categories in the add cocktail form.
6. Logout.

#### Home page

The home page is the page the user is taken to when they first log in or register it is also available on th enavbar as page for users whod do not
wish to register. It contains a picture of a cocktail that has a call to action button which takes the user to - if they are logged in he add cocktail form,
if they are not logged in, the register form. The page also contains all of the cocktails that have been created on the site available for anyone to view.
The home page also has a search function that searches the drink collection in the database for words in the search either returning the relevant drinks or a message 
telling the user that no drinks match the search.

#### Spirit selection

The spirit selection is a page that queries all the cocktails in the database and separates them into their different alcohol categories. 

#### Add-cocktails

The add-cocktails page contains a form that is used to collect the input for cocktails in the databae. There are 6 required fields in the form.

1. The alcohol selection is the first field, this is a drop down that is connected to a collection within the data base. This is a required field and it separates 
the cocktails into the different.
2. Alcohol this is for the first ingredient in the cocktail. It is required as to make a cocktail you will at need at least one component.
3. Alcohol measure, this is for the measurement of the first alcoholic ingredient this is a required field as a measurement would be needed to make a cocktail. This will 
also take a numerical value as an input.
4. Measurement, this used to choose whatever type of measurement would be used e/g MLs or Ounces this again is required as you need a measurement quantity to create a cocktail. The measurement
is also a dropdown that is part of a collection with in the database I am using
5. Glassware again is mandatory as it is a physical aspect that is required in making a cocktail. Glassware is also a dropdown menu that is a collection part of the database, it 
contains a variety of Glassware that can be selected.
6. Method. Method is a required field as it a fundamental part of the process in making a cocktail.

The rest of the fields are all optional including the add an image section that allows you to add a url to a picture representing the cocktail created. If an image is not selected a placeholder
image will be used in its stead.

#### Drink card 

The drink card is how the cocktails are displayed in the relevant sections. They contain aan image of the cocktail as well as the name of the cocktail the spirit category and the user who created the cocktail.

#### Cocktail recipe

The cocktail image and name on the drink card are wrapped in an anchor that takes you to drinks recipe page, this page contains the rest of ingredients, the method, notes on the cocktail . The page also contains three buttons, the back button 
which takes the user back to the home page. Also, the delete and edit cocktail buttons which are only visible if the cocktail was created by the logged in user.

#### Edit cocktail 

The edit cocktail form is the same as the add cocktail form but all the fields that had been previously filled in by the user are pre-populated.
At the bottom of the for there are two buttons, edit cocktail which confirms the edit and brings the user back to the home page and cancel button which cancels any of the edits ad brings the user back to the home page.

#### Delete cocktail

The delete cocktail function removes the cocktail from the app as well as removing it from the data-base.

#### Register 

The register page asks the user to input a username and a password. The username and password has a minimum of 5 characters and a maximum of 15, it takes the any lower or uppercase letter and
any number between 0-9. The user will be notified by a flash message if the username is already taken, once the username and password have been entered a flash message will come notifying the user
that the registration was successful. The user is then added to the database.

#### Login

The login page takes the users username and password. If the password or username is incorrect a flash message will display saying that the username or password are incorrect (it will not identify which one is incorrect as an extra security measure).
If the username and password are found a flash message will display welcoming the user with their username and they will be directed to their profile page.

#### Logout

The log out function pops out the session user and redirects them to the login page

#### Profile

The profile page has a card displaying the logged in users name and also displays all the cocktails created by the user.

#### Add Categories

This page is only open to admin users it allows the user to add extra categories to the dropdown function as well as editing and deleting existing ones. The top of the page contains a button labelled add category, this will take you to a card with an input field
that allows you to type in the name of the category you wish to add and a button to confirm the addition, the user will be taken back to the mange categories section whit a flash message displaying that the selected category has been added.
The user would click on the manage categories section which would take the user the mange categories page. On a materialize carousel the categories are displayed, if the user cick on one it will open up giving you two buttons Edit and Delete.
Delete will remove the category from the dropdowns and database and displayed a message your category has been deleted, edit will take you to a separate card that will have two buttons and an input box that allows the user to change the name of the category.
After the user has changed the name in the input box they can either click edit which will take them back to the manage categories page with a flash displaying that your category has been successfully edited, or you can click cancel which will cancel the operation and take you back to the manage categories section.


### Features to add

There are features I would like to Implement in to the app in the future.  have not yet put these features into place due to time constraints and also some of them 
would be beneficial with a bigger base of users.

#### Change password / username

I would like to implement a functiom that allows users to be able to change thier password and or username. This would be beneficial for users in the event they thought their security had been comprimised, also if they had made
a mistake and either the password or username had become and inconvenience.

#### A like system

I would like a like sysytem where users could express thier like in  particular cocktail. This data could be collected and used top promote certain products to users or suggest other
similar cocktails that they may like.

#### Favourites

This would be used in conjunction in the like system it would collect all the users favourite cocktails and store them for the user to view at any time they liked. 


## User guidance

### Register

1. Click the register link in the navigation bar.
2. Enter a chosen username. 
3. Enter a chosen password.
4. Click the register button. 
5. You will be taken to your new created profile page.
6. Alternatively choose the "Have an account login" link below the login if the user already has an account.

### Login

1. Click the login link in the navigation bar.
2. Enter your previously chosen username.
3. Enter your previously chosen password.
4. Click the register button. 
5. You will be taken to your profile page.
6. Alternatively choose the "If you don’t have account click here Register Here" link below the login if the user does not have an account.

### Login
1. Click the logout link in the navigation bar.
2. This will take you back to the login page.

### Add-cocktail

1. Click the add-cocktail link in the navigation bar.
2. You will be taken to the add cocktail form.
3. For the choose alcohol type choose the champion alcohol in your cocktail. This will be provided in a drop-down menu with a drop down arrow which when pressed will display the alcohol categories.
4. The remaining fields are to be selected as the user goes through the form. All dropdown menus will be displayed in the same way.
5. The measurement fields are integers and will only take numerical values.
6. Asterixed fields are mandatory.
7. To add a a url to the image filed of the form the user must choose the image they wish to use and copy the url for the image and then paste this in to the image filed.
8. Click on the add cocktail button on the bottom of the form.

### Edit-cocktail

1. Click on a cocktail that has been created by the logged in user.
2. Click on the edit button at the bottom of the cocktail recipe page.
3. All the fields of the cocktail form that have previously been filled when the cocktail was created will be populated by the values originally chosen.
4. Asterixed fields are mandatory.
5. To add a a url to the image filed of the form the user must choose the image they wish to use and copy the url for the image and then paste this in to the image filed.
6. Click on the edit cocktail button on the bottom of the form to apply the changes.
7. Alternatively click on the cancel button to cancel the changes and go back to drinks page.


## Technologies used

- [git-hub](https://github.com/) To Store my code
- [git-pod](https://www.gitpod.io/) Used as my IDE to work on my code
- [HTML5](https://en.wikipedia.org/wiki/HTML5) Used to build my project
- [Cascading-Style-Sheets](https://www.w3.org/Style/CSS/Overview.en.html) Used to style my project
- [Google-Fonts](https://fonts.google.com/) Used for the two types of text used throughout the project 
- [Font-awesome 5](https://fontawesome.com/) Used for icons used on the project 
- [Jquery](https://jquery.com/download/) Jquery used to simplify some of the code
- [Materialize](https://materializecss.com/) Used for the  framework of my project and also for the navigation bar, the cards (spirit selection, cocktail cards)



## Testing

For testing, I used the [goggle chrome development tools](https://developers.google.com/web/tools/chrome-devtools) to test the app on a
variety of screen sizes for Responsiveness, design and user experience. Although on chrome development tools, the app appeared to work across all
screen sizes on using my iPhone and iPad I found some problems.

For the actual task of testing, I went through each device and used all the functions on the app. This was to check out the aesthetics and functionality 
off the app.


## Testing 

I tested the functionality of the app throughout the entire development process and also had friends and family test it on various devices.



### Validators

- [The-W3c-Markup-Validation-Service](https://jigsaw.w3.org/css-validator/) - Validates/checks for mistakes CSS
- [The-W3c-Markup-Validation-Service](https://validator.w3.org/) - Validates/checks for mistakes HTML

### Code format

[freeformatter](https://www.freeformatter.com/css-beautifier.html) was used to format both CSS and HTML.

### Devices used for testing 
#### In google chrome dev tools

- Moto G4 
- Galaxy S5
- Pixel 2 
- Pixel 2 XL
- iPhone 5/SE  
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone x 
- iPad
- iPad Pro

#### My appliances

- MacBook pro 
- iPad
- iPhone

 #### Browswers 

 some of the browsers were tested on [Lambdatest](https://app.lambdatest.com/console/realtime) which allowed me to test in real-time across different browsers.

- Chrome
- Safari
- Internet explorer - windows 8.1 & 10
- firefox windows - windows 8.1
- Edge - Windows 10 
 
#### Problems

I had a problem with the measure fields taking numbers, which I wanted to do to minimalize mistakes when people are inputting data as thy would only be able to input numbers rather than text. 
Then sending them to the mongo database as string, so when they were returned they would not pre populate the fields in the edit cocktail form. To fix this problem I turned the string into integers in the app.route in bot the add-cocktails and the edit cocktail function <p>alcohol_measure': int(request.form.get('alcohol_measure'))</p> this seemed to work initially but 
then  relised that if the measure fields were left empty then it would send back an error. This could have been solved by using a number of if statements but after deliberating with the tutors I made the decision 
it would be less problematic to leave the fields as text field rather than overcomplicate the code with lengthy if statements.


## Deployment

### Heroku deployment

1. Login to my Heroko account.
2. Click on New at the right top corner and click on Create new app.
3. Choose App name and a region (Europe was the closest to me). Then click on Create app.
4. Go to terminal window and create requirements.txt by running command pip3 freeze --local > requirements.txt
5. Then create Procfile by running command echo web: python app.py > Procfile Remember P is capital
6. Add these files to staging area by running command git add requirements.txt & git add Procfile.
7. Then commit these file respectively by running command git commit -m "Added requirements.txt & git commit -m "Added Procfile.
8. Then push these files to github by running command git push
9. Go back to Heroku to your App and click on Deploy tab.
10. Then go to Deployment Method and click on Github Connect to Github.
11. Then make sure your Github Profile is displayed and add you repository name and click on Search.
12. Once it finds your repository then click on Connect.
13. Go to Settings at the top. Then click on Reveal Config Vars.
14. In Config Vars add IP with value 0.0.0.0 then add PORT as 5000 then add SECRET_KEY then add MONGO_URI and then add MONGO_DBNAME which is the name of database.
15. Go back to Deploy tab and click on Enable Automatic Deploys.
16. Click on Deploy Branch
17. It will take a minute and display a message that Your app was successfully deployed.
18. Click on View to launch your deployed app.

My website is now deployed and live here

https://

### Clone 

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. Click the clipboard symbol to the right of the URL.
4. Open IDE Terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone and copy in your URL and press enter.

You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:
git clone https://github.com/irinatu17/MyCookBook
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
In the terminal window change directory (CD) to the correct file location (directory that you have just created).
Set up environment variables:
Create .env file in the root directory.
On the top of the file add import os to set the environment variables in the operating system.
Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax: os.environ["SECRET_KEY"] = "YourSecretKey"
os.environ["MONGO_URI"] = "YourMongoURI"
.
Install all requirements from the requirements.txt file putting this command into your terminal:
pip3 install -r requirements.txt
Note: GitPod does not require sudo, so if you use another IDE, you will need to include sudo in the beginning of the command: sudo pip3 install -r requirements.txt.
Create a new Database called "MyCookBook" in MongoDB Atlas.
You can sign up for free account, if you do not have one.


This information can be obtained from [Github](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

## Credits 

### Code
For help 
- 
- [Irina](https://github.com/irinatu17/MyCookBook)
- The structure of the CRUD functionality and fra work for part of the app were taken from the code institution course
- For the pagination used this to reference and the modify. [This](https://github.com/DarilliGames/flaskpaginate/blob/master/app.py#L88)
- For reference**Flask Tutorials** - [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) - package structure, custom error pages, WTForms,  hashing passwords
- The navigation bar, cards, modal and mobile-first framework all from [Materialize]()
https://ibb.co/3k51S5K


### websites

All websites I used for reference and guidance.

- [stackoverflow](https://stackoverflow.com/)
- [w3schools](https://www.w3schools.com/)
- [csstricks](https://css-tricks.com/)

### Images

- Images were all obtained through google searches. 
- [BeFunky](https://www.befunky.com/features/graphic-designer/) was used to put effects over  the landing image to make it look more cartoon like.

### Special Thanks

- I would like to give a special mention to all the people on slack and all the people Code Institute, in particular, the Tutor support team and my Mentor Aaron Sinnot.

### Disclaimer 

This app/site was made for a project for the second milestone project on  [Code Institue Course web development course](https://courses.codeinstitute.net/program/FullstackWebDeveloper) by myself James Graham David. 


