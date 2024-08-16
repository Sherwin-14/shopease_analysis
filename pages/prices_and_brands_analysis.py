from utils import *


st.title("Analysis On Prices And Brands")


data_product = df_data_intro.drop_duplicates(subset='Product_id')


@st.cache_resource
def show_avg_price_by_brand(_data_product):
    avg_price = data_product.groupby('Brand')['Price'].mean().compute().reset_index()
    avg_price_top_10 = avg_price.sort_values(by='Price', ascending=False)[:10]

    fig = px.bar(avg_price_top_10, x='Brand', y='Price', color='Price', color_continuous_scale='RdBu')
    fig.update_layout(
        xaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)'),
        yaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)')
    )
    st.plotly_chart(fig,use_container_width=True)

@st.cache_resource
def filter_and_analyze_data(_data_product):
    # Filter rows where 'Main_Category' is 'electronics' and 'Items' is 'clock'
    clocks_df = data_product[(data_product['Main_Category'] == 'electronics') & (data_product['Items'] == 'clocks')].reset_index()

    # Calculate the average price for each brand
    top_10_brands = clocks_df.groupby('Brand')['Price'].mean().nlargest(10)

    top_10_brands_costliest = top_10_brands.compute()

    colors = ['above_avg' if price > top_10_brands_costliest.mean() else 'medium_avg' if price > top_10_brands_costliest.median() else 'below_avg' for price in top_10_brands_costliest.values]    # Create a horizontal bar chart with conditional formatting
    fig = px.bar(top_10_brands_costliest, y=top_10_brands_costliest.index, x=top_10_brands_costliest.values, 
                 orientation='h', color=colors, color_discrete_map={'above_avg': '#3498db', 'medium_avg': '#f1c40f', 'below_avg': '#e74c3c'})

    fig.update_layout(width=800, height=600, xaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)'),
                      yaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)'))  # Set the width and height of the figure
    st.plotly_chart(fig, use_container_width=True)

@st.cache_resource
def display_top_brands(_data_product):
    refrigerators_df = _data_product[(_data_product['Main_Category'] == 'appliances') & (_data_product['Items'] == 'kitchen.refrigerators')].reset_index().compute()
    top_10_brands = refrigerators_df.groupby('Brand')['Price'].mean().nlargest(10)
    
    fig = px.bar(top_10_brands, x=top_10_brands.values, y=top_10_brands.index, orientation='h',
                 color=top_10_brands.values, color_continuous_scale='RdBu')
    fig.update_layout(width=800, height=600, xaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)'),
                      yaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)')) 
    
    st.plotly_chart(fig, use_container_width=True)


@st.cache_resource
def display_top_washer_brands(_data_product):
    washers_df = data_product[(data_product['Main_Category'] == 'appliances') & (data_product['Items'] == 'kitchen.washer')].reset_index()
    
    washers_df = washers_df.compute()
    # Calculate the average price for each brand
    top_10_brands = washers_df.groupby('Brand')['Price'].mean().nlargest(10)
    
    
    fig = px.bar(top_10_brands, x=top_10_brands.values, y=top_10_brands.index, orientation='h',color=top_10_brands.values, color_continuous_scale='RdBu')
    fig.update_layout(width=800, height=600, xaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)'),
                      yaxis=dict(showgrid=False, gridcolor='rgba(0,0,0,0)')) 
    
    st.plotly_chart(fig, use_container_width=True)

@st.cache_resource
def generate_wordcloud(_data_product):
    # Compute brand counts
    brand_counts = data_product['Brand'].value_counts().compute().to_dict()

    if brand_counts:
        # Create a string with each brand repeated according to its count
        brand_string = ' '.join([brand + ' ' * count for brand, count in brand_counts.items()])

        if brand_string.strip():  # Check if brand_string is not empty
            # Create a word cloud object
            wordcloud = WordCloud(width=1000, height=400, random_state=21, max_font_size=110).generate(brand_string)

            # Display the word cloud using Streamlit
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
        else:
            st.write("No brands found in the data.")
    else:
        st.write("No brands found in the data.")    

st.write("### Top 10 Brands with Highest Average Product Prices: Insights into Premium Offerings and Customer Willingness to Pay ")
show_avg_price_by_brand(data_product)


st.write("### Top 10 Brands with Highest Average Product Prices: Insights into Premium Offerings and Customer Willingness to Pay ")
filter_and_analyze_data(data_product)

st.write("### Top 10 Most Expensive Refrigerator Brands: Leading Luxury Brands Known for High Prices and Exceptional Craftsmanship ")
display_top_brands(data_product)


st.write("### Top 10 Most Expensive Washing Machine Brands: Leading Luxury Brands Known for High Prices and Exceptional Craftsmanship")
display_top_washer_brands(data_product)


st.write("### Top 10 Most Popular Brands by Revenue: Leading Companies Generating the Highest Total Revenue ")
generate_wordcloud(data_product)