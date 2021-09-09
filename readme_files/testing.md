## Testing
* [Responsiveness](#responsiveness)
* [General](#general)
    * [Navigation](#navigation)
    * [Button "Top of Page"](#top_of_page)
    * [Footer](#footer)
* [Home](#home)
* [Products](#products)
* [Shopping Bag & Checkout](#bag-checkout)
* [Account](#account)
    * [Registration & Login](#registration_login)
    * [Profile & Order history](#profile_orderhistory)
    * [Product Management](#product_management)
* [Blog](#blog)
* [Contact](#contact)

**Back to [Readme.md](README.md)**

****

## Responsiveness

![responsivness](readme_files/AmIResponsive.png)

I tested the site on various browsers such as Google Chrome, Mozilla Firefox and Safari, mobile phones, both android and iOS, tablets. laptops and desktops. The site is responsive from small mobile phones of 360px up to desktops with 2K. Larger screens of 4K makes the images a bit small and centered in the middle with some blank space on either sides. 


| **Functionality**                   | **Anticipated Outcome**                 | **Actual Outcome** | **Pass/Fail** |
|-------------------------------------|-----------------------------------------|--------------------|---------------|
| Watching on mobile device           | Images adapted, no overflow             | As Expected        | P             |
| Watching on tablet device           | Pages rendering properly, no distortion | As expected        | P             |
| Watching on laptop device           | All in order, no distortion             | As expected        | P             |
| Watching on desktop device up to 2k | All in order, no distortion             | As expected        | P             |


## General

### Navigation

| **Functionality**                                                 | **Anticipated Outcome**                                   | **Actual Outcome** | **Pass/Fail** |
|-------------------------------------------------------------------|-----------------------------------------------------------|--------------------|---------------|
| Clicking on Logo                                                  | Home page opens                                           | As Expected        | P             |
| Clicking on  All Products, Posters, Frames or Special Offer links | Dropdown tab with links are opened for each               | As expected        | P             |
| Clicking on Account link                                          | Dropdown tab with links are opened for Login and Register | As expected        | P             |
| Clicking on Logout link (once Logged in)                          | Logs out user and directs to Login page                   | As expected        | P             |
| Clicking on Shopping bag Icon                                     | Shopping bag opens and shows current selection            | As expected        | P             |


### Top of Page (only mobile and tablet devices)

| **Functionality**            | **Anticipated Outcome**       | **Actual Outcome** | **Pass/Fail** |
|------------------------------|-------------------------------|--------------------|---------------|
| Clicking on Go to Top button | Scrolls up to top of the page | As Expected        | P             |


### Footer

| **Functionality**          | **Anticipated Outcome**                 | **Actual Outcome** | **Pass/Fail** |
|----------------------------|-----------------------------------------|--------------------|---------------|
| Clicking on Contact Us     | Opens email modal to contact site owner | As expected        | P             |
| Clicking on Journal        | Opens blog page with all posts listed   | As expected        | P             |
| Clicking on Facebook icon  | Opens Facebook website in new tab       | As expected        | P             |
| Clicking on Instagram icon | Opens Instagram website in new tab      | As expected        | P             |
| Clicking on Pinterest icon | Opens Pinterest website in new tab      | As expected        | P             |
| Clicking on YouTube icon   | Opens YouTube website in new tab        | As expected        | P             |


## Home

| **Functionality**          | **Anticipated Outcome** | **Actual Outcome** | **Pass/Fail** |
|----------------------------|-------------------------|--------------------|---------------|
| Clicking on Explore button | Opens the Products page | As expected        | P             |


## Products

| **Functionality**                                                          | **Anticipated Outcome**                                                                                | **Actual Outcome** | **Pass/Fail** |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------|---------------|
| Clicking on Sort by button                                                 | Shows products under that Category                                                                     | As Expected        | P             |
| Clicking on Product image                                                  | Shows Product Details info on a new page                                                               | As Expected        | P             |
| On detail page selecting the number to purchase  and clicking "Add to Bag" | Adds the selected quantity of the item to cart and then opens a toast where you see your shopping cart | As Expected        | P             |


## Shopping Bag & Checkout

| **Functionality**                               | **Anticipated Outcome**                                                          | **Actual Outcome** | **Pass/Fail** |
|-------------------------------------------------|----------------------------------------------------------------------------------|--------------------|---------------|
| Changing quantity and clicking on Update button | Changes quantity of product and shows Shopping Cart page.                        | As Expected        | P             |
| Clicking on Checkout button                     | Opens Shopping cart page where you fill in your delivery and payment information | As Expected        | P             |


| **Functionality**           | **Anticipated Outcome**                                                           | **Actual Outcome** | **Pass/Fail** |
|-----------------------------|-----------------------------------------------------------------------------------|--------------------|---------------|
| Shows current order summary | All chosen products are shown in summary                                          | As Expected        | P             |
| Shipping and payment form   | All info saved in profile is shown except card payment                            | As Expected        | P             |
| Shipping and payment form   | If new customer, blank to be filled in, with checkbox if you want to save profile | As Expected        | P             |
| Complete Order button       | Gives you a success message that order is completed and an email has been sent    | As Expected        | P             |


## Account

### Registration & Login

| **Functionality**                                      | **Anticipated Outcome**                                                                                                         | **Actual Outcome** | **Pass/Fail** |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------|
| Clicking on Registration button                        | Registers the user and redirects to confirm email address. If registration form is incomplete, shows Please fill out this field | As Expected        | P             |
| Clicking on LogIn with correct username and password   | Directs user to the index page                                                                                                  | As Expected        | P             |
| Clicking on Login with Incorrect username and password | Message to user showing incorrect username or password                                                                          | As Expected        | P             |
| Clicking on Logout button                              | Logs out user and rdirects to index page                                                                                        | As expected        | P             |


### Profile

| **Functionality**               | **Anticipated Outcome**                                 | **Actual Outcome** | **Pass/Fail** |
|---------------------------------|---------------------------------------------------------|--------------------|---------------|
| Clicking on Edit Profile button | Opens Edit Profile page                                 | As Expected        | P             |
| Clicking on Update button       | Saves changes to profile and redirects to Profile  page | As Expected        | P             |
| Show order history              | Shows user's previous orders with all information       | As Expected        | P             |

### Product Management

| **Functionality**                                                           | **Anticipated Outcome**                                                                                              | **Actual Outcome** | **Pass/Fail** |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|---------------|
| Clicking on Product Admin (admin functionality only available to superuser) | All products can be edited or deleted                                                                                | As Expected        | P             |
| Clicking on Edit                                                            | Form with prefilled current description and SKU, can be edited with new info and then saved on Update product button | As Expected        | P             |
| Clicking on Delete                                                          | Form with question if you are sure you want to delete                                                                | As Expected        | P             |

## Blog

| **Functionality**                                        | **Anticipated Outcome**                                                                      | **Actual Outcome** | **Pass/Fail** |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------|---------------|
| Clicking on Read More link                               | Shows blog post on a new page                                                                | As Expected        | P             |
| Click on Add Comment                                     | Shows a new page with comment form                                                           | As Expected        | P             |
| Clicking on Edit and Delete buttons (only for superuser) | Shows a Edit Post form or Delete page where you are asked again to verify you want to delete | As Expected        | P             |

## Contact

| **Functionality**                                 | **Anticipated Outcome**                                                     | **Actual Outcome** | **Pass/Fail** |
|---------------------------------------------------|-----------------------------------------------------------------------------|--------------------|---------------|
| Filling out form with contact details and message | All fields are required and show prompt to fill out if left blank           | As Expected        | P             |
| Clicking on Send Message button                   | Message pops up confirming your message is sent and to expect reply shortly | As Expected        | P             |


**Back to [Top](testing.md)**