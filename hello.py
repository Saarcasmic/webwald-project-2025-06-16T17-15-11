import pandas as pd
import plotly.express as px
import preswald

preswald.connect()
preswald.sidebar()

# Load the dataset
df = preswald.get_df('data/house.csv')


sql = "SELECT bedrooms, price, floors, city, country FROM data/house.csv WHERE bedrooms = 3 "
filtered_df = preswald.query(sql, "data/house.csv")
fig = px.scatter(df, x="price", y="bedrooms", color="city")



preswald.text("# My Data Analysis App")

# Show the filtered table
preswald.table(filtered_df, title="Sample Data from SQL Query")

# Show the chart
preswald.plotly(fig)


