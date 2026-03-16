# Medium Task - Shopping Site

This task will involve building a shopping site.

You will start off with some very basic code  and then you will add some more features to make this much more useful.

## Task 1 - Run the Site

Start by running the site, navigating around, and seeing what there is already.

## Task 2 - Adding some Products

At the moment, there is only 1 product in stock. You can get rid of this and add your own products, and should make sure there are at least 10 products in your shop.

You can pick what you want to stock, and you will need to:
- add a row into 'products.csv' for each one
- add an image to the images folder
- put the filename into the 'img' column of products.csv

Once you've added some items, re-run the site and check whether it still shows up the same as before.
You will now need to **edit the template and the route** to ensure all products are printed, not just one.

Try changing stock quantities in the csv - read the code and predict what happens when the stock = 0.

## Task 2.5 - Changing Colours / Styles

There is a bit of CSS generated for this website, but it's very plain and needs some work to look good. Now you know what kind of shop you are making, you may want to add some more styling to ensure that your website looks good.

in static/style.css you will find many colours which you can change. You can experiment, change different things, see what happens with all the code - if it all goes wrong, you can always revert to a previous commit.

For colours in particular, [Coolors](https://coolors.co/2f6690-3a7ca5-d9dcd6-16425b-81c3d7) is a good tool for finding colours and colour schemes. Just press space to randomise - you can lock in colours by pressing the padlock icon and this will keep those colours when you regenerate, and find colours which go with your chosen ones.

Be mindful of **contrast** in your colour scheme - text should always have a high contrast against its background, and you should avoid using red and green on top of each other as red-green colourblindness is very common.

You can also do things like:
- make an image background
- make a gradient background

## Task 3 - Adding Single Page View

In `product.html` there is a template set up for viewing an individual product - you need to add to the route for 'product' to:
- get the right product out of the list
- render the correct template, passing any required information.

You can also re-style this to fit your site's aesthetic.

## Task 4 - Ordering

At the moment, our shop doesn't work as a shop.

You need to add a way of ordering products.

There are two different ways of doing this - one is easier, one is better.

### Easy way:
Add to `product.html` so that there is a button which calls the `order(id)` route, and add to the route so that it:
- ensures the product has enough stock - if it doesn't, give the user some error - you could even make a new template for this.
- adds a new row to the order csv
- reduces the stock of the item in the products csv

### Better way:
Create a basket system so that users can order multiple items. You will need to:
- add a data structure which represents a shopping basket
- add buttons to add items to the shopping basket
- add a view & template so you can see the shopping basket and its contents
- add an order button
- check stock to validate the sale, then update the order and product csvs
- empty the basket.

For both options, you should also add a view which allows staff to see a list of orders.

## Task 5 - Extension

Now you have a basic, functional shop - you could:
- add more to the products
- test your site to ensure it is bug free

Or if you want more of a challenge - there are lots of other features you can add:
- a form to allow users to enter an address when they order: [flask-wtf docs here](https://flask-wtf.readthedocs.io/en/1.2.x/form/) or [DigitalOcean guide](https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application)
- create a relational database instead of using csv files: [sqlalchemy and models](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)