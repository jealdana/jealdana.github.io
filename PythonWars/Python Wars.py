
# coding: utf-8

# ## Episode 1 - The Python Menace
# 
# Description:  
# In this tutorial we will crawl quotes from Star Wars The clone wars, clean the format and automate a daily random email.
# 
# Activities included in this tutorial:
# 
# - Web scraping and automated mailing
# - Python and SQL 
# 
# ### Topics:
# 
# - Data mining
# - Automation
# - Natural Language Processing (NLP)
# - SQL
# - Web scraping
# - Machine learning
# 
# ### Path of the Python Menace:
# 
# 1. Get the force in the quotes
# 1. Send the quotes through email
# 
# ## Episode 2
# 1. Classify the quotes by topics using Natural language processing + Machine Learning
# 1. Select a specific topic and receive a quote
#     1. Use jupyter buttons
#     1. Save the logs to the SQL palace
# 
# 
# Theme: Starwars, python
# 
# The website is from mytowntutors.com : [quotes link](http://mytowntutors.com/2014/04/star-wars-the-clone-wars/)

# In[ ]:

import webbrowser
import requests
import bs4

res = requests.get('http://mytowntutors.com/2014/04/star-wars-the-clone-wars/')

print(res.status_code == requests.codes.ok)
print("Number of lines in te downloaded page: %i"%len(res.text))
print("The first 20 thousand lines for a quick assesment. Hint: by using the finder it will give you an idea of the tags related to the info.")
print(res.text[:20000]) # quick assesment


# <a id="GettingQuotes"></a>
# ## Getting the quotes
# 
# ### Extracting the quotes

# In[ ]:

starwars_website = bs4.BeautifulSoup(res.text)
starwars_quotes = starwars_website.select('li')

print("Number of elements that have li tag" + str(len(starwars_quotes)));

starwars_quotes[126].getText(); # Since the quotes are together we need to find the first
                                # quote and the last. In this case were 19 and 127 respectively

starwar_quotes_selected = []
for quote in starwars_quotes[19:127]:
    starwar_quotes_selected.append(quote.getText())
starwar_quotes_selected


# ### Cleaning the quotes

# In[60]:

starwar_quotes_selected_cleaned = []
for quote_number in range(len(starwar_quotes_selected)):
    starwar_quotes_selected_cleaned.append(starwar_quotes_selected[quote_number].encode("utf-8").split(":")[1].strip("\xe2\x80\x9d").strip(" \xe2\x80\x9c").replace("\xe2\x80\x99","'").replace("\xe2\x80\x94",","))
starwar_quotes_selected_cleaned


# ### Mailing the quotes
# 
# 1. Get the record of the last 15 quotes.
# 1. We will randomize the quotes, those that are not in the last 15 sent quotes, so you don't get the same quotes in the same order over and over. # Hint: circular buffer for sent quotes.
# 1. Mail the quote
# 

# In[ ]:



