from dash import Dash, html, doc
import plotly.express as px
import pandas as pd

#function that gets all unique products from a csv file in the provided format
def get_products(file_name):
    products = []
    with open(file_name, "r") as f:
        for line in f: 
            line = line.split(",")
            if line[0] not in products:
                products.append(line[0])
    return products[1:]

#products from the three files are the same 
all_products = get_products("data/daily_sales_data_0.csv")



