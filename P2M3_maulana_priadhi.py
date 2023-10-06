'''
=================================================
Milestone 3

Nama  : Maulana Muhamad Priadhi
Batch : FTDS-007-HCK

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Dataset yang digunakan adalah dataset mengenai pembelian produk deposito oleh nasabah bank.
=================================================
'''

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

# kode untuk menghubungkan PostgreSQL ke python
conn_string="dbname='db_phase2' host='localhost' user='postgres' password='123456'"
conn=db.connect(conn_string)
df=pd.read_sql("select * from table_M3", conn)

# function untuk cleaning data
def data_cleaning(df):

    '''
    Fungsi ini ditujukan untuk melakukan Data Cleaning pada dataframe.

    Parameters:
    df: dataframe yang telah didefinisikan

    Return
    data: hasil dataframe yang telah dilakukan cleaning
        
    Contoh penggunaan:
    df = data_cleaning(df)
    '''

    # menghapus missing value
    df = df.dropna()

    # rename kolom menjadi lowercase
    df = df.rename(columns={'Id': 'id'})

    # menghapus nilai 'age' yang tidak masuk akal
    umur_aneh = df[(df['age'] == 999) | (df['age'] == -1)].index
    df.drop(umur_aneh, inplace=True)

    return df  # Mengembalikan variabel dataframe yang telah dilakukan Data Cleaning

# run function
df = data_cleaning(df)

# menyimpan csv yang sudah dilakukan Data Cleaning
df.to_csv('P2M3_maulana_priadhi_data_clean.csv')
print("-------Data Saved------")


# kode untuk mengupload dataframe yang sudah diolah ke dalam elastic search
es = Elasticsearch("http://localhost:9200")
df_cleaned=pd.read_csv('P2M3_maulana_priadhi_data_clean.csv')
for i,r in df.iterrows():
    doc=r.to_json()
    res=es.index(index="table_m3", body=doc)
    print(res)