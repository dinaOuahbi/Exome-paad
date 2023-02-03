#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
import missingno as msno


# In[2]:


os.listdir('../data')


# In[3]:


df = pd.read_csv('HRDscore_cellReport.csv', sep=';')
print(df.shape)

### Supprimer (par caro) 'genome_doublings' et 'eCARD':
to_drop = df.columns[df.columns.tolist().index('eCARD'):].tolist()
to_drop.append('genome_doublings')
len(to_drop)
df.drop(to_drop, axis=1, inplace=True)
df = df.rename(columns={'patient_barcode':'patient'})


# In[14]:


# filtrer sur PAAD
df = df[df['disease']=='PAAD']
df.shape


# In[15]:


# merge with patient of interest
groups = pd.read_csv('groups.csv')
print(groups.shape)
groups.rename(columns={'condition':'pred_dicho'}, inplace=True)
groups.head(2)


# In[16]:


df_columns = df['patient'].tolist()
groups_columns = groups['patient'].tolist()


# In[17]:


len(df_columns) #9125
len(groups_columns) #162


# In[18]:


# ya 25 patient sans données HDR
len([i for i in groups_columns if i not in df_columns])


# In[19]:


# get data in common 
int_df = pd.merge(groups, df, how ='inner', on ='patient')
int_df.head()


# In[20]:


int_df.set_index('patient', inplace=True)


# In[21]:


int_df.drop('TCGA sample barcode', axis=1, inplace=True)


# In[22]:


int_df.head(2)


# In[23]:


#OBJECT with on level
to_drop = []
for col in int_df.select_dtypes('object'):
    if int(int_df[col].value_counts().count()) == 1:
        to_drop.append(col)
int_df.drop(to_drop, axis=1, inplace=True)


# In[24]:


to_drop


# In[25]:


# NAN
#sns.heatmap(int_df.isnull(), cbar=False)
int_df.replace('', np.NaN, inplace=True)
msno.matrix(int_df)


# In[156]:


int_df.dtypes.value_counts().plot.pie()
plt.axis('off')


# In[26]:


# create 3 data according to NAN
# mut_cna dataframe
mut_cna = int_df[['pred_dicho','mutLoad_silent','mutLoad_nonsilent','CNA_n_segs','CNA_frac_altered ','CNA_n_focal_amp_del']]

# mutsig dataframe
temp = [i for i in int_df.columns if i.startswith('mutSig')]
temp.append('pred_dicho')
mutSig = int_df[temp]

# ch_data dataframe
temp = int_df.columns.tolist()[int_df.columns.tolist().index('aneuploidy_score'):]
temp.append('pred_dicho')
ch_data = int_df[temp]


# In[27]:


print(
    mut_cna.shape,
    mutSig.shape,
    ch_data.shape
)


# In[28]:


mutSig.dropna(inplace=True) #loose 8 patients
ch_data.dropna(inplace=True) # loose 11 patients


# In[29]:


# convert to float
for col in mut_cna.select_dtypes('object'):
    if col != 'pred_dicho':
        mut_cna[col]=[float(i.replace(',','.')) for i in mut_cna[col]]


# In[30]:


# convert to float
for col in mutSig.select_dtypes('object'):
    if col != 'pred_dicho':
        mutSig[col]=[float(i.replace(',','.')) for i in mutSig[col]]


# In[31]:


# convert to float
for col in ch_data.select_dtypes('object'):
    if col != 'pred_dicho':
        ch_data[col]=[float(i.replace(',','.')) for i in ch_data[col]]


# In[32]:


os.getcwd()


# In[33]:


mut_cna.to_csv('processed_data/model10/mut_cna.csv')
mutSig.to_csv('processed_data/model10/mutSig.csv')
ch_data.to_csv('processed_data/model10/ch_data.csv')


# In[58]:


df = pd.read_csv('../data/processed_data/model10/mutSig.csv')
df.head()


# In[59]:


from scipy.stats import wilcoxon


# In[60]:


# compute quartile1 and quartile 75 and median 
def desc(col, group):
    Q1 = df[col][df['pred_dicho']==group].describe()[4]
    Q3 = df[col][df['pred_dicho']==group].describe()[6]
    med = np.median(df[col][df['pred_dicho']==group])
    f_res = f'{med}({Q1},{Q3})'
    return f_res


# In[62]:


for col in df:
    if col.startswith('mut'):
        print(f'--------------> {col}')
        print(desc(col, 'low'))


# In[ ]:




