## actionable
**actionable** is a website/web application that gives users the ability to find protests and gatherings around issues that they care about, near their inputted location, and within a specific timeframe. **actionable** also gives users common tips and tricks for protests (before, during, and after them), and access to current events via a newsfeed.

## Motivation
I am extremely interested in social movements, and how they are born and thrive. However, as someone who loves going to protests myself, I know how hard it is to find a centralized place where one can find these gatherings that match one's interests, and furthermore, how hard it is to get advice on _how_ to protest. It was also incredibly important to me that this resource remained detached from any sort of account system, or tracking – privacy, especially when it comes to social movements, is paramount. So, I set out to create that place: **actionable**.

## Build status
[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=bv-test-build-on-edge)](https://travis-ci.org/travis-ci/travis-web)
 
## Screenshots
**actionable** logo:
![logo](https://image.ibb.co/cebvhw/actionable_logo2.png "actionable logo")

Homepage:
![homepage](https://image.ibb.co/bZB1sw/homepage.png "Homepage")

Protest Finder:
![protest](https://image.ibb.co/b10GQG/protestform.png "Protest Finder")

Resources:
![protest](https://image.ibb.co/md5peb/resources.png "Resources")

News:
![protest](https://image.ibb.co/ighkKb/news.png "News")

## Features
**actionable** has the following features:
1. Protest Finder – Search for protests that you care about near you.
2. Resources – Find handy resources to keep you safe and maximize your protest efficacy.
3. News – Stay on top of current events, and find links to some of the most reputable news sources.
4. Dynamic scaling of content for all screen sizes.

## Prerequisites
One needs the following libraries to be able to run **actionable**:
* urllib3
* facebook
* requests
* pandas
* datetime
* Flask
* Flask_Session
* sqlite3

To install these libraries, use [pip](https://pip.pypa.io/en/stable/#), then in a new terminal window, type:
`pip install [library]`.

## Installation
In a new terminal window, execute the following commands, replacing the element in the square brackets with the path of the actionable folder:
```
cd [actionable folder]
export FLASK_APP=app.py
flask run
```

To visit the website, go to the outputted url.

## Tests
Describe and show how to run the tests with code examples.

## How To Use
One can navigate the website intuitively, especially the index, resources and news pages. The application aspect, the protest finder, is used as follows:
1. Navigate to the protests page, usually by using the navigation bar at the top.
2. Scroll down, then fill out the form as follows:
3. Select your protest issue.
4. Input your five-digit zipcode. If your zipcode is invalid, the site will take you back to the homepage.
5. Select your desired timeframe.
6. Click the button that says `Find Me Some Protests`.

Then, one will be able to see the protests that matched one's selections.

## Author
**Hakeem Angulu**, Harvard College Class of 2020
[hangulu@college.harvard.edu](mailto:hangulu@college.harvard.edu)

## Acknowledgments
I'd like to thank all who helped and inspired me to tackle this project, including:
* The CS50 Staff, especially my TF, Derek Wang
* My friends and family, who kept me sane during the development process
* Websites like [kettle](https://wearekettle.com) and [Laura Makes Stuff](http://www.lauramakesstuff.com/) for the design inspiration
