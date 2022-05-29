import streamlit
import pandas
import requests
import snowflake.connector
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

                                        
  
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
streamlit.header('🍌🥭 Fruityvice Fruit Advice  🥝🍇')
fruit_choice=streamlit.text_input('Choice of fruit for advice','orange')
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+ fruit_choice)
fruityvicw_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvicw_normalize)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit load List Contains :")
streamlit.dataframe(my_data_rows)
add_my_fruit =streamlit.text_input('Choice of fruit for advice','Mango')
streamlit.text('Thanks for adding : ')
streamlit.text(add_my_fruit)
