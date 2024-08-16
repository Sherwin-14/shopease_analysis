from utils import *


ddf = df_transformed


st.title("Brand Analysis Extended With Time Series Factors")

@st.cache_resource
def plot_daily_revenue_by_brand(_ddf):

    ddf['date'] = ddf['date'].astype('datetime64[ns]')
    # Calculate daily revenue by brand
    revenue_by_day_nov = ddf.groupby(['date', 'Brand'])['Price'].sum().compute().reset_index(name='daily_revenue')

    # Get the top 5 brands by revenue for November and October
    top5_revenue_brands_nov = revenue_by_day_nov.groupby('Brand')['daily_revenue'].sum().nlargest(5).index
    revenue_by_day_nov['brand_grouped'] = revenue_by_day_nov['Brand'].apply(lambda x: x if x in top5_revenue_brands_nov else 'Other')

    # Take top 5
    revenue_day_top5_nov = revenue_by_day_nov[revenue_by_day_nov['brand_grouped']!='Other']

    # Stacked bar chart
    fig = px.bar(revenue_day_top5_nov, x='date', y='daily_revenue', color='Brand', 
                 labels={'date': 'Date', 'daily_revenue': 'Daily Revenue'},
                 title='Daily Revenue by Brand (Top 5 Brands) - November and October',
                 barmode='stack')

    fig.update_layout(legend_title_text='Brand',
                      legend=dict(orientation='h', x=0, y=1.02, xanchor='left', yanchor='bottom'),
                      width=1000, height=400)

    st.plotly_chart(fig)

@st.cache_resource
def plot_retention_rate(_ddf):
    # Step 1: Identify unique users who made a purchase from each brand
    brand_users = ddf.groupby('Brand')['User_id'].nunique().compute()

    # Step 2: Identify users who made repeat purchases from each brand
    repeat_users = ddf[ddf['Event_type'] == 'purchase'].groupby(['Brand', 'User_id']).size()
    repeat_users = repeat_users.groupby('Brand').count().compute()

    # Calculate retention rate for each brand
    retention_rate = repeat_users / brand_users

    # Get the top 10 brands with the highest retention rate
    top_10_brands = retention_rate.nlargest(10)

    # Create a 3D scatter plot
    fig = px.scatter(x=top_10_brands.index, y=top_10_brands.values,
                        title='Top 10 Brands with Highest Retention Rate', 
                        labels={'x': 'Brand', 'y': 'Retention Rate'})

    st.plotly_chart(fig)

@st.cache_resource
def plot_total_orders_per_brand(_ddf):
    # Calculate total orders per brand
    brand_total_orders = ddf.groupby("Brand")["Event_type"].count().compute().reset_index()
    brand_total_orders = brand_total_orders.rename(columns={'Event_type': 'total_orders'})

    # Get top 5 brands
    top_brands = brand_total_orders.nlargest(5, "total_orders")

    # Create a scatter plot
    fig = px.scatter(top_brands, x="Brand", y="total_orders", 
                     title="Total Orders for Top 5 Brands",
                     labels={"Brand": "Brand", "total_orders": "Total Orders"},
                     template="plotly_white")

    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))

    # Show the plot
    st.plotly_chart(fig)



plot_daily_revenue_by_brand(ddf)    
plot_retention_rate(ddf)
plot_total_orders_per_brand(ddf)