from splinter import Browser
from selenium import webdriver
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import time 
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
   
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    
    final_data = {}
    #output = marsNews()

    browser = init_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    article = soup.find('div',class_='list_text')
    news_title = article.find('div',class_='content_title').text
    news_p = article.find('div',class_='article_teaser_body').text
    #output = [news_title,news_p]
    
    
    #final_data["mars_news"] = output[0]
    #final_data["mars_paragraph"] = output[1]
    #final_data["mars_image"] = marsImage()
    #final_data["mars_weather"] = marsWeather()
    #final_data["mars_facts"] = marsFacts()
    #final_data["mars_hemisphere"] = marsHem()

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)  
    html = browser.html
    soup = bs(html, 'html.parser') 
    images = soup.find_all('a',class_= "fancybox")
    for image in images:
        featured_image_url = 'https://www.jpl.nasa.gov' + image['data-fancybox-href']

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html = browser.html
    soup = bs(html, 'html.parser') 
    mars_weather = soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    hemispheres_images_url = []
    image_list = soup.find('div',class_='result-list')
    hemispheres = image_list.find_all('div',class_='item')
    for hemisphere in hemispheres:
         title = hemisphere.find('h3').text
         end_link = hemisphere.find('a')["href"]
         image_link = "https://astrogeology.usgs.gov/" + end_link   
         browser.visit(image_link)
         html = browser.html
         soup=bs(html, "html.parser")
         downloads = soup.find("div", class_="downloads")
         image_url = downloads.find("a")["href"]
         hemispheres_images_url.append({"title": title, "img_url": image_url})

    final_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "hemispheres_images_url": hemispheres_images_url
    }
    # Close the browser after scraping
    browser.quit()
    
    return final_data

# NASA Mars News
#def marsNews():
#    browser = init_browser()
#   url = 'https://mars.nasa.gov/news'
#  browser.visit(url)
#    html = browser.html
#    soup = bs(html, 'html.parser')
#    article = soup.find('div',class_='list_text')
#    news_title = article.find('div',class_='content_title').text
#   news_p = article.find('div',class_='article_teaser_body').text
#    output = [news_title,news_p]
    
#    browser.quit()

#    return output

# def marsImage():
#     image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#     browser.visit(image_url)  
#     html = browser.html
#     soup = bs(html, 'html.parser') 
#     images = soup.find_all('a',class_= "fancybox")
#     for image in images:
#         featured_image_url = 'https://www.jpl.nasa.gov' + image['data-fancybox-href']
#     return featured_image_url 

# def marsWeather():
#     weather_url = 'https://twitter.com/marswxreport?lang=en'
#     browser.visit(weather_url)
#     html = browser.html
#     soup = bs(html, 'html.parser') 
#     mars_weather = soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
#     return mars_weather 
    
# def marsFacts():
#     facts_url = 'https://space-facts.com/mars/'
#     browser.visit(facts_url)
#     mars_facts = pd.read_html(facts_url)
#     df = mars_facts[0]
#     html_table = df.to_html(header = False, index = False)
#     html_table.replace('\n', '')
#     df.to_html('table.html')

#     return mars_facts

# def marsHem():
#     hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(hemispheres_url)
#     html = browser.html
#     soup = bs(html, 'html.parser')
#     hemispheres_images_url = []
#     image_list = soup.find('div',class_='result-list')
#     hemispheres = image_list.find_all('div',class_='item')
#     for hemisphere in hemispheres:
#         title = hemisphere.find('h3').text
#         end_link = hemisphere.find('a')["href"]
#         image_link = "https://astrogeology.usgs.gov/" + end_link   
#         browser.visit(image_link)
#         html = browser.html
#         soup=bs(html, "html.parser")
#         downloads = soup.find("div", class_="downloads")
#         image_url = downloads.find("a")["href"]
#         hemispheres_images_url.append({"title": title, "img_url": image_url})

#     return hemispheres_images_url

