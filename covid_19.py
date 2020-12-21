import requests
import pandas as pd
import numpy as np
import seaborn as sns
from  datetime import date, timedelta

pd.set_option('display.max_columns', None)

url="https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"

myfile = requests.get(url, allow_redirects=True)
open('D:/My documents/!GoogleDrive/Public/covid-19/covid_19.xlsx', 'wb').write(myfile.content)



df = pd.read_excel('D:/My documents/!GoogleDrive/Public/covid-19/covid_19.xlsx')
df=df.rename(columns = {"countriesAndTerritories":"Country",
  df.columns[0]:"date",
  "cases":"Infected_new",
  "deaths":"Deaths_new",
  "continentExp":"region",
  }).sort_values(by=['Country','date'])

df.drop(['month','year','day'],1,inplace = True)

df.loc[df.date.isin(["2020-04-03","2020-04-04","2020-05-18","2020-05-20"]) & (df.Country=="France"),
  "Deaths_new"]=[1355,1120,300,183]
df.loc[df.date.isin(["2020-04-27","2020-04-28","2020-04-29"]) & (df.Country=="Spain"),
  "Deaths_new"]=[331,301,325]  
df.loc[df.date.isin(["2020-04-27","2020-05-01","2020-05-01"]) & (df.Country=="Germany"),
  "Deaths_new"]=[193,94] 
  
df["date"]=df['date'] - pd.to_timedelta(1,unit='d')
df["Country"]=df["Country"].replace("United States of America|United_States_of_America","USA", regex=True )
df["Country"]=df["Country"].replace("United Kingdom|United kingdom|United_Kingdom","UK", regex=True )
df["Country"]=df["Country"].replace("United_Arab_Emirates","UAE", regex=True )
df["Country"]=df["Country"].replace("_"," ", regex=True )


seq_df = pd.concat(
  [pd.DataFrame(
    {'Country': i, 
    'date': pd.date_range("2019-12-30",date.today()- timedelta(days = 1))}
    )for i,g in df.groupby(['Country'])]
                     )
df = pd.merge(seq_df, df, how='left', on=['Country', 'date'])

# df['geoId']=df.groupby('Country')['geoId'].transform('first')
# df['popData2018']=df.groupby('Country')['popData2018'].transform('first')
# df['region']=df.groupby('Country')['region'].transform('first')
# df['Deaths']=df.groupby('Country')['Deaths_new'].transform(lambda x: x.fillna(0).cumsum())
# df['Infected']=df.groupby('Country')['Infected_new'].transform(lambda x: x.fillna(0).cumsum())

df = df.assign( 
  geoId = df.groupby('Country')['geoId'].transform('first'),
  popData2019 = df.groupby('Country')['popData2019'].transform('first'),
  region = df.groupby('Country')['region'].transform('first'),
  Deaths = df.groupby('Country')['Deaths_new'].transform(lambda x: x.fillna(0).cumsum()),
  Infected = df.groupby('Country')['Infected_new'].transform(lambda x: x.fillna(0).cumsum()),
  letal= round(df['Deaths']/df['Infected'],2),
  Deaths_pc= round(df['Deaths']*1000000/df['popData2019'],2),
  Deaths_new_pc= round(df['Deaths_new']*1000000/df['popData2019'],2)
)

df=df.query('Deaths>0')

df.dtypes

start_i=100
start_d=5

df = df.assign(
  n = df.groupby('Country')['Country'].transform('count'),
  ord =  df.groupby('Country').cumcount()+1,
  totalD30=df.groupby('Country')['Deaths'].transform(lambda x: x.rolling(30, min_periods=1).sum())#,
  )

df['totalD30']=df.groupby('Country')['totalD30'].transform('last')


del df['FirstOrder']


df.head(5)

  #totalD30 = 

#-----------------


sample_data = {'user': ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'],\
                'clicks': [0,1,2,3,4,5,6,7,8,9]}
x = pd.DataFrame(sample_data)

x.groupby('user')['clicks'].rolling(3, min_periods=1).sum().groupby(level=0).shift()

x
x.groupby('user')['clicks'].rolling(3, min_periods=1).sum().groupby(level=0).shift()
x.groupby('user')['clicks'].rolling(3, min_periods=1).sum().shift()
x.groupby('user')['clicks'].rolling(3, min_periods=1).sum()



df['date']=pd.to_datetime(df['date'])

,format="%d/%m/%y"

df %>% filter(Country=="Ukraine" & Deaths<5)

df.loc[(df['Country']=="Ukraine") & (df['Deaths']<5)]
df.loc[np.logical_and(df['Country']=="Ukraine",df['Deaths']<5)]

pd.to_datetime(df['date'],format="%y-%m-%d").head()

x=df.groupby('Country')['Deaths'].mean().reset_index()

tbl = df.groupby('Country').agg(
  Deaths_max=('Deaths',max),
  Deaths_min=('Deaths',min),
  Infected_mean=('Infected','mean'),
  Infected_min=('Infected',min),
  N=
  ).reset_index()


df['new'] = df.groupby('Country', group_keys=False).apply(lambda x: x.Deaths.max())

df= df.assign( new= lambda x: x.groupby('Country').transform('max')['Deaths'] )
df = df.assign( max_deaths = lambda x: x.groupby('Country')['Deaths'] .transform('max'),
)

df['sum_deaths'] = df.groupby('Country').apply(lambda x: x['Deaths'].sum())

df= df.assign(new = df.Deaths*2)

df=df.drop('new',1)


ir = sns.load_dataset('iris')
ir = ir.assign( max_petal_len_species = lambda x: x.groupby('species').transform('max')['petal_length'] )
ir = ir.assign( max_petal_len_species4 = ir.groupby('species')['petal_length'].transform('first') )


with open('D:/My documents/!GoogleDrive/Public/ЗНО/OpenData2018.csv') as f:
    print(f)

