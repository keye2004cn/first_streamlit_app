import streamlit;
streamlit.title('my parents healthy dinner')
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text('Omega 3 & blueburry oatmeals')
streamlit.text('Kale,spinach & Rocket Smoothies')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberry'])
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests




