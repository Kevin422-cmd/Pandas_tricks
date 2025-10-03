#@author : Kevin Saputra 2473011

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

#01 menyertakan plefix dan seluruh kolom data frame 
n_rows=5
n_cols=5
cols= tuple('ABCDE')
df=pd.DataFrame(np.andom.radint(1,10,size=(n_rows, n_cols)),
                colums=cols)
df
tuple('ABCDE')
df.add_preflix('kolom_')
df.add_suffix('_field')

#02 Pemilihan baris (rows selection) pada data frame
n_rows=10
n_cols=5
cols= tuple('ABCDE')
df=pd.DataFrame(np.andom.radint(1,5,size=(n_rows,n_cols)),
                colums=cols)
df
tuple('ABCDE')

df[(df['A']== 1) | (df['A'] == 3)]
df[df['A'].isin([1,3])]
df[~df['A'].sin([1,3])]



#03 konversi tipe data stirng ke numerik pada kolom data frame
data = {'col1':['1', '2', '3', 'teks'],
        'col2':['1', '2', '3', '4']}
df = pd.DataFrame(data)
df
df.dtypes

df_x=df.astype({'col2':'int'})
df_x
df_x.dtypes

df_x=df.astype({'col2':'float'})
df_x
df_x.dtypes

df.apply(pd.to_numeric, errors='coerce')


#04 Pemilihan kolom pada data frame berdasarkan tipe data
n_rows=5
n_cols=2
cols= tuple['bil_pecahan', 'bil_bulat']
df = pd.DataFrame(np.random.radint(1, 20, size=(n_rows, n_cols)),
                  columns==cols)
df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index=pd.util.testing.makeDateIndex(n_rows, freq='H')
df=df_reset_indekx()

df['teks']=list('ABCDE')
df
df.dtype

df.select_dtypes(include='number')
df.select_dtypes(include='float')
df.select_dtypes(include='int')

df.select_dtypes(include='object')
df.select_dtypes(include='datetime')
df.select_dtypes(include=['number', 'object'])



#Revisi Materi
n_rows=5
n_cols=2
cols= tuple['bil_pecahan', 'bil_bulat']
df = pd.DataFrame(np.random.radint(1, 20, size=(n_rows, n_cols)),
                  columns==cols)
df['bil_pecahan'] = df['bil_pecahan'].astype('float')
df


df.index = pd.date_range(start='2023-10-01', periods=n_rows, freq='H')
df=df.reset_index()
df['teks'] = list('ABCDE')
df 
df




   
       
         