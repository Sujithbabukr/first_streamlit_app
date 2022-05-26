import streamlit
import pandas
import requests
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
                                        
  
streamlit.title('My Mom \'s healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#create multivalue picklist
fruits_to_selected =streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Apple','Orange'])
fruits_to_show = my_fruit_list.loc[fruits_to_selected]
# display Dataframe
streamlit.dataframe(fruits_to_show)
streamlit.text(fruityvice_response)
