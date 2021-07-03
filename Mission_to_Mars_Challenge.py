# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # Visit URL
# url = 'https://spaceimages-mars.com'
# browser.visit(url)

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

base_url = 'https://marshemispheres.com/'

html = browser.html
hemisphere_soup = soup(html, 'html.parser')
hemisphere_items = hemisphere_soup.find_all('div', class_=['description'])

hemisphere_items

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemi_image_data = {}

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for hemi_item in hemisphere_items:
    #get url for each hemisphere and pull data
    hemi_url =base_url + hemi_item.a['href']
    
    #get title for each hemisphere 
    browser.visit(hemi_url)
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    hemi_title = hemi_soup.find('h2').text
   
    
    # get image url for each hemisphere
    hemi_image_url = hemi_soup.find('img', class_="wide-image").get('src')
    hemi_image_url = base_url + hemi_image_url
   
    
    hemi_image_data["img_url"] = hemi_image_url
    hemi_image_data["title"]= hemi_title
    hemisphere_image_urls.append(hemi_image_data)


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()





