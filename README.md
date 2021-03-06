# Dance Your Way

Dance Your Way is a website designed alongside Gusto, a London based Latin Dance group

Dancers will come to the website to see what local events are occurring, whilst event organisers will log in to add their events to the database.

---

# Contents

1. [UX](#ux)
2. [Features](#Features)
3. [Technologies](#Technologies)
4. [Languages](#Languages)
5. [Libraries](#Libraries)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)

## UX

##### User Stories

- "As an event organiser, I want to post details about my events, so I can get more customers"
- "As a dancer, I want to view information about events in my city, so I can plan where to go for class"

##### Design Choices

- Pagination style with distinct pages for each section
- A hero video demoing a class. This is supplemented by call to action icons for both key user types (dancers and organisers)
- Purple was used as one of the primary colours (#6A1B9A). This was used throughout the website, contrasted with white backgrounds to give a clean, simple feel.
- Montserrat is the main font family used as a clear and professional style for the body of the website. Indie Flower was used for the brand name to give a creative vibe
- The navbar fixed due to the large amount of results on each page so the user does not have to scroll back to the top, this is hidden away in mobile view

##### Wireframes

I used [Balsamiq](https://balsamiq.com/) to create detailed wireframes for each page at a mobile level and then at a desktop level to keep with the Mobile First design approach.

As is to be expected certain elements present in the wireframes did not make it into the project itself but may yet do so further down the line.

You can find my wireframes [here](https://github.com/Magnusson95/Dance-Your-Way/tree/master/wireframes).

## Features

##### Existing Features

### Base

All pages have a navbar, which condenses on mobile view:

- **User not logged into the platform**
<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Base%20Navbar.JPG?raw=true" alt="Navbar Not Signed In">
 <img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Base%20Sidenav.JPG?raw=true" alt="Sidenav Not Signed In">

Unregistered users may view events, organisers and sign-up. The "Add Event" function will redirect unregistered users to the sign-up page.

- **User logged into the platform**
<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Base%20Navbar%20Signed%20In.JPG?raw=true" alt="Navbar Signed In">
<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Base%20Sidenav%20Signed%20In.JPG?raw=true" alt="Sidenav Signed In">

Signed In users are able to view events, organisers, add events, edit their account details, edit their event details and sign out.

### Sign Up/Login

Users may sign up, submitting their details to the database (passwords are hash protected). They can then use the same page to login.

CRUD - Create:
 -  Checks are made on the database to ensure usernames are not duplicated upon creation
 -  Security of users details is maintained through the use of hashes on passwords

CRUD - Read:
 -  Function reads login details and checks they match the database
 -  Incorrect login errors are displayed if either do not match

- **User sign up/login page**
<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Login%20and%20Signup.JPG?raw=true" alt="Login and Signup">

### Account Page

Users are directed upon login, or through the link in the top left of the navbar, to their account page.

CRUD - Read:
 -  Users can see the current information held within the database, through their account page.
 -  AWS S3 has been used to display profile pictures

CRUD - Update:
 -  Users can update the information pulled from the read function
 -  Users can create/update their account profile picture
 -  Users can find links to edit their events from this page

CRUD - Delete:
 -  Users can delete their profile, this also deletes all events created by the user.
 -  Users can delete individual events from this page

- **Account page**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Account%20Update.JPG?raw=true" alt="Account Page">

- **Edit event page**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Event%20Update%20Page.JPG?raw=true" alt="Event Update Page">

- **Delete Account/Event**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Profile%20and%20Event%20Delete.JPG?raw=true" alt="Delete Account/Event">

### Event Cards and Maps

All users may view the events within the database both through a list of event cards and as markers plotted on Maps

- **Event Card**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Event%20Card%20Example.JPG?raw=true" alt="Event Card Example">
<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Event%20Card%20Example%20Details.JPG?raw=true" alt="Event Card Example Details">

Event card shows the event name, city, country, weekday, time, dance styles and event social link on the cover. AWS S3 has been used to display event pictures.

Clicking on the card provides further details including an about section, price for the event, full address and the organiser's name (with link to their page).

- **Maps**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/London%20Events%20Map%20Example.JPG?raw=true" alt="London Events Map Example">

Maps filter to the country (zooming to center on the country accordingly) and dance style selected. A basic version of the event card is shown when the marker is clicked.

### Organiser information

A page displays information and events for all the organisers within the database, allowing users to look up specific event organisers

- **Organisers Page**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Organiser%20Details.JPG?raw=true" alt="Organisers Page">

### Filters

The main pages displaying lists of events can be filtered by country

- **Country Filter**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Country%20Filter.JPG?raw=true" alt="Country Filter">

Dance styles can be filtered by the "Where to Dance" page link

- **Style Filter**

<img src="https://github.com/Magnusson95/Dance-Your-Way/blob/master/Features/Event%20Style%20Filter.JPG?raw=true" alt="Style Filter">

##### Features Left to Implement

- Separate CRUD functionality for one off events with specific dates, rather than weekly events
- ecommerce system to purchase tickets for events

## Technologies

- [Github](https://github.com/) to host this project's respositories.
- [Gitpod](https://www.gitpod.io/) IDE of choice for development.
- [Git](https://en.wikipedia.org/wiki/Git) for version control
- [Google Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools) for testing and troubleshooting.
- [Coolors](https://coolors.co/) for colour schemes.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML) to build the page.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to style the page.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) to add interactivity.
- [Python](https://www.python.org/) to query database

## Libraries

- [Font Awesome](https://fontawesome.com/) for icons.
- [Google Fonts](https://fonts.google.com/) used for fonts.
- [Materialize](https://materializecss.com/) a modern responsive front-end framework based on Material Design.
- [jQuery](https://jquery.com/) used for easier integration of Javascript.
- [Flask](https://www.fullstackpython.com/flask.html) for app routing
- [PyMongo 3.10.1](https://api.mongodb.com/python/current/) Python API for MongoDB

## Testing

##### Internet Browsers

The same process of opening up the live page and meticulously clicking all links, buttons, and re-sizing of windows was utilized in the following browsers:

- Google Chrome - Main browser of choice for development.
- Microsoft Edge – All working as intended
- Mozilla Firefox - No issues. Everything works as intended.
- Safari - All working as intended.

The site has been tested physically on a number of mobile devices including:

- iPhone 5, 7, 10 and 11
- Google Pixel
- Galaxy S9.

Various examples of multiple screen sizes on different pages of the site can be found [here](https://github.com/Magnusson95/Dance-Your-Way/tree/master/wireframes)

Javascript tested through user testing during each stage of writting. Including confirmation of API connection, API verification, API customisation and user testing of jQuery with Google Chrome Developer Tools.

Google Maps API saw no major issues. The Code Institute training was used to implement this API and then further customisation was done through the Google Maps API documentation, meaning no bugs occurred during testing.

Google Maps Geocode API saw no major issues. Testing of multiple addresses showed that the API successfully distinguished the closest related geocode possible. Where the API fails due to false address input, this is caught before the form is submitted, requiring the user to resubmit a new address.

Email JS API saw some minor issues with verification of the API link, this was rectified through resubmitting the API link. Bug messages were built in for successful or unsuccessful runs of the API. This was tested in a number of ways, from various devices and consol messages were checked.

- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

- JavaScript

  - [JS Hint](https://jshint.com/) - All scripts were checked with JS Hint. All errors were solved, only received a handful of warnings for code only available in ES6.

- Python
  - [PEP8](http://pep8online.com/) - The Python scripts were checked with pep8online. All the errors were solved.

##### Issues and Resolutions

- Font sizes became too large for Mobile view. Fixed this by adding vw sizes
- Google Maps API Javascript code would not read the original data being pulled from MongoDB. Fixed this by creating it as a separate variable in the Python code and converting to a list so Javascript could read it

# Deployment

You will need the following tools installed on your system:

- [Python 3](https://www.python.org/downloads/)
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/download/)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

## Local Deployment

The following instructions are based on use on a Windows 10 OS and IDE VS Code. If your OS is different, the commands may be different, but the process, in general, remains the same.

#### Instructions

- Save a copy of the Github repository located at https://github.com/Magnusson95/Dance-Your-Way.
  - Unzip the repo into the chosen folder.
- If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/Magnusson95/Dance-Your-Way
```

- Within the chosen directory, create a virtual environment with the command:

```
python -m venv venv
```

- Activate the virtual environment with the command:

```
.\venv\bin\activate
```

- Install all required modules with the command:

```
pip install -r requirements.txt
```

- Create a `.env` file with your credentials:
  e.g

```
  - **MONGO_URI_KEY**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
  - **GOOGLE_ACCESS_KEY**: `your google API key`
  - **ACCESS_KEY_ID**: `your AWS S3 access key`
  - **ACCESS_SECRET_KEY**: `your mailjs access key`
```

- Create a database in MongoDB Atlas called **events_manager** with the following collections:

  - **countries**
  - **events**
  - **organisers**

- Run the application with the command

```
flask run
```

- Open the website at `http://0.0.0.0:8080/`

## Remote Deployment

#### Instructions

To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
- Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
- In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `8080`
  - **MONGO_URI_KEY**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
  - **GOOGLE_ACCESS_KEY**: `your google API key`
  - **ACCESS_KEY_ID**: `your AWS S3 access key`
  - **ACCESS_SECRET_KEY**: `your mailjs access key`
- You are now ready to access the deployed app on Heroku.

## Credits

### Content

- All content was created by me or my fellow dance colleauges:
  - [Gabeto](https://www.facebook.com/Tropicsalsa/)
  - [Gusto](https://www.facebook.com/groups/545395699629121/)
  - [Dance Xplosion](https://www.facebook.com/DanceXplosionSibiu)

### Media

- All media was sourced from the facebook accounts of dance colleagues:
  - [Gabeto](https://www.facebook.com/Tropicsalsa/)
  - [Gusto](https://www.facebook.com/groups/545395699629121/)
  - [Dance Xplosion](https://www.facebook.com/DanceXplosionSibiu)
