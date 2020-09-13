
<p align="center">
<img src="https://i.ibb.co/kJBb49T/Screenshot-2020-09-13-at-11-28-24.png"  alt="All devices" target="_blank" rel="noopener">
</p>



# [My Cocktail Buddy](https://cocktail-buddy-jim.herokuapp.com/)  

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
A live demo can be found [here](https://cocktail-buddy-jim.herokuapp.com/add_cocktails)

# My Idea

I would like to design an application that allows users to create, read, edit and delete cocktail recipes. It would serve as a cocktail library that allows anyone to read the recipes but only users who are signed up to the app would be able to add to the library, users would only be able to edit and/or delete their cocktail entries.

1. This app would serve the user who likes to drink cocktails but does not know the recipes to allow them to make them at home. In the current climate of people not going out as much but still wanting to enjoy cocktails I the comfort of their home.
2. This App would also serve to hospitality staff as it would hold an ever-growing library of recipes they could call up =on if they cannot remember how something is mad. It would also serve as a place to house their creations.

### User stories

### First Time Visitor Goals
1. As a First Time Visitor, I want to easily navigate the app using the navbar.
2. As a First Time Visitor, I want to be able to easily find and look through the different drink cards without the obligation of registering an account.
3. As a First Time Visitor, I want to be able to open up the drink cards and view the recipes inside them.

### Returning Visitor Goals
1. As a Returning Visitor, I want to be able to register an account with the app.
2. As a Returning Visitor, I want to be able to add my content in terms of drink recipes.
3. As a Returning Visitor, I want to be able to use the search engine t find my drink or any other drinks that I would like to try.

### Frequent User Goals
1. As a Frequent User, I want to be able to log in easily to the app with my login details.
2. As a Frequent User, I want to be able to edit and or delete any recipes I may have created.
3. As a Frequent User, I want to be able to view my content readily and easily through a profile page.
4. As a Frequent User, I want to be able to easily and safely exit the app.
5. As a Frequent User, I want to be able to view the app easily on different devices.




Jake T, a bartender from Wales, UK - "I work in a cocktail bar and am constantly making cocktails for customers, I have a lot of recipes stored in my head but sometimes customers ask for cocktails, I don’t quite know how to make I generally google the wanted cocktail to find the recipe. I would love to be able to have an ever-growing
                                      recipe book that I could consult for recipes and a place in which I can store my creations"

Adam R, a financial consultant from Melbourne, Aus - "I enjoy the weekends where I can go out and enjoy cocktails and experience drinks that I am unable to drink at home. But sometimes I would like to avoid the crowds and invite my friends around to my house for drinks or to host a cocktail party to honour an occasion. I would like
                                                      a database of drinks with the steps that allow me to recreate them at home."



# Design

I wanted the look of the app to be simplistic but have the vibe of a classy cocktail menu.

For the framework of the app, I used [Materialize](https://materializecss.com/). choose this front-end design framework as it has an ease of use and a look of effortless simplicity. I used this for my nav-bar, cards, grid system, icons and colour schemes.
[jquery](https://jquery.com/) was used for the functionality of some of the materialize elements.

### Fonts

The main fonts I settled on was [Ubunto](hhttps://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@1,300&display=swap") which was used for the main body 
of the app, I choose this as I wanted it to look stylish but still approachable easy to read and with character.

### Colours

The colour of white and black are used for the main body of the app. The navbar and footer are black which wraps the body which has a background of white, I felt I wanted to keep this clean and simple as here would be a fair bit going on in the body 
with different cards having different colours on them. 
I also wanted to use colours that would signify the use of the functionality to the user’s red being danger green beI also used a red colouring a success and blue being neutral.


[flatui colorpicker](http://www.flatuicolorpicker.com)
[Materialize Color](https://materializecss.com/color.html)


### Color Scheme

 - I used a red colour with a hsla to give it an opaque colour and a forest green colour to give the app some colour, as well as on a lot of the buttons

<img width="200px" height="100%px" src="https://github.com/jimbobding/Cocktail-buddy-jim/blob/master/static/images/Screenshot 2020-09-11 at 11.43.17.png">
<img width="200px" height="100px" src="https://github.com/jimbobding/Cocktail-buddy-jim/blob/master/static/images/Screenshot 2020-09-13 at 19.52.37.png">
 

<img src="https://i.ibb.co/GQMx2Hj/Screenshot-2020-09-13-at-19-46-25.png" alt="Login" target="_blank" rel="noopener">

### Logo

The logo was used in the nav-bar as a route back to the home page. The logo itself is the face of a bartender with the site name underneath.
[Canva](https://www.canva.com/) to design the logos.


## Wireframe

For my wireframes I first used pen and paper to jot down my original thoughts and then once I had a clearer picture in my head of
how I wanted the app to look I used [Balsamiq](https://balsamiq.com/) to mock it up. The design did change from the pen and pad to Balsamiq
to actual coding as certain things did not look at good as I hoped, but overall it stayed pretty much the same.

 [wireframes](https://github.com/jimbobding/Cocktail-buddy-jim/blob/master/static/wireframes)

## Features
### Existing Features
#### Navbar   

The nav-bar will be on every page of the app.

The nav-bar is set at the top of the screen and holds the links for users to navigate easily across the site. I choose black as the colour as it was in keeping with the colour scheme I was going for giving a slick stylish look. In the left-hand corner of the navbar is the logo for the app which also serves
as a link, back to the home page. If the app is viewed on mobile devices the menu condense into a hamburger menu that slides the links out from the left, Jquery is
used to activate this.

If a user is logged in the nav-bar offers the links 

1. Home - Takes the user to the home page.
2. Spirit Categories - Takes the user a page with cards that are used to separate the cocktails into the different alcohol sections.
3. Add-cocktails - Takes the user to the add cocktail form.
4. Profile - Takes the user to their profile page which displays their user name and the cocktail they have created (if they have created any)
5. Logout - Logs the user out and takes them to the login page.

If the user is not logged in 

1. Home.
2. Login - Takes the user to the login page where they can log in if they are already registered.
3. register - Takes the user to the registration page allowing them to create an account.

If the user is logged in as Admin

1. Home.
2. Spirit Categories.
3. Add-cocktails.
4. Profile.
5. Manage Categories - Takes the user to the category page where they can add and edit some of the drop categories in the add cocktail form.
6. Logout.

#### Home page

The home page is the page the user is taken to when they first log in or register it is also available on the navbar as a page for users who do not
wish to register. It contains a picture of a cocktail that has a call to action button which takes the user to - if they are logged in the add cocktail form
if they are not logged in, the register form. The page also contains all of the cocktails that have been created on the site available for anyone to view.
The home page also has a search function that searches the drink collection in the database for words in the search either returning the relevant drinks or a message 
telling the user that no drinks match the search.

#### Spirit selection

The spirit selection is a page that queries all the cocktails in the database and separates them into their different alcohol categories. 

#### Add-cocktails

The add-cocktails page contains a form that is used to collect the input for cocktails in the database. There are 6 required fields in the form.

1. The alcohol selection is the first field, this is a drop-down that is connected to a collection within the database. This is a required field and it separates 
the cocktails into the different.
2. Alcohol this is for the first ingredient in the cocktail. It is required to make a cocktail you will at need at least one component.
3. Alcohol measure, this is for the measurement of the first alcoholic ingredient this is a required field as a measurement would be needed to make a cocktail. This will 
also, take a numerical value as an input.
4. Measurement, this used to choose whatever type of measurement would be used e/g MLS or Ounces this again is required as you need a measurement quantity to create a cocktail. 
5. Glassware again is mandatory as it is a physical aspect that is required in making a cocktail. Glassware is also a dropdown menu that is a collection part of the database, it contains a variety of Glassware that can be selected.
6. Method is a required field as it a fundamental part of the process in making a cocktail.

The rest of the fields are all optional including the add an image section that allows you to add a URL to a picture representing the cocktail created. If an image is not selected a placeholder
image will be used in its stead.

#### Drink card 

The drink card is how the cocktails are displayed in the relevant sections. They contain an image of the cocktail as well as the name of the cocktail the spirit category and the user who created the cocktail.

#### Cocktail recipe

The cocktail image and name on the drink card are wrapped in an anchor that takes you to the drinks recipe page, this page contains the rest of the ingredients, the method, notes on the cocktail. The page also contains three buttons, the back button which takes the user back to the home page. Also, the delete and edit cocktail buttons which are only visible if the cocktail was created by the logged-in user.

#### Edit cocktail 

The edit cocktail form is the same as the add cocktail form but all the fields that had been previously filled in by the user are pre-populated.
At the bottom of the for there are two buttons, edit cocktail which confirms the edit and brings the user back to the home page and cancel button which cancels any of the edits and brings the user back to the home page.

#### Delete cocktail

The delete cocktail function removes the cocktail from the app as well as removing it from the database.

#### Register 

The register page asks the user to input a username and a password. The username and password have to have a minimum of 5 characters and a maximum of 15, it takes any lower or uppercase letter and
any number between 0-9. The user will be notified by a flash message if the username is already taken, once the username and password have been entered a flash message will come notifying the user
that the registration was successful. The user is then added to the database.

#### Login

The login page takes the users username and password. If the password or username is incorrect a flash message will display saying that the username or password is incorrect (it will not identify which one is incorrect as an extra security measure).
If the username and password are found a flash message will display welcoming the user with their username and they will be directed to their profile page.

#### Logout

The log out function pops out the session user and redirects them to the login page

#### Profile

The profile page has a card displaying the logged in users name and also displays all the cocktails created by the user.

#### Add Categories

This page is only open to admin users it allows the user to add extra categories to the dropdown function as well as editing and deleting existing ones. The top of the page contains a button labelled add category, this will take you to a card with an input field
that allows you to type in the name of the category you wish to add and a button to confirm the addition, the user will be taken back to the manage categories section whit a flash message displaying that the selected category has been added.
The user would click on the manage categories section which would take the user the mange categories page. On a materialize carousel the categories are displayed, if the user clicks on one it will open up giving you two buttons Edit and Delete.
Delete will remove the category from the dropdowns and database and displayed a message your category has been deleted, edit will take you to a separate card that will have two buttons and an input box that allows the user to change the name of the category.
After the user has changed the name in the input box they can either click edit which will take them back to the manage categories page with a flash displaying that your category has been successfully edited, or you can click cancel which will cancel the operation and take you back to the manage categories section.

#### pagination

This is used in the drinks section and also the profile page. It allows only 8 cocktail recipes per page and gives a page-turning system so you can go back and forth between pages each displaying 8 recipe cards.


### Features to add

There are features I would like to Implement in the app in the future.  have not yet put these features into place due to time constraints and also some of them 
would be beneficial with a bigger base of users.

#### Change password / username

I would like to implement a function that allows users to be able to change their password and or username. This would be beneficial for users in the event they thought their security had been compromised, also if they had made
a mistake and either the password or username had become and inconvenience.

#### A like system

I would like a like system where users could express their like in a particular cocktail. This data could be collected and used to promote certain products to users or suggest other
similar cocktails that they may like.

#### Favourites

This would be used in conjunction in the like system it would collect all the users favourite cocktails and store them for the user to view at any time they liked. 


## User guidance

### Register

1. Click the register link in the navigation bar.
2. Enter a chosen username. 
3. Enter a chosen password.
4. Click the register button. 
5. You will be taken to your newly created profile page.
6. Alternatively, choose the "Have an account login" link below the login if the user already has an account.

### Login

1. Click the login link in the navigation bar.
2. Enter your previously chosen username.
3. Enter your previously chosen password.
4. Click the register button. 
5. You will be taken to your profile page.
6. Alternatively, choose the "If you don’t have an account click here Register Here" link below the login if the user does not have an account.

### Login
1. Click the logout link in the navigation bar.
2. This will take you back to the login page.

### Add-cocktail

1. Click the add-cocktail link in the navigation bar.
2. You will be taken to the add cocktail form.
3. For the choose alcohol type choose the champion alcohol in your cocktail. This will be provided in a drop-down menu with a drop-down arrow which when pressed will display the alcohol categories.
4. The remaining fields are to be selected as the user goes through the form. All dropdown menus will be displayed in the same way.
5. The measurement fields are integers and will only take numerical values.
6. Asterisked fields are mandatory.
7. To add a URL to the image filed of the form the user must choose the image they wish to use and copy the URL for the image and then paste this into the image filed.
8. Click on the add cocktail button on the bottom of the form.

### Edit-cocktail

1. Click on a cocktail that has been created by the logged-in user.
2. Click on the edit button at the bottom of the cocktail recipe page.
3. All the fields of the cocktail form that have previously been filled when the cocktail was created will be populated by the values originally chosen.
4. Asterisked fields are mandatory.
5. To add a URL to the image filed of the form the user must choose the image they wish to use and copy the URL for the image and then paste this into the image filed.
6. Click on the edit cocktail button on the bottom of the form to apply the changes.
7. Alternatively, click on the cancel button to cancel the changes and go back to the drinks page.


## Technologies used

- [git-hub](https://github.com/) To Store my code
- [git](https://git-scm.com/) For version control
- [git-pod](https://www.gitpod.io/) Used as my IDE to work on my code
- [pip](https://pip.pypa.io/en/stable/installing/) For installing tools used in the project
- [HTML5](https://en.wikipedia.org/wiki/HTML5) Used to build my project
- [Cascading-Style-Sheets](https://www.w3.org/Style/CSS/Overview.en.html) Used to style my project
- [Am-I-Responsive](http://ami.responsivedesign.is/) I used this to check the responsiveness on devices and used the images as part of the read me file
- [Google-Fonts](https://fonts.google.com/) Used for the two types of text used throughout the project 
- [Font-awesome 5](https://fontawesome.com/) Used for icons used on the project 
- [Jquery](https://jquery.com/download/) Jquery used to simplify some of the code
- [Materialize](https://materializecss.com/) Used for the  framework of my project and also for the navigation bar, the cards (spirit selection, cocktail cards)
- [Python-3.8.2] (https://www.python.org/) Back end programming language dI used for this project.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)- a microframework for building and rendering pages.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - templating language for Python, to display back-end data in HTML.
- [Heroku](https://dashboard.heroku.com/app) - to host the project.
- [MongoDB](https://cloud.mongodb.com/)- NoSQL database for storing back-end data.
- [PyMongo] - Used to connect MongoDB and Python
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Secuirty use for password hashing

### Testing User Stories from User Experience (UX) 
### First Time Visitor Goals
1. As a First Time Visitor, I want to easily navigate the app using the navbar.
- The Navbar is located at the top off the screen and stands out from the body of the page. The links on the navbar change colour when they are hovered over
to show responsiveness. If the user is not logged in only certain parts of the application will be open to them.
2. As a First Time Visitor, I want to be able to easily find and look through the different drink cards without the obligation of registering an account.
- Using the Navbar the user can easily navigate to the home page where they can browse through all of the drinks that are currently on the app, the search engine is also
available and useable for users who are not logged in.
3. As a First Time Visitor, I want to be able to open up the drink cards and view the recipes inside them.
- Again without being logged in a user may browse through all the drink cards and can click on any of them to see the content. 

### Returning Visitor Goals
1. As a Returning Visitor, I want to be able to register an account with the app.
- The register page is marked on the navbar and is also marked in the login page. The username and password are hashed after they are input and the fields themselves are 
tool tipped to inform the user if they are not meeting the criteria for the fields or if they are choosing details that have already been chosen.
2. As a Returning Visitor, I want to be able to add my content in terms of drink recipes.
- On the home page and the navbar, the add cocktail button is marked. Upon clicking this link you will be taken to the add cocktail form in which you are given fields to fill in regarding your recipe. All the mandatory fields are marked clearly in red and are tool tipped to advise the user that they have not filled in the field.
3. As a Returning Visitor, I want to be able to use the search engine to find my drink or any other drinks that I would like to try.
- On the homepage and marked in a coloured box is a search bar with a call to action button. There is a brief paragraph advising the user on the use of this search engine. The user will
be prompted if the search returns no results.

### Frequent User Goals
1. As a Frequent User, I want to be able to log in easily to the app with my login details.
- The login field is marked clearly on the navbar and again marked in the register page. It has icons next to the fields to prompt users to fill them in and they are also
tool tipped to let users know of any mistakes.
2. As a Frequent User, I want to be able to edit and or delete any recipes I may have created.
- The user can find his recipes by either looking through all the drinks on the database, using the search engine to find their recipes or if they click on the profile page all there own drink-recipes 
will be displayed here. If they click on any of these recipes they will take taken to a page with the ingredients, method etc but there will also be three calls to action buttons. The back button will take the user back to the previous page, the edit button will open the cocktail recipe in the cocktail form with all the fields pre-populated with what the user originally input here the user can change any of the fields they choose and then click the edit cocktail button at the bottom of the form, if the user changes there mind they can click the cancel button and all changes will be cancelled. The third button is the delete cocktail button in which the user can delete the cocktail from the database. These edit and delete the call to action buttons are only available on the users drink recipes.
3. As a Frequent User, I want to be able to view my content readily and easily through a profile page.
- If the user clicks on the profile page they will be taken to their profile page which will display their name, the number of drinks they have as well as all of their drink recipes.
4. As a Frequent User, I want to be able to easily and safely exit the app.
- The logout function located clearly on the navbar takes the user out of the session and does not leave any hint or clue in the login section about their details.
5. As a Frequent User, I want to be able to view the app easily on different devices.
- The app was built on the materialize framework which uses a very easy to use grid layout system allowing for a smooth transition into various devices. The app was tested on various devices to ensure good user experience. 


## Testing

For testing, I used the [goggle chrome development tools](https://developers.google.com/web/tools/chrome-devtools) to test the app on a
variety of screen sizes for Responsiveness, design and user experience. Although on chrome development tools, the app appeared to work across all
screen sizes on using my iPhone and iPad I found some problems.

For the actual task of testing, I went through each device and used all the functions on the app. This was to check out the aesthetics and functionality 
off the app.


## Testing 

I tested the functionality of the app throughout the entire development process and also had friends and family test it on various devices.


### Drinks/Home page

When I click on the home page in the navbar I am taken to a page that displays an image with a button giving me the option to log in, if I a not logged in and to add a cocktail
if I am logged in. It also shows a search query which will find a drink searching the in fields of alcohol_element_text_glass_type_text_drink_name_text three fields in the drink collection of my cocktail database in Mongo DB. It also displays the first 8 cocktails in my drink collection with pagination buttons to take you to a further 8.



### Register
 
 - Tried to register with a username and password that were too short min length being 5 letters. Tooltip response ("please match the format that is requested")
 - Tried to register with empty fields for username and password Tooltip response ("please fill in this field")

### Login

- Tried to login with non-existent credentials. Flash message  ("Incorrect password and/or username")
- Tried to login with empty fields. Tooltip response ("please fill in this field")
- Tried to login with non-matching username and password. Flash message ("Incorrect password and/or username")

### Add cocktails

- Tried to add a cocktail without filling in the required fields. Tooltip response ("please select an item in the list" or "please fill in the valid field")
- Tried adding a cocktail with no image URL. The place holder picture which I was adding in on the add cocktail app.proute worked for the drinks page but I noticed it did
not appear on the profile page or the spirit selection queries.
- Tired adding a cocktail and making the drink name the max amount of characters, I adjusted the font size to make sure it fit in the card.

#### Resoltions

- In the add cocktail app.route, the picture was being added as an image that I had saved in my static images file, this meant that when it came through to my drink page it was fine but as a user would go to other pages on the app e/g the profile page the URL for the profile page would get called first and not allow the static image to be displayed. I got around this by using the URL for the image so it was being called externally. This fixed the issue an the image now displays on all pages.


### Edit cocktail

- Clicked on the edit cocktail button, all field that was populated was still populated.
- Tried to remove a required field in the testing form. Tooltip response ("please fill in this field")
_ Tried to change all of the fields in the edit function> they all worked and changed accordingly.
- Tried to remove the selected the URL for the image address and save the change. The place holder image did not appear in the drinks card or cocktail recipe page.

#### Resoltions

- This issue is currently unresolved

#### Log out
- Log out function worked as planned and took me to the login page.


### Feedback 

I had three separate people test it across different formats.

- The add cocktail form became congested on smaller devices.
- The measurements part of the add cocktail function is unnecessary users would rather be able to type in there own measurements or choose one measurement and have the rest of the areas be pre-populated with this same measurement.


### Resolutions

- I changed the format of the add cocktail format so that each option would take up an entire column rater than share the screen with another selection.
- I choose to get rid of the measurement collection as I did not think it was majorly important and it allowed users to tye in their measurements. I would like to implement the measurement collection but with better user use in the future.


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

- Chrome
- Safari
- Internet explorer - windows 8.1 & 10
- firefox windows - windows 8.1
- Edge - Windows 10 

#### Problems

I had a problem with the measure fields taking numbers, which I wanted to do to minimalize mistakes when people are inputting data as they would only be able to input numbers rather than text. 
Then send them to the mongo database as a string, so when they were returned they would not pre-populate the fields in the edit cocktail form. To fix this problem I turned the string into integers in the app.route in bot the add-cocktails and the edit cocktail function <p>alcohol_measure': int(request.form.get('alcohol_measure'))</p> this seemed to work initially but then realised that if the measure fields were left empty then it would send back an error. This could have been solved by using several if statements but after deliberating with the tutors I made the decision it would be less problematic to leave the fields as text fields rather than overcomplicate the code with lengthy if statements.


## Deployment

### Heroku deployment

1. Login to my Heroku account.
2. Click on New at the right top corner and click on Create new app.
3. Choose App name and a region (Europe was the closest to me). Then click on Create app.
4. Go to the terminal window and create requirements.txt by running command pip3 freeze --local > requirements.txt
5. Then create Procfile by running command echo web: python app.py > Procfile Remember P is capital
6. Add these files to the staging area by running command git add requirements.txt & git add Procfile.
7. Then commit these file respectively by running command git commit -m "Added requirements.txt & git commit -m "Added Procfile.
8. Then push these files to GitHub by running command git push
9. Go back to Heroku to your App and click on deploy tab.
10. Then go to Deployment Method and click on Github Connect to Github.
11. Then make sure your Github Profile is displayed and add you repository name and click on Search.
12. Once it finds your repository then click on Connect.
13. Go to Settings at the top. Then click on Reveal Config Vars.
14. In Config Vars add IP with value 0.0.0.0 then add PORT as 5000 then add SECRET_KEY then add MONGO_URI and then add MONGO_DBNAME which is the name of the database.
15. Go back to Deploy tab and click on Enable Automatic Deploys.
16. Click on Deploy Branch
17. It will take a minute and display a message that Your app was successfully deployed.
18. Click on View to launch your deployed app.


### Clone 

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. Click the clipboard symbol to the right of the URL.
4. Open IDE Terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone and copy in your URL and press enter.

This information can be obtained from [Github](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
                                                    
## Credits 

### Code

- [Irina](https://github.com/irinatu17/MyCookBook) - I took the idea of the error page sand some inspiration form this excellent project
- The structure of the CRUD functionality and fra work for part of the app were taken from the code institution course
- Parts of the code for logn and registrayion were taken from advice from te ttors at the codeistitute course
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
- [unsplash](unsplash.com/)
- Images were all obtained through google searches. 

### Drink recipes
- My own creations
- [bbc-drinks](https://www.bbcgoodfood.com/recipes/category/all-cocktails-drinks)
- [drinks-tube](https://www.jamieoliver.com/drinks-tube/)
- [wikipedia] (https://en.wikipedia.org/wiki/Main_Page)

### Special Thanks

- I would like to give a special mention to all the people on slack and all the people Code Institute, in particular, the Tutor support team and my Mentor Aaron Sinnot

**This project is for educational use only.**
