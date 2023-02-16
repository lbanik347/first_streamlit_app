import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')
streamlit.header('🍌 🍎 Build Your Own Fruit Smoothie 🥝 🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# Pre-populate the list with Avocado and Strawberries
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# Added on 14-Feb-2023 -- New section to display fruityvice api response 
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + 'kiwi')
streamlit.header("Fruityvice Fruit Advice!")

# Normalize JSON response in table form
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Add the tabular output to dataframe to display on the app 
#streamlit.dataframe(fruityvice_normalized)

#Added on 15-Feb-2023 -- Use of variable
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalize JSON response in table form
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Add the tabular output to dataframe to display on the app 
streamlit.dataframe(fruityvice_normalized)
