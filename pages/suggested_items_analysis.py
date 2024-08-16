from utils import *


data_product = df_transformed

st.title("Requested Items Analysis")


@st.cache_resource
def plot_smartphone_word_cloud(_data_product):
    smartphones = data_product[data_product['Items'] == 'smartphone']
    brand_counts = smartphones['Brand'].value_counts().compute().to_dict()
    if brand_counts:
        brand_string = ' '.join([brand + ' ' * count for brand, count in brand_counts.items()])
        if brand_string.strip():  # Check if brand_string is not empty
            wordcloud = WordCloud(width=1000, height=400, random_state=21, max_font_size=110).generate(brand_string)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.write("No brands found in the smartphone data.")
    else:
        st.write("No brands found in the smartphone data.")

@st.cache_resource
def plot_clocks_word_cloud(_data_product):
    clocks = data_product[data_product['Items'] == 'clocks']
    brand_counts = clocks['Brand'].value_counts().compute().to_dict()
    if brand_counts:
        brand_string = ' '.join([brand + ' ' * count for brand, count in brand_counts.items()])
        if brand_string.strip():  # Check if brand_string is not empty
            wordcloud = WordCloud(width=1000, height=400, random_state=21, max_font_size=110).generate(brand_string)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.write("No brands found in the clocks data.")
    else:
        st.write("No brands found in the clocks data.")


@st.cache_resource
def plot_washers_word_cloud(_data_product):
    washers = data_product[data_product['Items'] == 'kitchen.washer']
    brand_counts = washers['Brand'].value_counts().compute().to_dict()
    if brand_counts:
        brand_string = ' '.join([brand + ' ' * count for brand, count in brand_counts.items()])
        if brand_string.strip():  # Check if brand_string is not empty
            wordcloud = WordCloud(width=1000, height=400, random_state=21, max_font_size=110).generate(brand_string)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.write("No brands found in the washers data.")
    else:
        st.write("No brands found in the washers data.")


@st.cache_resource
def plot_clock_sales_by_weekday(_data_product):
    # Convert the 'date' column to datetime type
    data_product['date'] = data_product['date'].map_partitions(pd.to_datetime)

    # Filter data to only include clock sales for October and November
    clocks = data_product[(data_product['Items'] == 'clocks') & (data_product['date'].dt.month.isin([10, 11]))].compute()

    # Group by weekday and count sales
    clock_sales_by_weekday = clocks.groupby('weekday')['Brand'].count().reset_index()

    # Map weekday numbers to names
    weekday_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    clock_sales_by_weekday['weekday'] = clock_sales_by_weekday['weekday'].map(weekday_names)

    # Rename the columns
    clock_sales_by_weekday.columns = ['weekday', 'sales']

    colors = ['#66D9EF', '#FFC107', '#66D9EF', '#FFC107', '#66D9EF', '#66D9EF', '#66D9EF']
    fig, ax = plt.subplots(figsize=(15,6))
    ax.barh(clock_sales_by_weekday['weekday'], clock_sales_by_weekday['sales'], color=colors)
    ax.set_xlabel('Sales')
    ax.set_ylabel('Weekday')
    ax.set_yticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    st.pyplot(fig)        

@st.cache_resource
def plot_smartphone_sales_by_weekday(_data_product):

    weekday_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    # Filter data to only include smartphone sales for October and November
    smartphones = data_product[(data_product['Items'] == 'smartphone') & (data_product['date'].dt.month.isin([10, 11]))].compute()

    # Group by weekday and count sales
    smartphone_sales_by_weekday = smartphones.groupby('weekday')['Items'].count().reset_index()

    # Map weekday numbers to names
    smartphone_sales_by_weekday['weekday'] = smartphone_sales_by_weekday['weekday'].map(weekday_names)

    # Rename the columns
    smartphone_sales_by_weekday.columns = ['weekday', 'sales']

    # Plotting
    plt.figure(figsize=(15, 6))
    colors = ['#34A85A', '#FF99FF', '#34A85A', '#FF99FF', '#34A85A', '#34A85A', '#34A85A']
    plt.barh(smartphone_sales_by_weekday['weekday'], smartphone_sales_by_weekday['sales'], color=colors)
    plt.xlabel('Sales')
    plt.ylabel('Weekday')
    plt.yticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    st.pyplot(plt)

@st.cache_resource
def plot_washer_sales_by_weekday(_data_product):

    weekday_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    # Filter data to only include washer sales for October and November
    washers = data_product[(data_product['Items'] == 'kitchen.washer') & (data_product['date'].dt.month.isin([10, 11]))].compute()

    # Group by weekday and count sales
    washer_sales_by_weekday = washers.groupby('weekday')['Brand'].count().reset_index()

    # Map weekday numbers to names
    washer_sales_by_weekday['weekday'] = washer_sales_by_weekday['weekday'].map(weekday_names)

    # Rename the columns
    washer_sales_by_weekday.columns = ['weekday', 'sales']

    # Plotting
    plt.figure(figsize=(15, 6))
    colors = ['#03A9F4', '#FF9800', '#03A9F4', '#FF9800', '#03A9F4', '#03A9F4', '#03A9F4']
    plt.barh(washer_sales_by_weekday['weekday'], washer_sales_by_weekday['sales'], color=colors)
    plt.xlabel('Sales')
    plt.ylabel('Weekday')
    plt.yticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    st.pyplot(plt)



st.write("### Popular Brands in Smartphones ")
plot_smartphone_word_cloud(data_product)

st.write("### Popular Brands in Clocks ")
plot_clocks_word_cloud(data_product)

st.write("### Popular Brands in Washers ")
plot_washers_word_cloud(data_product)


st.write("### Clock Sales by Weekday for October and November ")
plot_clock_sales_by_weekday(data_product)

st.write("### Smartphone Sales by Weekday for October and November")
plot_smartphone_sales_by_weekday(data_product)

st.write("### Washer Sales by Weekday for October and November")                                
plot_washer_sales_by_weekday(data_product)