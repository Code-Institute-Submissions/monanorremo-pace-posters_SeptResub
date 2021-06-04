#Pace Posters


Live Page  [Pace Posters](https://mno-pace-posters.herokuapp.com/)


## Table of Contents

* [Inspiration](#inspiration)
* [UX - 5 Planes](#ux——5-planes)
  * [The Strategy](#strategy)
    * [User Stories](#user-stories) 
  * [Scope](#scope)
  * [Structure](#structure)
	* [Database Schema](#database-schema)
  * [Skeleton](#skeleton)
    * [Wireframes](#wireframes)
* [Surface](#surface)
   * [Existing Features](#existing-features)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Credits](#credits)


## Inspiration

I chose to build an e-commerce site to see how hard it actually is to create a site that can be descriptive, easy to navigate, user-friendly.

I currently work at a retailer and they launched their e-commerce site in 2016!!!! The company is over 100 years old and the largest department store chain in my country. Since the launch I have gotten frustrated whenever i use the site and that&#39;s even with an employee discount.

It has been hard, Ive run in to countless issues in the process, but Im so grateful that I am somewhat happy with my result even as an MVP.

## UX - 5 Planes

### Strategy

A site that lets the products speak for themselves in a minimalistic packaging. Posters in various sizes split up in different categories and frames to match. A shopping site that will satisfy the purchasing needs of shoppers on desktop, tablet or mobile phone devices.

Posters are best bought from an e-commerce site, as a shopper you are at home and can visualise your walls after buying some nice posters in different sizes to create beautiful art walls.

For the e-commerce site owner and staff the admin section will make it easy to update, add and delete products. The Django admin site makes it easy for the super user to get an overview of the site. products, details, registerred customers, what&#39;s trending on the set etc.

### User-Stories

As a shopper:

	1.	View all products to enable me to make a purchase
	2.	View a specific category to find what i am looking for easier than to look at all product.
	3.	View product details, so that i can see price, description, rating, image and available sizes.
	4.	See deals, clearance items, special offers if that is the type of purchase I want to make.
	5.	Easily view the total of my shopping cart in all different parts of the site.
	6.	Sort all products in a desired way by ranking, name, price and category.
	7.	Sort a particular category to see ranking, name, price within
	8.	When searching to be able to quickly see how many results there were in my search and the products within my search.
	9.	Choose a size and quantity with ease and be sure that it is clear what my selection is.
	10.	View my shopping bag, with product, size and quantity and see total cost of my bag.
	11.	Easily adjust the quantity of items in my bag before paying.
	12.	When purchasing i want to quickly be able to enter my payment information and place my order.
	13.	Easily login/logout and register an account.
	14.	Recover my password with ease if I forget it.
	15.	Be sure that my personal and financial information is secure.
	16.	Be able to save my personal information in my profile.
	17.	Get an order confirmation after checkout so that everything is correct.
	18.	Get an email confirmation that my purchase has been received and my order will be fulfilled.
	19.	When I return to shop more I want my information details be saved and shown when i fulfill my next order.
	20.	When i return I would like to see my order history.

As a Store Owner:

	1.	I want to be able to add products.
	2.	I want to be able to delete products.
	3.	I want to be able to edit products.
	4.	View shoppers shopping patterns.

### Scope

When designing the page, I wanted for the user to have a clear and positive experience and for the web-site to be easy to use. User can navigate through the navigation bar that is always visible on desktop and mobile and by links in the footer. They can go from any part of the web-site to any other part. Simple to navigate and intuitive.

Design

The website structure is simple so that the posters can pop out and draw in the user. Where there are colours I have used nude and beige tones to match the Main background Image of a perfect art wall. Something the user could strive for and shop the selection in the inventory.

Fonts

I have chosen to pair Montserrat for the Logo, Headings and Navbar. This paired with Raleway for Product details, prices etc is a great pairing.
All fonts are from Google fonts.

Icons

All the icons used in this app are from the newly extended Bootsrtrap Icons, Shopping-bag, Search, Chevron, Tags, Star, the Plus and Minus icons. I used a few Font Awesome icons, one of which is for the spinner icon.

Features Included:

- Navbar included on all pages.
- On the left side is the Pace Posters Logo, in desktop view.
- On mobile view the menu is behind the hamburger icon where you easily click forward to all the different landing pages.
- On desktop, you have the categories: All Products with subcategories:by Price, by Rating, by Category, All Products, Posters with subcategories: Animals, Architecture, Botanical &amp; Nature, Colourful, All Posters, Frames with subcategories: Picture Frames, Poster Hangers, All Frames, and Special Offers with subcategories: New Arrivals, Deals, Clearance, All Specials, centrally located on the navbar.
- Search bar is centrally located on the top middle in the navbar so thet users can look up what they are looking for.
	
Based upon the strategy and research, some design features that I aim to include are:
- Search bar for customers to search for an item that they are looking for.
- Shop by category which takes the customer to products for a specific category they are looking for.
- A shopping bag for customers to add their products and see what the total charges will come to.
- A Special features area for the customers to see if there are any new products, deals, clearance on the site since they last visited.
- Profile page for customers to save their delivery details and see their previous orders.
- **Contact** section for customers to query anything which is not covered on the website itself.
- **Blog** section to inspire and guide the customers to streamline the user experience all the way home.
- On each product page the ability to sort the products by name (A-Z), price (high to low), rating (high to low) or category (A-Z).


### Structure

The site will be structured in a linear grid format, which will match up nicely with the recurring rectangles of the posters and frames.

The site will have a similar layout to the websites Ive researched. With this the site ensures that the customer experiences duality to other sites in the market. 

Keeping the layout consistent across all pages to keep a consistent and clean UX.

**Database Schema**[here](read.me files/models.pdf


### Skeleton

Insert Wireframes

### Surface 

#### Existing Features

Navbar

- All pages throughout have the navbar for shopper convenience.
- Pace Posters logo on left side next to all products and shop by category link.
- All products link will link to all products page.
- Shop by category will be a full width dropdown with links to categories botanical&amp;nature, colourful, architecture, animals.
- Search bar in centre of navbar which will allow customers to search for keywords found in product names or descriptions.
- Right hand logos will feature links to my account pages and cart page.
- My account when logged in as superuser will dropdown links to product admin, help admin, my profile and logout.
- My account when logged in as user will dropdown links to my profile and logout.
- My account when not logged in will dropdown links to register and login.
- In tablet view or smaller, all links will be contained in a burger dropdown icon on the right side and the search bar will be below the navbar full width.

**Footer**

- All page will contain the same footer.
- Social media links in center, to Facebook, Instagram and Twitter.
- Link to contact us page on right.
- Journal page which is an inspirational blog with helpful tips.

**Home Page**

- A full height and width background art wall image.	
- A central elevator pitch "Get inspired and discover our collections now" and below "Explore".

**Product Pages**

- Displaying all products or a specific products from each category.
- Title squares informing what products are displaying.	
- On the left will display the number of products d- laying.	
- On the right will be a dropdown menu for the user to sort products by:	
- Price (low to high)	
- Price (high to low)	
- Name (A-Z)	
- Name (Z-A)	
- Rating (high to low)	
- Rating (low to high)	
- Below will display a grid containing each product. The grid will display 3 items on each row on tablet or larger and 1 item per row on mobile.	
- Each item will display the product image, product name, product price and a button to view further details of the item.	
- An edit and delete link will be shown for superusers, edit link will take the superuser to the edit product page and delete will remove the item.	
- At the bottom right a return to top circular button.
		
**Registering And Authentication**

- The site uses the Django allauth pages for registering and authentication.

**Product Detail Page**

- Will display a larger product image on the left and information on the right, and in mobile view product image at the top and below the product information.
- Product information will include title with the name of the product, product price, product description, product dimensions available in a dropdown box, delivery cost, a form to increment / reduce quantity and buttons to `add to cart` and `keep shopping&`.
- For super users below the title links will display for superusers, edit link will take the superuser to the edit product page and delete will remove the item.

**Profile Page**

- Profile page will only be accessible for logged in users.
- Will display the central heading 'My Profile".
- Subheading below displaying "Delivery Information"
- Below will be a central Django crispy form, which will be prefilled if the user has ticked the "save this information to my profile" checkbox on the checkout page. The form will contain:
- Phone number	
- Street address 1	
- Street address 2	
- Town or city	
- County	
- Postcode	
- Country (dropdown)
- Centered button "Update information"
- Suheading "Order history"
- A table containing the users previous orders.
- The columns for the table will be order number, date, items and order total.

**Shoppingcart Page**

- Displaying all products that have been added to cart.
	⁃	
- Centered title "Shopping Cart"
- A table containing the users products added to cart.	
- The columns for the table will be product info, price, quantity and total.	
- Product info will contain the product name and image.
- Quantity will be a form to increment / reduce quantity.
- Total will be product price multiplied by quantity.	
- At the bottom of the table will be delivery (calculated using delivery policy)
- A link to the delivery policy on the help centre page.	
- Subtotal which will be total of all the items plus delivery cost.	
- Grand total will be delivery plus subtotal.	
- Below buttons to "keep shopping&" and to "secure checkout".
- If there are no items in the cart, a subheading will display 'Your cart is empty' and a 'keep shopping' button.

**Checkout**

- Centered title 'Checkout'
- If the user is not registered or logged in, 'Register / Login' will display and buttons to link to register and log in pages.
- In laptop and tablet delivery information will be a left column and order summary on the right.
- In mobile view Order summary will display above delivery information.
- Delivery information will be form with a subheading &'Details' and containing name and email address and below a crispy form with the heading 'Delivery' and the fields:
- Phone number
- Street address 1	
- Street address 2
- Town or city
- County
- Postcode	
- Country (dropdown)	
- If the user is a logged in user, at the bottom of the form will display 'Save this delivery information to my profile' with a checkbox, when the user ticks the checkbox the delivery information will be saved to their profile.
- Below a stripe payment field will display a button to 'adjust cart', which will take user back to cart page and 'Complete order' which will send payment to stripe.	
- Below buttons will display 'Your card will be charged (amount)'	
- The order summary will display subheading of 'Order Summary and will display the information:	
- Product image	
- Product name
- Quantity
- Item total	
- Subtotal	
- Delivery	
- Grandtotal
	
**Admin Add / Edit Products**

- Add / Edit product page will be the same layout. and close in style to the checkout page as well.
- Only accessible as superuser.	
- Will edit or add products that user enter into form.	
- Centered title Product Administration	
- Subheading Add / Edit Product	
- Central form containing:	
- Sku
- Name	
- Description	
- Price
- Size in dropdown box	
- Image
- Edit page will display the current image.
- Both will display a button to 'Select Image.'
- Edit page with display central buttons 'Cancel' and 'Update'
- Add page with display central buttons 'Cancel' and 'Add Product'
	
**Toasts**

- Toast messages will appear on the top right when the user completes different actions in the categories: info, warning, success and error.

Features left to implement:

Contact Us form or users to message any questions or feedback.
A pop up model for superuser when deleting products to make sure products arent deleted accidentally.

### Technologies Used

**Languages**

- HTML: for the site structure.	
- CSS: for adding styles to the website.	
- Javascript: to add the website interactive features.
- Python: to handle the backend functionality.
	
**Libraries and Frameworks**

- Django
- Bootstrap
- Jquery

**Databases and Storage**

- SQLite3: for development.
- PostgresSQL: for deployed website.
- AWS: for storing static files.

**Payments**

 - Stripe: Used to handle the payments at checkout.

**IDE and Hosting**

- Gitpod: Used as IDE environment.
- Git: Used for version control.
- Github: Used for version control and repository hosting.
- Heroku: Used to host live website.

**Tools**

- [Google fonts](http://Fonts.google.com) - 
For the fonts.

- [Jshint.com/](https://jshint.com/) -
For validation of Javascript code.

- [Validator.w3.org](http://Validator.w3.org)- 
For validation of HTML code.

- [Jigsaw.w3.org/css-validator](http://Jigsaw.w3.org/css-validator) - 
For validation of CSS code.

- [Google.com/test/mobile-friendly](http://Search.google.com/test/mobile-friendly) -
 For testing the website mobile responsiveness.

- Google Chrome DevTools - For testing website responsiveness.

- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) - For generating a Django random secret key.

- [Pep8online.com/](http://pep8online.com/) - 
For validating Python code.

- [Favicon.io](favicon.io/) - For creation and implementation of favicon.

## Deployment

### Installation Prerequisites

To be able to run the project the following technologies will be need to be in installed in your IDE environment.

- Python3
- Git
- pip3

You will need to be signed up to the following services:

- [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&amp;gclid=Cj0KCQjwpdqDBhCSARIsAEUJ0hMbGWS3dMlZowadFExUalBu2L\_UVf27xViAk9dBlCKLsRQI7V2PuScaAmCPEALw\_wcB)

- [AWS](https://aws.amazon.com/)

- [Stripe](https://stripe.com/gb)

### Cloning on GitHub

1. Login to GitHub.com.
2. Open monanorremo/pace-posters.
3. Click 'Code' then under 'Clone' copy the link with the HTTPS URL.
4. Go to the terminal in your IDE environment.
5. Change the working directory to where you want the clone to be saved by typing `cd` and the name of the directory.
6. Type `git clone` and paste the copied HTTPS URL.
7. After pressing enter the clone will be saved to your chosen directory.

### Local Deployment On Gitpod

1. After cloning repository on GitHub. Go to your chosen IDE environment and open the clone directory.
2. Install the libraries from the requirements.txt, in the terminal type - `pip3 install -r requirements.txt`.
3. Set your environment variables in your gitPod settings or in an env.py file.
4. If setting variables within an env file add this to the .gitignore file so your variables are not exposed
when pushing to gitHub.
5. Your environment variables will need to be set as follows:
- os.environ[`DEVELOPMENT`] = `True`
- os.environ[`SECRET\_KEY`] = `Your Secret key`
- os.environ[`STRIPE\_PUBLIC\_KEY`] = `Your Stripe Public key`
- os.environ[`STRIPE\_SECRET\_KEY`] = `Your Stripe Secret key`
- os.environ[`STRIPE\_WH\_SECRET`] = `Your Stripe WH\_Secret key`

6. Create the database from the models by typing in the terminal `python3 manage.py makemigrations`. Followed by
`python3 manage.py migrate`
7. Load the data fixtures by typing in the terminal: `python3 manage.py loaddata products`
8. Create a superuser so you can log in to the Django admin by typing in the terminal: `python3 manage.py createsuperuser`
9. The site can now be run locally by typing in the terminal `python3 manage.py runserver`

### Heroku Deployment**

1. After logging in to Heroku, select `Create New App` Choose the region closest to you and select `Create app`.
2. On the resources tab, to provision the database in the add on field search for and select `Heroku Postgres`.
3. A pop up should appear and under `Plan name` use `Hobby Dev-Free` and select `Provision`.
4. Go to your IDE and type `pip3 install dj_database_url` and `pip3 install psycopg2-binary` as these need to be
installed to use Postgres. Also `pip install gunicorn` for the webserver.
5. To make sure Heroku installs all of the apps when deployed save the requirements by typing in the terminal
`pip3 freeze > requirements.txt`
6. Back on Heroku under settings, select `Reveal config vars` and copy the key from DATABASE\_URL.
7. In the project folder on settings.py in the database setting, comment out the current database setting.
8. Replace with:

```
DATABASES = {
    'default': dj_database_url.parse('<Enter the copied DATABASE_URL key here>')
}
```

9. Add the data to the postgres database by typing in the terminal `python3 manage.py makemigrations`. Followed by
`python3 manage.py migrate`
10. Load the data fixtures by typing in the terminal: `python3 manage.py loaddata products`
11. Create a superuser so you can log in to the Django admin by typing in the terminal: `python3 manage.py createsuperuser`
12. Return to database setting in settings.py and remove code added in step 8 and uncomment the previous database setting.
13. Create a Procfile and add `web: gunicorn pace_posters.wsgi:application`
14. Login to Heroku through the cli `heroku login -i`
15. Temporarily disable collect static by typing `heroku config:set DISABLE_COLLECTSTATIC=1`
16. Add `vision-furniture.herokuapp.com, localhost' to ALLOWED_HOSTS in settings.py.
17. The app can now be deployed by typing in the terminal `heroku git:remote -a pace-posters` and `git push heroku master`
18. On Heroku dashboard under "Deploy" set "Deployment method" to connect to Gitub. Under "Automatic Deplays" set 
"Enable automatic deploy" so the code is automatically deployed to Heroku and GitHub.

### Add Static Files to AWS

1. Go to AWS and find S3 under services and create a new bucket, selecting the region closest to you and allowing all public access.
2. Go to the new bucket and under properties tab, turn on static website hosting.
3. Under permissions tab the CORS configuration tab and enter the following:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
4. Go to the bucket policy tab. And select "policy generator" so we can create a security policy for this bucket.
5. Add in the following:
- Policy type: S3 bucket policy
- Effect: Allow
- Principal: `*`
- Action: GetObject
- Copy the ARN from the bucket policy tab. And paste it into the ARN box at the bottom.
- Click Add statement. Then generate policy.
6. Copy the policy into the bucket policy editor.
7. Add `/*` onto the end of the resource key. Click Save.
8. Go to access control list tab and set the list objects permission for everyone under the Public Access section.
9. Create a user to access the bucket by selecting IAM from the services menu.
10. Select "Groups" and select "Create new group". Add in a new group name and click next, next again then "create new group"
11. Create a policy to access the bucket, by selecting "policies" then "create policy". Select JSON tab and import managed policy. Search for s3 and import "AmazonS3FullAccess".
12. Copy the bucket policy ARN from the bucket policy in s3 > permissions. Paste it into the JSON resource key on create policy twice 
giving the second paste a `/*` at the end. Select "review policy". Give the policy a name and description and create the policy.
13. Go to "groups", select the new group, select "attach policy", search for the newly created policy and attach it to the policy.
14. Go to "users", add user, create a user name, give them programmatic access and select next.
15. Add the new user to the group and select next to create user then download the .csv file.
17. Go to your IDE terminal type: `pip3 intsall boto3` and `pip3 intall django-storages` to install the packages 
to connect to django. Type: `pip3 freeze > requirements.txt` so they get installed on heroku when its deployed.
18. Add 'storages' to installed apps on the settings.py file. Add the following code to tell Django which bucket to 
communicate with:
```
if 'USE_AWS' in os.environ:
    # Bucket Config

AWS_STORAGE_BUCKET_NAME = ‘mno-pace-posters’

AWS_S3_REGION_NAME = ‘eu-north-1’

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY_ID')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```


19. On Heroku add the AWS keys from the .csv file to the config vars. Also add USE_AWS: True, so the that the setting file knows 
to use the AWS configuration when deploying to Heroku. Remove the COLLECTSTATIC variable.
20. Push all the changes to Github. Which will trigger an automatic deployment to Heroku.

## Credits

**Tutorials**

- The site is based on the Boutique Ado Code Institute tutorial project.
- The blog is based on tutorial from Youtube Codemy.com https://www.youtube.com/watch?v=B40bteAMM\_M

**Images**

Home background image is from [Poster Store](https://posterstore.eu/)
Blog posts is also from the [Poster Store](https://posterstore.eu/)
All poster images are from [Unsplash] (https://unsplash.com/)

**Acknowledgements**

• Code Institute Slack Channel for valuable guidance and opinions.
• Code Institute tutors for assistance in my times of need.
