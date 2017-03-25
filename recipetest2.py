from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv

#this will open up a new file that you can write in
csvfile = open("recipe_list.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)

#these will be the labels for the header row of the csv
c.writerow(['name', 'description', 'ingredients', 'instructions'])

#this is the page that I am trying to scrape:
html = urlopen("https://whatscooking.fns.usda.gov/search/solr-results/im_field_term_menu_items/main-dishes-152")
#use the html5lib -- refer to webappsplus wordpress to get there
bsObj = BeautifulSoup(html, "html.parser")
recipe_list = []

#this will open the file for writing (w = writing) t = open ("recipetest.txt", 'w')

def get_next_page(html, bsObj):
    next_page = bsObj.find("a",{"title":"Go to next page"})
    if next_page and ('href' in next_page.attrs):
        partial = str(next_page.attrs['href'])
        new_url = "https://whatscooking.fns.usda.gov/search/solr-results/im_field_term_menu_items/main-dishes-152" + partial
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        get_player_pages(html,bsObj)
    else:
        print("Done collecting URLs")

def get_recipe_pages(html, bsObj):
    global recipe_list
    tag_list = bsObj.findAll("a", {"class":"views-field-label"})
    for tag in tag_list:
        if 'href' in tag.attrs:
            recipe_list.append(str(tag.attrs['href']))
    time.sleep(1)

def get_recipe_details(recipe_list):
    for recipe in recipe_list:
        new_url = "https://whatscooking.fns.usda.gov/search/solr-results/im_field_term_menu_items/main-dishes-152" + recipe
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        bsObj.span.decompose()
        recipe_details = []
        #use .find, not .findAll -- findAll will return an array of EVERYTHING and we just want the first one
        name = bsObj.find("div", {"class":"titleWrapper"} )
        description = bsObj.find("div", {"class":"field-items"} )
        ingredients = bsObj.find("div", {"class":"recipe-ingredients"} )
        instructions = bsObj.find("div", {"class":"recipe-instructions"} )

        recipe_details = [name, description, ingredients, instructions]

        #this is an empty list for the CSV rows
        row = []
        for detail in recipe_details:
            try:
                #write a new item into the list, row
                row.append( detail.get_test() )
            except AttributeError:
                # write a new item into the list, row
                row.append( "None" )

                # write a new row in the CSV, by writing the list
        c.writerow( row )

        # delay program for 1 second
        time.sleep(1)



get_recipe_pages(html, bsObj)
get_recipe_details(recipe_list)
#don't forget to close the CSV!!!!!!!!
csvfile.close()
