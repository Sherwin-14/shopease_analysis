from utils import *
@profile
def get_cluster(user_id):
     cluster  = df_rfm['cluster'][df_rfm['User_id'] == user_id].compute()
     return cluster

"""

@profile
def representing_categories():
    mainCat_values = df_data_intro.group_by('Main_Category').agg(pl.count('Product_id')).sort('Main_Category')
    mainCat_names = mainCat_values['Main_Category']
    mainCat_counts = mainCat_values['Product_id']
    fig = px.pie(names=mainCat_names, values=mainCat_counts, hole=0.8)
    fig.update_layout({"title":{"text":"Main category distribution", "x":0.50}})                       

"""

@profile
def main():
    print('start calculating')
    primes = get_cluster(253299396)
    #x = representing_categories()
    print(f'done')
     

if __name__ == '__main__':
    main()
