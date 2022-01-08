import pandas as pd
import numpy as np

df = pd.read_csv('HazardousDrivingAreas.csv')


def get_area(lat, lng, num=50):
    # compute distance using Pythagoras
    sorted_df = ((df.Latitude-lat)**2 + (df.Longitude-lng)**2).sort_values()[:num]
    a = sorted_df.index.values.tolist()

    print(a)
    reduced_df2 = df.loc(a) # todo: make this work
    print(reduced_df2)


def areas_to_avoid():
    # todo have a threshold value for places to avoid
    severity_threshold = 0.02
    incidents_threshold = 5
    reduced_df = df.loc[df['SeverityScore'] >= severity_threshold ]
    print(reduced_df)

    # for index, row in df.iterrows():
    #     if(row.SeverityScore>0.01):
    #         print(row)
    pass

# misc testing
#print(type(df))
#print(df)
#print(df.Latitude)

#get_area(43.7,-79.5)
areas_to_avoid()