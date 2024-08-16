from utils import *


user_list = df_rfm['User_id'].unique().compute()

st.title("Customer Segmentation Model")

option = st.selectbox(
    "Choose a user id to get the cluster he/she falls in",
    user_list,
)

st.write("You selected :", option)

col1, col2, col3 = st.columns(3)

@profile
def get_cluster(user_id):
     cluster = df_rfm.loc[df_rfm['User_id'] == user_id, 'cluster'].compute().iloc[0]
     return cluster


cluster = get_cluster(option)

cols = st.columns(4)

with cols[1]:
    ui.metric_card(title="Cluster", content= cluster.item(), key="card1")

cluster_counts = df_rfm.groupby('cluster')['User_id'].nunique().compute()

st.write("### Customer Segmentation Breakdown")

cluster_df = pd.DataFrame({'Cluster': cluster_counts.index, 'Customer Count': cluster_counts.values})

st.dataframe(cluster_df[['Cluster','Customer Count']], width=1100, height=210)


