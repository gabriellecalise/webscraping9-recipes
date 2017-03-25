from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#this will open up a new file that you can write in
#csvfile = open("recipe_list.csv", 'w', newline='', encoding='utf-8')
#c = csv.writer(csvfile)

#these will be the labels for the header row of the csv
#c.writerow(['name', 'description', 'ingredients', 'instructions'])

#this is the page that I am trying to scrape:
html = urlopen("https://whatscooking.fns.usda.gov/recipes/supplemental-nutrition-assistance-program-snap/apple-slice-pancakes")

#use the html5lib -- refer to webappsplus wordpress to get there
bsObj = BeautifulSoup(html, "html.parser")

#this will open the file for writing (w = writing)
t = open ("recipetest.txt", 'w')

recipe_details = []

#use .find, not .findAll -- findAll will return an array of EVERYTHING and we just want the first one
name = bsObj.find("div", {"class":"titleWrapper"})
description = bsObj.find("div", {"class":"field-items"})
ingredients = bsObj.find("div", {"class":"recipe-ingredients"})
instructions = bsObj.find("div", {"class":"recipe-instructions"})

recipe_details = [name, description, ingredients, instructions]

for text in recipe_details:
    t.write(text.get_text() + "\n")


t.close()

#csvfile.close()
