I wanted to scrape the "What's Cooking? USDA Mixing Bowl" website for recipes:  https://whatscooking.fns.usda.gov/search/solr-results  

I was able to successfully scrape the names of recipes, recipe descriptions, ingredients and directions for all of the main course recipes into a txt file. Then I tried to do it and put it in a CSV file, but it is not working for me.

I broke this project into three parts:
1. Get the individual items from each page
2. Get the links from the list of recipes
3. Get all the links from each page of links

The first one was successful. In recipetest.py, I was able to take the info from a recipe page and scrape it and put it into a .txt file. Then when I tried to write it to a CSV in recipetest2.py, I was unable to get values put into my CSV.

I do not receive errors when I run this code, but nothing writes to the CSV except for the headings.
