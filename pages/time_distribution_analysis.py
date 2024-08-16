from utils import *

st.title("Time Distribution Analysis")

@st.cache_resource
def plot_events_by_weekday(_df_transformed):
    event_types = ['view', 'cart', 'purchase']
    event_by_weekday = {}
    for event_type in event_types:
        event_count = df_transformed[df_transformed.Event_type == event_type].groupby("weekday")["Event_type"].count().compute()
        event_by_weekday[event_type] = event_count
    event_by_weekday = pd.DataFrame(event_by_weekday)
    weekday_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    event_by_weekday.reset_index(inplace=True)
    event_by_weekday['weekday'] = event_by_weekday.index.map(weekday_mapping)
    fig = px.bar(event_by_weekday.sort_values(by='weekday', ascending=True), x=["view","cart","purchase"], y="weekday", barmode="stack",orientation = 'h')
    st.plotly_chart(fig)

@st.cache_resource
def plot_event_distribution_by_hour(_data_transformed):
    event_types = ['view', 'cart', 'purchase']

    event_by_hour = {}
    for event_type in event_types:
        event_count = df_transformed[df_transformed.Event_type == event_type].groupby("time_dt")["Event_type"].count().compute()
        event_by_hour[event_type] = event_count

    event_by_hour = pd.DataFrame(event_by_hour)

    event_by_hour = event_by_hour.reset_index()
    event_by_hour_melted = pd.melt(event_by_hour, id_vars=['time_dt'], value_vars=['view', 'cart', 'purchase'])

    fig = px.bar(event_by_hour_melted, x="time_dt", y="value", color="variable", barmode="stack")

    fig.update_layout(width=1000, height=400)

    st.plotly_chart(fig, use_container_width=True) 

@st.cache_resource
def plot_event_distribution_by_hour_percent(_df_transformed):
    event_types = ['view', 'cart', 'purchase']

    event_by_hour = {}
    for event_type in event_types:
        event_count = df_transformed[df_transformed.Event_type == event_type].groupby("time_dt")["Event_type"].count().compute()
        event_by_hour[event_type] = event_count

    event_by_hour = pd.DataFrame(event_by_hour)

    event_by_hour = event_by_hour.reset_index()
    event_by_hour_melted = pd.melt(event_by_hour, id_vars=['time_dt'], value_vars=['view', 'cart', 'purchase'])
    
    for event_type in ['view', 'cart', 'purchase']:
        event_by_hour[f'{event_type}_percent'] = event_by_hour[event_type] / event_by_hour.sum(axis=1) * 100

    # Plot stacked line chart
    fig = px.line(event_by_hour, x=event_by_hour.index, y=[f'{event_type}_percent' for event_type in ['view', 'cart', 'purchase']],
                 labels={"x": "Hour", "y": "Percentage"},
                 template="plotly_white")

    fig.update_layout(yaxis=dict(tickformat=".0f"), width=1100, height=400)

    st.plotly_chart(fig, use_container_width=True)


@st.cache_resource
def plot_original_values_by_hour(_df_transformed):
    # Remove duplicates
    _df_transformed = _df_transformed.drop_duplicates()

    event_types = ['view', 'cart', 'purchase']
    event_by_hour = {}

    # Group by hour and count events
    for event_type in event_types:
        event_count = _df_transformed[_df_transformed.Event_type == event_type].groupby("time_dt")["Event_type"].count().compute()
        event_by_hour[event_type] = event_count

    # Convert to DataFrame
    event_by_hour = pd.DataFrame(event_by_hour).reset_index()

    # Melt the DataFrame for plotting
    event_by_hour_melted = pd.melt(event_by_hour, id_vars=['time_dt'], value_vars=event_types, var_name='Event', value_name='Count')

    # Calculate rates
    add_to_cart_rate = (event_by_hour['cart'] / event_by_hour['view']) * 100
    cart_to_checkout_rate = (event_by_hour['purchase'] / event_by_hour['cart']) * 100
    cart_abandonment_rate = 100 - cart_to_checkout_rate

    # Ensure rates are within valid range
    cart_to_checkout_rate = cart_to_checkout_rate.clip(upper=100)
    cart_abandonment_rate = cart_abandonment_rate.clip(lower=0)

    # Create a DataFrame for rates
    rates_by_hour = pd.DataFrame({
        'time_dt': event_by_hour['time_dt'],
        'Add_to_Cart_Rate': add_to_cart_rate,
        'Cart_to_Checkout_Rate': cart_to_checkout_rate,
        'Cart_Abandonment_Rate': cart_abandonment_rate
    })

    # Melt the DataFrame for plotting
    rates_by_hour_melted = pd.melt(rates_by_hour, id_vars=['time_dt'], value_vars=['Add_to_Cart_Rate', 'Cart_to_Checkout_Rate', 'Cart_Abandonment_Rate'], var_name='Rate_Type', value_name='Rate')

    # Plot the rates
    fig_rates = px.line(rates_by_hour_melted, x="time_dt", y="Rate", color='Rate_Type')

    # Update layout
    fig_rates.update_layout(xaxis_title="Hour", yaxis_title="Rate (%)", width=1100, height=400)

    # Display the plot
    st.plotly_chart(fig_rates)

@st.cache_resource
def plot_correlation(_df_transformed):

    event_types = ['view', 'cart', 'purchase']
    event_by_weekday = {}
    for event_type in event_types:
        event_count = df_transformed[df_transformed.Event_type == event_type].groupby("weekday")["Event_type"].count().compute()
        event_by_weekday[event_type] = event_count

    event_by_weekday = pd.DataFrame(event_by_weekday)

    event_by_weekday.reset_index(inplace=True)

    # Calculate Add to cart rate (ATCR)
    event_by_weekday['ATCR'] = (event_by_weekday['cart'] / event_by_weekday['view']) * 100

    # Calculate Cart-to-checkout Rate (CTCR)
    event_by_weekday['CTCR'] = (event_by_weekday['purchase'] / event_by_weekday['cart']) * 100

    # Calculate Conversion Rate (CAR)
    event_by_weekday['CAR'] = (event_by_weekday['purchase'] / event_by_weekday['view']) * 100

    # Calculate correlation matrix
    corr_matrix = event_by_weekday[["ATCR", "CAR", "CTCR"]].corr()

    fig = px.imshow(corr_matrix, color_continuous_scale="Viridis")

    fig.update_layout(width=1000, height=1000, 
                      xaxis=dict(title="Metrics"), 
                      yaxis=dict(title="Metrics"),
                      coloraxis=dict(colorbar=dict(title="Correlation Coefficient")))
    st.plotly_chart(fig)



st.write("### Distribution of Events by Weekday")
plot_events_by_weekday(df_transformed)

st.write("### Event Distribution by Hour")
plot_event_distribution_by_hour(df_transformed)


st.write("### Percentage Distribution of Events by Hour")
plot_event_distribution_by_hour_percent(df_transformed)

st.write("### Percentage Distribution of ATCR, CTCR, CAR by Hour")
plot_original_values_by_hour(df_transformed)


st.write("### Correlation Matrix for ATCR, CAR, and CTCR")
plot_correlation(df_transformed)




