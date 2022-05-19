import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"),


streamlit.title('My Mom s healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#create multivalue picklist
streamlit.multiselect("Pick Some Fruits:" , list(my_fruit_list.index))
# display Dataframe
streamlit.dataframe(my_fruit_list)

