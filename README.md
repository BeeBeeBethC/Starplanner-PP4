# Starplanner - Portfolio-Project-4

# Contents

* [What is MOTech](#what-is-MOTech)
    * [What-is-Starplanner?](#what-is-Starplanner)
    * [Why-use-Starplanner](#Why-use-Starplanner)
* [User Stories]()
* [Existing Features](#existing-features)
    * [Future Implementations](#future-implementations)
    * [Technologies and Libraries Used]()
* [Data Model](#data-model)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Clone The Repository](#how-to-clone-the-repository)
    * [How To Create A Fork](#how-to-fork-the-repository)
    * [Deployment to Heroku](#heroku-deployment)
* [Credits](#credits)
    * [Content](#credits)
    * [Media](#credits)

## What is MOTech?
MOTech or Motion Optimised Technology are a small, hypothetical 'start-up' IT Company who have asked me to create a Django based, Task Management System. They wanted the app to have some specifics. MOTech wanted to have individual user logins, The ability to switch planner views from all tasks to their individual user tasks. The ability to select task priority between low, medium and high. Minimalist in design and be easy to use.

This is where Starplanner was born.

## What is Starplanner?
Starplanner is a work management, planner app that allows users to Create, Update and Delete their own tasks as well as being able to 'Read' tasks that fellow work colleagues are working on.

## Why use Starplanner?

The aim of Starplanner is to provide a task management system that all users of MOTech can individually and collectively work on.

## User Stories

For Starplanner, Agile principles were used to track and monitor the progress of the project. user stories were documented as issues on GitHub. Agile also included the use of GitHub's Kanban project board. The MoSCoW technique used to prioritize tasks, features or requirements for a project split into four columns, Must-have, Should-have, Could-have and Won't-have more information on MoSCoW methodology can be found here: (https://www.techtarget.com/searchsoftwarequality/definition/MoSCoW-method)

## Existing Features

login, logout, sign up abilities, 
create, read, update and delete tasks 
comments automatically added to track when tasks where created and updated.
access restrictions. users must be registered to view tasks and can only update and delete their own.

please note: some of the following screenshots were taken during the project and once deployed. 

## Future Implementations
future implementations: other companies can use it


## Technologies and libraries used in Starplanner
* Gitpod - coding workspace
* Github - storage and commit history
* Heroku - hosting platform for Starplanner
* Replit - used to aid with debugging.

### Languages

Html, CSS, Javascript, Python and Django

### Libraries used 

Bootstrap - for aid with styling and keeping consistency throughout
Crispy Forms - for aid with form styling and form validation

## Data Models

INSERT ERD HERE

## Testing

Full testing documentation can be viewed in the TESTING.md file. 

## Deployment Instructions

Starplanner was deployed to both Github and Heroku.

The reason for deploying to Github as well as Heroku was to monitor version control and commits throughout the project.

### Github Clone
To clone a copy of Starplanner from the Github repository, please follow these steps:

1. Go to the repository you wish to clone, project link is as follows. (INSERT PROJECT LINK)

2. Click on the green button that reads 'Code'.

3. On the dropdown menu, please select the 'Copy URL to clipboard' option this button looks like two squares overlaying one another.

4. Open your favourite code editor, for myself it is Visual Studio Code. on Visual Studio Code, click the 'source control' button from the left hand menu.

(Alternatively, open the terminal and change your working directory to the location of the cloned repository.)

5. Paste the repository URL into the top navigation bar of Visual Studio Code.

(Alternatively type 'git clone' into the terminal and paste the URL link.)

6. Save the repository to a localised folder where the repository will be stored on your computer.

7. Click on select repository location.

8. Let the repository download and click 'open' when the on screen prompt shows in the lower right corner of the screen.

### Github Fork

To fork the repository of Starplanner, please follow these steps.

1. Sign up or login to Github.

2. Go to the repository for Starplanner (INSERT PROJECT LINK)

3. Click the fork button on the top right hand side of the screen.

PLEASE NOTE: The steps followed above will provide the code only. To access the project from Heroku, please continue to follow the steps below.

### Heroku Deployment

The live link to Starplanner can be found here (INSERT PROJECT LINK)

To deploy to Heroku, please follow these steps:

1. Create your list of requirements by navigating to the requirements.txt file. each package is known as a dependency so therefore should be located in this file when uploading to heroku so that Heroku can still open projects.

2. To create your list of requirements, type in the gitpod (or code terminal of your choice) "pip3 freeze > requirements.txt" ensuring you have the exact same spelling, all lower case for the exact file name or this will not work.

3. Commit and push most recent code upto github.

4. If not done already, Sign-up or Login to Heroku.

5. Navigate to your Heroku dashboard.

6. From the Heroku dashboard, create a new app and name it. Each app name needs to be unique or it won't accept it.

7. Select region.

8. Make sure your settings have been set before you deploy.

9. If settings are not declared, here are the steps for checking settings before deployment.
    1. Find the config vars section. (these are environmental variables section found in heroku settings). In this tab "Reveal config vars" this is where you put sensitive information for example creds.json that can't be shown publicly.
    2. (For Code Institute Students only) For more compatibility, also add another config var to heroku settings which is a port key: PORT value is 8000. This ensures a much smoother deployment as projects may not deploy if this is missed out.

10. Navigate to add build pack and Select "Python". Click save changes then find "node.js". select and click save changes.
NOTE: If these two packages are the opposite way round you can click and drag them so that python pack is on top and node.js is below python.
This step is important to ensure the project will be set up properly.

11. For this project there is the choice of automatic deployment or manual. For Starplanner the author has chosen to manually deploy it which means that it won't automatically update from pushed changes but it does show deployment logs along the way.

12. To manually update and re-deploy the project using the main branch:
    1.  Firstly make sure your most recent changes have been pushed to github and confirm these before moving onto the next step.
    
    2.  Navigate back to project overview and select the deploy option from the navigation menu at the top of the page.
    
    3.  Scroll down the deploy page until you reach manual deploy.
    
    4.  Choose branch to deploy, make sure it's the main branch.
    
    5.  Click the deploy button. (return to follow steps 13 onwards)

13. Once the project has been deployed you should recieve a message stating that "Your app was successfully deployed" and you should be able to click 'view' that takes you to the application terminal where your code is running in Heroku.

14. In the heroku terminal there is no need to run "python3 run.py" command as the programme is already running. After exiting the application, in order to restart this programme you can click the red button at the top that states "run programme" with a play symbol on it.

## Credits
### Content


### Media
Screenshots used in this project are all authors own.
### Acknowledgements

I would like to say a huge thank you to my family and friends for the continual support.

I would like to say a huge Thank You to my awesome Mentor Luke Buchanan. for his guidance through out this project and previous projects completed.

I would like to send a shout out to Kera Cudmore who provides an excellent readme document that I continually to use for guidance for my own readme documents.

I also would like to thank all staff members at Code Institute.