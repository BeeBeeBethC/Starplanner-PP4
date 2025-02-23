# Starplanner

This document has been produced due to the extensive testing conducted on this project.

# Contents
* [Full Website Testing](#manual-testing)
* [Automatic Website Testing](#automatic-testing)
* [Validator Testing](#validator-testing)
* [Debugging](#debugging)
    * [Known bugs](#known-bugs)
    * [Resolved Bugs](#resolved-bugs)
    * [Existing Bugs](#existing-bugs)
* [Further Testing](#further-testing)


## Manual Testing
Full Manual Testing performed. results as shown

| Website Feature | Expected Outcome | Testing Performed | Result | Pass or Fail |
| :-------: | :-------------: | :-------: | :-------: | :-------: |
| website displayed login status on homepage | the login status of the user is visible | opened the website | login status shown | Pass |
| burger icon on medium screens | navbar drops down | clicked on the burger icon | navbar dropped down | Pass |
| press 'Login' option on navbar when on medium plus screens | page displays status of being logged in or not, navbar drops down | clicked on login | navigated to page where login status was displayed | Pass |
| login | the sign in form shows up | clicked the login button | sign in form appeared | Pass |
| sign up from login page | the register page appears instead of login | clicked the sign up link | sign up form loaded | Pass |
| form validation | empty forms, passwords less than 8 characters and entirely numeric values throw up an error | input numbers 1-4 and 1-8 as well as passwords less than 8 characters threw errors | validation error occurred (see accompanying screenshots below) | Pass |
| sign in success message | a django message shows successfully signed in as 'username of person logged in' | signed into the website | success message showed up | Pass |
| selecting 'my tasts' as new user | new users will only have the option to create new tasks | clicked 'my tasks' | only create new task button showed up | Pass |
| selecting my tasks as an existing user | users have the option to access their tasks first | clicked 'my tasks' | tasks created by user showed up first | Pass |
| create task | used for task creation | clicked the 'create new task button' | create new task form showed up | Pass |
| create task form input validation | form field validation shows up if users haven't put in enough detail or skipped a field | put varying amounts of content into the create task form | validation showed up (see accompanying screenshots) | Pass |
| update task button and validation (as above) | update button gets clicked and form fields show validation is same as above | pressed the update button put various amounts of content in | update task form appeared validation shown as above | Pass |
| delete task | delete button is clicked verification shows 'do you want to delete this task?' | clicked the delete button | delete validation showed | Pass |
| clicked comments button | comments that are automatically input on creation and update | clicked the comments button | could see the comments that had been made | Pass |
| clicked on someone else's task buttons (update, delete and comment buttons) | modal should show stating that the user doesnt have access to modify the task | clicked the update, delete and comments button | modal appeared, access denied | Pass |
| priotiry shown | each priority category has a corresponding badge | clicked priority in create/update task modes | corresponding badge appeared (red, yellow and green badges) | Pass |
| page navigation buttons | each button changes what tasks display | clicked page buttons | tasks and numbers changed | Pass |
| pressed logout on navbar  | sign out page shows asking if you want to sign out | clicked logout nav link | Logout page appeared | Pass |
| pressed sign out button  | signs user out | clicked the sign out button | user signed out | Pass |
| as super user, users and coresponding tasks get removed from the task view | removes all tasks created from deleted user | deleted user as admin | user and corresponding tasks removed from website | Pass |
|  |  |  |  |  |

## Automatic Testing

INSERT AUTOMATIC TESTING SCREEN SHOTS HERE

## PEP8 validation

INSERT PEP8 VALIDATION SCREEN SHOTS HERE

## Bugs

INSERT DOCUMENTED BUGS HERE

### Solved bugs

TALK ABOUT HOW TO RESOLVE ABOVE BUGS HERE

### Remaining Bugs

ANY REMAINING BUGS? NOPE I DON'T THINK SO!

## Wave Testing

INSERT SCREENSHOTS HERE

## Lighthouse Scores

INSERT SCREENSHOTS HERE

### Further Testing

further testing was completed on:

* A huawei laptop

with no issues identified.

Thank you for viewing the testing.md document for CEDAS.