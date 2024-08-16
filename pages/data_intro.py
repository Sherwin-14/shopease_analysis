from utils import *

st.title("A Brief Overview Of Data",anchor='center')

cols = st.columns(5)

with cols[0]:
     ui.metric_card(title="Main Categories", content= "13", key="card1")

with cols[1]:
     ui.metric_card(title="Event Types", content= "3" , key="card2")

with cols[2]:
     ui.metric_card(title="Brands", content= "1,741", key="card3")

with cols[3]:
     ui.metric_card(title="Items", content= "125", key="card4")

with cols[4]:
     ui.metric_card(title="Total Users", content= "14,16,617", key="card5")


st.write("### The Original Dataset after Transformations")

st.dataframe(df_data_intro.head(10),width=1400, height=400)

