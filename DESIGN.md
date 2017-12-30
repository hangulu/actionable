## actionable's Design

### Tools
**actionable** was developed using Python, the Python microframework, [Flask](http://flask.pocoo.org), some Javascript, and a lot of HTML and CSS. Much of the aesthetic design of **actionable** is due to the [Bootstrap](https://getbootstrap.com) front-end component library.

## Development Steps

#### Step 1: The Drawing Board

Before I began to code any of the application side of **actionable**, I spent a considerable amount of time, with pen and paper, laying out the look of the website. I knew I wanted to use the Bootstrap navigation bar, but with a few key design differences (like transparency, having the linking elements to the rights, etc), and I knew what I wanted my three pages to look like. In true minimalist and private fashion, I wanted to keep things as simple as possible, visually, so as not to distract the user from their goal – ultimately, the user visits the website/app for a few minutes to make plans and learn up, then they leave. It was never my intention to entertain with images, or video, but to provide users with a quick way to access relevant information.

#### Step 2: HTML and CSS

I used some of the CSS and HTML code from my solution to CS50's PSET8, with many changes. **actionable** needed to be responsive (and smoothly scalable for multiple screen sizes), so I learned how to use different units for CSS (vh, rem, em, etc), and converted the units accordingly. I radically changed the layout and design of the HTML pages to center text and make information as clear as possible. I used bright, but not distracting, colors to keep users engaged and to make it visually pleasing. I also decided that I needed new fonts that reflected my artistic mission for simplicity.

### Step 3: The Application – The Protest Finder

This aspect of the development process gave me the most pause when I was thinking about it initially. I knew that one way to get "protests" would be to scrape Facebook events that matched given search queries, so I went with that. It was difficult to find some information about how to do this (especially since this type of project is so unique), but I scraped through the one [tutorial](https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999) I could find, and the documentation for the [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/) to get the necessary tools to do my extraction.

I signed up for a Facebook developer account, got a token for this app, then proceeded to write a python module and function, `get_events` and `lookup_event`, to find events that the user wanted. I am quite familiar with pandas dataframes, so I decided to use that as my data structure – they're fast, easily searchable, and have easy and intuitive ways of filtering and filling in missing data.

The final aspect of this was the main module, `app.py` which runs the entire website using Flask. It gets user input from the HTML forms, and renders all the HTML templates. The function `lookup_event` is in the `protests` function, and it is used there to get the events that the user inputted on the `/protests` page. It also looks up zipcodes in a database of places in `actionable.db`, to ensure accuracy.

I decided to use Python and Flask because I wanted to push the limits of my own knowledge. I initially set out to learn a new language and implement the application and website that way, but ultimately, my goal was to create a good and useful website, not necessarily to cram a new language to try to do so. Hence, I used the tools that were already at my disposal, and invested saved time into making this project as successful as possible.

## Omitted Initial Ideas
Initially, I wanted to provide users with a way to login to the website and save their data, user forums, and the ability to add a distance radius to their searches. The distance radius addition proved a bit too difficult to implement with the Facebook events implementation, which is why I omitted it. However, after doing more research into protests and providing tools for protests, I learned that privacy is significant, and outweighs the ability to login or save data. Hence, I made the form as light as possible, so that users can easily input the same information to get their results, and omitted user forums (which would give little use in the age of Facebook Messenger, iMessage, and WhatsApp).

## Author
**Hakeem Angulu**, Harvard College Class of 2020
[hangulu@college.harvard.edu](mailto:hangulu@college.harvard.edu)

## Acknowledgments
I'd like to thank all who helped and inspired me to tackle this project, including:
* The CS50 Staff, especially my TF, Derek Wang
* My friends and family, who kept me sane during the development process
* Websites like [kettle](https://wearekettle.com) and [Laura Makes Stuff](http://www.lauramakesstuff.com/) for the design inspiration
