from utils import *

st.title("Analysis On Major Categories and Items")

@st.cache_resource
def representing_categories():
    mainCat_values = df_data_intro.groupby('Main_Category')['Product_id'].nunique().compute()
    mainCat_names = mainCat_values.index
    fig = px.pie(names=mainCat_names, values=mainCat_values, hole=0.8)
    fig.update_layout({"width": 1100,  # Set the width to 400 pixels
    "height": 400})
    st.plotly_chart(fig,use_container_width=True)

@st.cache_resource
def top_categories_chart():
    top_5_cat = df_data_intro.groupby('Main_Category')['Price'].sum().compute()
    top_5_cat = top_5_cat / 1000000
    top_5_cat = top_5_cat.round(2)
    top_5_cat_sorted = pd.Series(top_5_cat).sort_values(ascending=False)[:5]
    top_5_cat_names = top_5_cat_sorted.index

    fig = px.pie(values=top_5_cat_sorted, names=top_5_cat_names, hole=0.8)
    fig.update_layout(
    margin=dict(l=50, r=50, b=50, t=50, pad=4),
    width=1100,  # Set the width to 800 pixels
    height=350,  # Set the height to 600 pixels
    )   
    st.plotly_chart(fig,use_container_width=True)   

@st.cache_resource
def show_avg_price_by_category(_df_data_intro):
    avg_price = df_data_intro.groupby('Main_Category')['Price'].mean().compute()
    avg_price = avg_price.sort_values(ascending=False)
    avg_price_df = avg_price.to_frame('Average Price').reset_index()
    avg_price_df.columns = ['Main Category', 'Average Price']

    fig = px.bar(avg_price_df, x='Main Category', y='Average Price', 
             color='Average Price', color_continuous_scale='RdBu')
    fig.update_layout({
        "xaxis" : dict(showgrid=False, gridcolor='rgba(0,0,0,0)'),
        "yaxis" : dict(showgrid=False, gridcolor='rgba(0,0,0,0)')
    })

    st.plotly_chart(fig,use_container_width=True)

@st.cache_resource
def show_top_10_items(_df_data_intro):
    top_10_items = df_data_intro.groupby('Items')['Price'].sum().compute()
    top_10_items = top_10_items / 1000000
    top_10_items = top_10_items.round(2)
    top_10_items_sorted = top_10_items.sort_values(ascending=False)[:10]
    top_10_items_names = top_10_items_sorted.index

    fig = px.pie(names=top_10_items_names, values=top_10_items_sorted, hole=0.8, color=top_10_items_sorted)
    fig.update_layout({
        "showlegend":True,
        "legend":{"orientation":"v", "yanchor":"bottom", "y":0.2, "x":1.5, "xanchor":"right"},
        "margin":{"l":50, "r":50, "b":50, "t":50, "pad":4},
        "width" :1100,  # Set the width to 800 pixels
        "height" : 350
    })

    st.plotly_chart(fig,use_container_width=True)   


@st.cache_resource
def show_electronics_subcategories(_df_data_intro):
    electronicsCat_names = _df_data_intro[_df_data_intro['Main_Category']=='electronics']['Items'].unique()
    electronicsCat_values = _df_data_intro[_df_data_intro['Main_Category']=='electronics'].groupby('Items')['Product_id'].nunique()
    print('Number of sub-categories in electronics products: ', len(electronicsCat_names))
    electronicsCat_df = pd.DataFrame(electronicsCat_values.reset_index())
    electronicsCat_df.columns = ['Items', 'Value']

    fig = px.pie(electronicsCat_df, values='Value', names='Items', hole=0.8, color='Value')
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="bottom",
            y=0.1,
            xanchor="right",
            x=1.5
        ),
        width = 1100,  # Set the width to 800 pixels
        height = 380
    )

    st.plotly_chart(fig,use_container_width=True) 

@st.cache_resource
def show_category_treemap(_df_data_intro):
    category_counts = df_data_intro.drop_duplicates(subset='Product_id').groupby(['Main_Category', 'Items']).size().reset_index()
    category_counts.columns = ['Main_Category', 'Items', 'Count']

    fig = px.treemap(category_counts, path=[0, 1], 
                      color_continuous_scale='YlGnBu')
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),
                     font=dict(size=14),
                     width=1100, height=700)

    st.plotly_chart(fig, use_container_width=True)


# Function Calls

st.write("### The store's product offerings are composed of a diverse range of categories, with the top 5 being ")
representing_categories()


st.write("### Top 5 Revenue-Generating Categories and Their Contribution to Total Revenue")
top_categories_chart()    


st.write("### Average Prices and Pricing Insights Across Main Categories")
show_avg_price_by_category(df_data_intro)   

st.write("### Top 10 Revenue-Generating Items and Their Contribution to Total Revenue")
show_top_10_items(df_data_intro)


st.write("### Top Revenue-Generating Products in Electronics and Their Contribution to Category Revenue")
show_electronics_subcategories(df_data_intro)

st.write("### Breakdown of Products by Main and Sub Categories: Insights into Distribution and Growth Opportunities")
show_category_treemap(df_data_intro)


