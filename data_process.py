import pandas as pd


#df = pd.DataFrame(pd.read_json('part-00000-60db49d6-8a95-4957-b5d8-129ba340723b-c000.json', lines=True), columns = ['lat', 'lon'])
#print(df.to_string()) 

json_data = 'https://azradls.blob.core.windows.net/bike-data/user/trusted-service-user/station_metrics_live/part-00000-de812749-e90b-4db8-b0e0-b6ae56e0367c-c000.json'



df = pd.DataFrame(pd.read_json(json_data, lines= True), columns = ['lat', 'lon','num_bikes_available', 'capacity', 'name', 'station_id', 'trend'])

df['a'] = df['trend'].apply(lambda x: df.trend.pop('23 ') )

#df['next_hour_trend'] = for k,v in df.trend.items()
print(df)

#print(df.trend.pop(1))
#for i in df.trend:
 #   try:
  #      print(i.pop('2 ')) #df.trend[i])
   # except KeyError:
    #    continue

#df.trend[].pop('23 ') 



#try:
#print( df.trend[1].pop('1 '))
#except:
 #   pass