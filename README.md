<p align="center">
  <img width="100%" height="90%" src="https://github.com/jimbobding/Bar-Hop-Uk/blob/master/assets/images/Bar Hop UK Logo Guy.png">
</p>

**Demo**
----------
A live demo can be found [here](https://8000-e35317c9-c729-49c7-bdd6-a14b63318364.ws-eu01.gitpod.io/)


# My Idea

I would like to design an application that allows users to create, read, edit and delete cocktail recipes. It would serve as cocktail library that allows anyone to read the recipes but only users who are signed up to the app would be able to add to the library, users would only be able to edit and/or delete their own cocktail entries.

1. This app would serve the user who likes to drink cocktails but do not know the recipes to allow them to make them at home. In the current climate of people not going out as much but still wanting to enjoy cocktails I the comfort of their home.
2. This App would also serve to hospitality staff as it would hold an ever growing library of recipes they could call up =on if they cannot remember how something is mad. It would also serve as a place to house their own creations.


## What the user wants

1. The user wants to easily navigate across all areas of the app. Users will bore quickly if they can find their way around from the moment they start
   interaction with the app.
2. The user wants to be able to view cocktail recipes without having to register.
3. The user wants to be able to register an account and have the information stored safely.
4. The user wants to be able to login it their account ad see their own recipes stored in a user page.
5. The user wants to be able to edit and delete their own recipes.
6. The user wants to be able to view all aspects of a recipe e/g not only the ingredient but also the amounts of said ingredient.
7. The user wants to be able to log out quickly and have the session terminated.
8. The user wants to be able to view the app on multiple platforms.

### Research



## Design

I wanted the look of the app to be simplistic but have the vibe of a classy cocktail menu.

For the framework of the app I used [Materialize](https://materializecss.com/). choose this front-end fdesign framework as it has an ease of use 
and a look of effortless simpliciy. I used ths for my navbar, cards, grid system, icons and colour schemes.
[jquery](https://jquery.com/) was used for functionality of some of the materialize elemts.

### Fonts

The main fonts I settled on was [Slabo](("https://fonts.googleapis.com/css2?family=Slabo+27px:100,300,400,700&display=swap")) which was used for the main body 
of the app, I choose thi as I wanted it to look stylish but still approachable. The oter font I used was [Fredericka the Great]("https://fonts.googleapis.com/css?family=Fredericka+the+Great:100,300,400,700&display=swap"),
this was used on the cocktaol headings to give a slightly more classy look, in keeping with the old school cocktail vibe of the application.



### Colours

The main color scheme was to be of white, black and red being the look of old school bartenders, White shirt with a blck wasitcoat adn a red bow tie.
I also wanted to use colours that would signify the use of functionality to users red being danger green being succes and blue being neutral.

[Materialize Color](https://materializecss.com/color.html)


### 0e9594 - Blue Chill 
grey darken-4

Was used for both header and footer of the app. The main colour of the app as it opens and closes the index page.



### Logo's

The logo was used in the nav-bar as a route back to the home page. The logo itself is the face of a bar tender with the site name underneath.
[Canva](https://www.canva.com/) to design the logos.


## Features
### Existing Features
#### Navbar   

The navbar will be on every page of th app.

The nav bar is set at teh top of the screen and holds the links for users to navigate easily across the site. I choose black as the colour as it was 
in keeping with the colour scheme I was going for givinga slick stylish look. In the lef hand corner of the nav bar is the logo for the app which also serves
as link back to the hoe page. If the app is viewed on mobile devices the menu condense into a hamburger menu that slides the links out from the left, Jquery is
used to activate this.

If a user is logged in the nav bar offers the links 

1. Home - Takes the user to the home page.
2. Spirit Categories - Takes the euser a page with cards that are used to seperate the cocktails into the different alcohol sections.
3. Add-cocktails - Takes user to the add cocktail form.
4. Profile - Takes the user to thier profile page which displays their user name and teh cocktail they have crayed (if they have created any)
5. Logout - Logs teh uer out and takes them to login page.

If user is not logged in 

1. Home.
2. Login - Takes user to the login page where they can log in if they are already registered.
3. register - Takes user to the register page allowing them to create an account.

If user is logged in as Admin

1. Home.
2. Spirit Categories.
3. Add-cocktails.
4. Profile.
5. Manage Categories - Takes the usr to the categotry page whre they can add and edit the soem of the drop categories in the add coktail form.
6. Logout.

## Home page

The home page is the page the user is taken to when they first log in or register it is also available on th enavbar as page for users whod do not
wish to register. It contains a picture of a cocktail that has a call to action button which takes the user to - if they are logged in he add cocktail form,
if they are not logged in, the register form. The page also contains all of the cocktails that have been created on the site available for anyone to view.
The home page also has a search function that searches the drink collection in the databse for words in te serach either returning the reevabt drinks or a message 
telling the user that no drinks match teh serach.




## Spirit selection

The spirirt selection is a that queries all the cocktails in the database and sepertes into there differnt alcohol categories. 


## Add-cocktails

The add-cocktails page contains a foorm that is used to collect the input for cocktails in the databae. There are 6 required fields in the form.

1. The alcohol selection is the first field, this is a drop down that is connected to a collection within the data base. This is a required field and it seperates 
the cocktails into teh different.
2. Alcohol this is for the first ingredient in the cocktail. It is required as to mak e acocktail you will at need at least o ecomponent.
3. Alcohol measure, this is for the measuremnt of the first alcoholic ingredient this is a required field as a measurement would be needded to make a cockail. This will 
also take a nuerical value as an input.
4. Measurement, this used to choose what ever type of measurement would be used e/g MLs or Ounces this again is requred as you need a measurement quantity to create a cocktail. The measurement
is also a dropdown that is part of a collection with in the database I am using.
5. Glassware again is mandatory as it is a physical aspect that is required in making a cocktail. Glassware is also a dropdown menu taht is a collection part of the database, it 
contains a variety of G;assware tah t can be selected.
6. Method. Method is a required field as it a fudamental part of the process in makeing a cocktial.

The rest of the fields are all optional including the add an iamge section that allows you to add a url to a picture representing the cocktail created. If an image is not selected a placeholder
image will be used  in its stead.

## Drink card 

The drink card is how the cocktails are dispalyed in the relevent sections. They contain aan image of the cocktail as well as the name of the cocktail the spirit  category and the user who created the cocktail.

## Cocktail recipe

The cocktail image and name on the drink card are wrapped in an anchor that takes you to drinks recipe page, this page contains the rest of ingredients, the method, notes on tehe cocktail . The page also contains three buttons, teh back button 
which takes the user back to teh home page. Also the delete and edit cocoktail buttons which are only visibile if the cocktail was creaetd by the logged in user.

## Edit cocktail 

The edit cocktail form is the same as the add cocktail form but all the fields that had been previously filled in by the user are pre populated.
At teh bottom of teh for there are two buttons, Edit cocktail which confirms the edit and brings teh user back to the home page and cancel button which cancels any of the edits ad brings the user back to the home page.

### Delete cocktail

The delete cocktail function removes the cocktail from the app as well as removing it from the data-base.

### Register 

The register page ask the user to input a username and a password. The username and password has a minimum of 5 characters and a maxinmun of 15, it takes the any lower or uppercase letter and
any number between 0-9. The user will be notified by a flash message if the username is already taken, once the username and password have been entered a flash message will come notifying the user
that the registration was succesful. The user is then added to the database.

### Login

The login page takes the users username and password. If the password or username is incorect a fash message will display saying that the username or pasword are incorect (it will not identify which one is incorect as an extra security measure).
If the username and password are found a flash message will display welcoming the user wih thier username and they will be directed to thier profil page.

### Logout

The log out function 

### Profile

The profile page has a card displaying the logged in users name and also diisplays all the cocktails created by the user.

### Add Categories

Ths page is only open to admin users it allows the user to add extra categories to the dropdown function aswell as editing and deleting existing ones. The top of the page comtains a button labelled add catedgory, this will take you to  a card with an input field
taht allows you to to type in the name of the category you wish to add and a button to confirm the addition, the user will be  taken back to teh mange categories section whit a flash message displaying that the selected category has been added.
The user would click on the manaage categories section which would take the user the mange categories page. On a materialize carousel the categpries are displayed, if the user cick on one it will open up giving you two buttons Edit and Delete.
Deler will remove the category from the dropdowns and database and displaye a message yor category has been deleted, Edit will take you to a seperate card that will have two buttons and an iput box that  allows the user to change the name of the category.
After the user has changed the name in the input box they can either click edit which will take them back to the manage categories page with a flash diplaying taht your catedory has been succesfully edited, or you can clck cancel which will cance the operatuion and take you back to the manage categories section.


### Testing 

I tested the functionaluty of the app throughout the entire devolpment process and also had friends and family test it on various devices.




## Users guidance


### Register

1. Click the register link in the navigation bar.
2. Enter a chosen username. 
3. Enter a chosen password.
4. Click the regster button. 
5. You will be taken to your new created profile page.
6. Alternativly choose the "Have an account login" link below the login if the user lredy has an account.


### Login

1. Click the login link in the navigation bar.
2. Enter your previously chosen username.
3. Enter your previously chosen password.
4. Click the regster button. 
5. You will be taken to your profile page.
6. Alternativly choose the "If you dont have account click here Register Here" link below the login if the user does not have an account.


### Login
1. Click the logout link in the navigation bar.
2. This will take you back to the login page.


### Add-cocktail

1. Click the add-cocktail link in the navigation bar.
2. You will be taken to the add cocktail form.
3. For the choose alcohol type choose the champiom alcohol in your cocktail. This will be provided in a drop down menu with a drop down arrow which when pressed will display the alcohol categories.
4. The reamining fileds are to be selected as the user goes through the form. All dropdown menus will be displayed in the same way.
5. The measurment fields are intergers and will only take numerical values.
6. Asterixed fields are mandatory.
7. To add a a url to the image filed of the form the user must choose the image they wish to use and copy the url for the image and then paste this in to the image filed.
8. Click on the add cocktail button on the bottom of the form.


### Edit-cocktail

1. Click on a cocktail that has been created by the logged in user.
2. Click on te edit button at the bottom of the cocktal recipe page.
3. All the fields of the cocktail form that have previously been filled whem th ecocktail was created will be populated by the values originally chosen.
4. 
5. The measurment fields are intergers and will only take numerical values.
6. Asterixed fields are mandatory.
7. To add a a url to the image filed of the form the user must choose the image they wish to use and copy the url for the image and then paste this in to the image filed.
8. Click on the edit cocktail button on the bottom of the form to apply the changes.
9. Alternativety click on the cancel button to cancel the changes and go back to drinks page.


### Code format

[freeformatter](https://www.freeformatter.com/css-beautifier.html) was used to format both CSS and HTML.

## Technologies used

- [git-hub](https://github.com/) To Store my code
- [git-pod](https://www.gitpod.io/) Used as my IDE to work on my code
- [HTML5](https://en.wikipedia.org/wiki/HTML5) Used to build my project
- [Cascading-Style-Sheets](https://www.w3.org/Style/CSS/Overview.en.html) Used to style my project
- [Google-Fonts](https://fonts.google.com/) Used for the two types of text used throughout the project 
- [Font-awesome 5](https://fontawesome.com/) Used for icons used on the project 
- [Jquery](https://jquery.com/download/) Jquery used to simplify some of the code
- [Materialize](https://materializecss.com/) Used for the  framework of my project and also for the navigation bar, the cards (spirit selection, cocktail cards)

## Validators

- [The-W3c-Markup-Validation-Service](https://jigsaw.w3.org/css-validator/) - Validates/checks for mistakes CSS
- [The-W3c-Markup-Validation-Service](https://validator.w3.org/) - Validates/checks for mistakes HTML


## Testing

For testing, I used the [goggle chrome development tools](https://developers.google.com/web/tools/chrome-devtools) to test the app on a
variety of screen sizes for Responsiveness, design and user experience. Although on chrome development tools, the app appeared to work across all
screen sizes on using my iPhone and iPad I found some problems.

For the actual task of testing, I went through each device and used all the functions on the app. This was to check out the aesthetics and functionality 
off the app.

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

I had  problem with 

#### Resolution


After testing I believe the site functions works well for a user.


## Wireframe

For my wireframes I first used pen and paper to jot down my original thoughts and then once I had a clearer picture in my head of
how I wanted the app to look I used [Balsamiq](https://balsamiq.com/) to mock it up. The design did change from the pen and pad to Balsamiq
to actual coding as certain things did not look at good as I hoped, but overall it stayed pretty much the same.

 [wireframes](https://github.com/jimbobding/Bar-Hop-Uk/tree/master/assets/wireframes)


I can still edit the site remotely from my gitpod workspace by making changes committing them and then and pushing them through to the repository.


## Deployment

1. Login to Heroko account.
2. Click on New at the right top corner and click on Create new app.
3. Choose App name and a region (Europe was the closest to me). Then click on Create app.
4. Go to terminal window and create requirements.txt by running command pip3 freeze --local > requirements.txt
5. Then create Procfile by running command echo web: python app.py > Procfile Remember P is capital
6. Add these files to stagging area by running command git add requirements.txt & git add Procfile.
7. Then commit these file respectively by running command git commit -m "Added requirements.txt & git commit -m "Added Procfile.
8. Then push these files to github by running command git push
9. Go back to Heroku to your App and click on Deploy tab.
10. Then go to Deployment Method and click on Github Connect to Github.
11. Then make sure your Github Profile is displayed and add you repository name and click on Search.
12. Once it find your repository then click on Connect.
13. Go to Settings at the top. Then click on Reveal Config Vars.
14. In Config Vars add IP with value 0.0.0.0 then add PORT as 5000 then add SECRET_KEY then add MONGO_URI and then add MONGO_DBNAME which is the name of database.
15. Go back to Deploy tab and click on Enable Automatic Deploys.
16. Click on Deploy Branch
17. It will take a minute and display a message that Your app was successfully deployed.
18. Click on View to launch your deployed app.

My website is now deployed and live here

https://


## Clone 

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. Click the clipboard symbol to the right of the URL.
4. Open IDE Terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone and copy in your URL and press enter.

This information can be obtained from [Github](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)


## Credits 

### Code

- The navigation bar, cards, modal and mobile-first framework all from [Materialize]()
- The maps and code that go with the breweries near you locater came from [here](https://codelabs.developers.google.com/codelabs/google-maps-nearby-search-js/#4). (all code including HTML, CSS and javascript was obtained from this site and then modified by myself)
- The maps and code that go with the cities maps came from [here](https://developers.google.com/maps/documentation/javascript/examples/directions-waypoints). (all code including HTML, CSS and javascript was obtained from this site and then modified by myself)
- The code for the auto-reply email was taught to me on the [Code Institue Course web development course](https://courses.codeinstitute.net/program/FullstackWebDeveloper) apart from the code for closing the modal and clearing the input fields which was from [stackoverflow](https://stackoverflow.com/)
- The button for the become a cicerone card was used with code obtained from  [here](https://fdossena.com/?p=html5cool/buttons/i.frag)

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

