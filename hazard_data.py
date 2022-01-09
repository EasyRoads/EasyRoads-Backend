import pandas as pd
import numpy as np

df = pd.read_csv('HazardousDrivingAreas.csv')

def get_area(lat, lng, distance_threshold = 0.05):
    nearby_df = df.loc[(df.Latitude-lat)**2 + (df.Longitude-lng)**2 <= distance_threshold**2]

    #print(nearby_df)

    return nearby_df


def areas_to_avoid():
    # todo figure out a good threshold value for places to avoid
    severity_threshold = 0.02
    incidents_threshold = 10
    reduced_df = df.loc[df['SeverityScore'] >= severity_threshold]
    reduced_df = reduced_df.loc[reduced_df['IncidentsTotal'] >= incidents_threshold]
    reduced_df.to_csv("hazards_above_threshold.csv")
    print(reduced_df)
    return reduced_df

    pass

# misc testing
#print(type(df))
#print(df)
#print(df.Latitude)

#get_area(43.7,-79.5)
areas_to_avoid()