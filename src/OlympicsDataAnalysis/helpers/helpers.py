import pandas as pd
import numpy as np



def get_country_wise_medal_tally(df:pd.DataFrame):
    medal_tally = df.drop_duplicates(subset =['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold','Silver', 'Bronze']].sort_values('Gold', ascending= False).reindex()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] +medal_tally['Bronze']
    return medal_tally

def country_year_list(df:pd.DataFrame):
    unique_year = df['Year'].unique().tolist()
    unique_year.sort()
    unique_year.insert(0,"Overall")
    
    unique_country = np.unique(df['region'].dropna().values).tolist()
    unique_country.sort()
    unique_country.insert(0,"Overall")
    
    return unique_year, unique_country

def filter_medal_tally(df,years, unique_countries):
    flag = 0
    medal_df = df.drop_duplicates(subset =['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    if years == "Overall" and unique_countries == "Overall":
        temp_df = medal_df
    if years == "Overall" and unique_countries != "Overall":
        flag = 1
        temp_df = medal_df.query("region == @unique_countries")

    if years != "Overall" and unique_countries == "Overall":
        temp_df = medal_df.query("Year == @years")
    if years!= "Overall" and unique_countries != "Overall":
        temp_df = medal_df.query('Year == @years and region == @unique_countries')
        
    if flag == 1:   
        filtered_df =temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year', ascending=True).reset_index()
    else:
        filtered_df =temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold', ascending=False).reset_index()
        
    filtered_df['total'] = filtered_df['Gold'] + filtered_df['Silver'] + filtered_df['Bronze']
    return filtered_df

def participating_nations_over_time(df:pd.DataFrame):
    
    years_vs_no_of_nation = df.drop_duplicates(['Year','region'])['Year'].value_counts().reset_index().sort_values('Year')
    years_vs_no_of_nation.rename(columns = {'Year':'Edition','count':'No of nation'}, inplace=True)
    return years_vs_no_of_nation
    
def no_of_events_over_the_year(df: pd.DataFrame):
    events_over_the_year = df.drop_duplicates(['Year','Event'])['Year'].value_counts().reset_index().sort_values('Year')
    events_over_the_year.rename(columns ={'Year': 'Edition', 'count': 'No of Events' }, inplace =True)
    return events_over_the_year

def no_of_athletes_over_the_year(df: pd.DataFrame):
    events_over_the_year = df.drop_duplicates(['Year','Name'])['Year'].value_counts().reset_index().sort_values('Year')
    events_over_the_year.rename(columns ={'Year': 'Edition', 'count': 'No of Athletes' }, inplace =True)
    return events_over_the_year

def sports_over_the_year(df:pd.DataFrame):
    x = df.drop_duplicates(['Year','Sport','Event'])
    pivot_table = x.pivot_table(index = 'Sport', columns='Year', values = 'Event', aggfunc= 'count').fillna(0).astype(int)
    return pivot_table

def most_sucessful_athletes(df, sport):
    temp_df = df.dropna(subset =['Medal'])
    
    if sport != "Overall":
        temp_df = temp_df.query("Sport == @sport")
    temp_df = (
        temp_df['Name'].value_counts()
                .reset_index()
                .head(15)
                .merge(df, left_on = 'Name', right_on = 'Name', how ='left')[['Name','count','Sport','region']]
                .drop_duplicates('Name')
            )
    temp_df.rename(columns= {'count': 'Medals'})
    
         
    return temp_df

def countrywise_medal_tally(df:pd.DataFrame, country:str):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset = ['Team','NOC', 'Games','Year','City','Sport','Event','Medal'], inplace= True)
    
    if country != "Overall":
        temp_df = temp_df.query("region == @country")
    countrywise_medal_tally = temp_df.groupby('Year').count()['Medal'].reset_index()
    
    return countrywise_medal_tally

def sport_wise_medal_tally(df:pd.DataFrame, country:str):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset = ['Team','NOC', 'Games','Year','City','Sport','Event','Medal'], inplace= True)
    if country != "Overall":
        temp_df = temp_df.query('region == @country')
    sports_wise_count = temp_df.pivot_table(index ='Sport', columns ='Year', values ='Medal', aggfunc ='count').fillna(0)
    return sports_wise_count

def most_sucessful_athletes_country_wise(df:pd.DataFrame, region:str):
    temp_df = df.dropna(subset =['Medal'])
    if region != 'Overall':
        temp_df = temp_df.query("region == @region")
    top_10_althlete_based_on_region = (
        temp_df['Name'].value_counts()
                .reset_index()
                .head(10)
                .merge(df, left_on = 'Name', right_on = 'Name', how ='left')[['Name','count','Sport']]
                .drop_duplicates('Name')
            )
    
    top_10_althlete_based_on_region.rename(columns= {'count': 'Medals'}, inplace =True)         
    return top_10_althlete_based_on_region
    
def athletes_age_analysis(df: pd.DataFrame):
    age_vs_medal = {}
    medal_list = ['Gold', 'Silver','Bronze','Overall']
    for medal in medal_list:
        if medal != 'Overall':
            x = df.query('Medal == @medal')['Age'].dropna()
            age_vs_medal[medal +' medalist'] = x
        else:
            x =df['Age'].dropna()
            age_vs_medal['Overall Age'] = df['Age'].dropna()
    return age_vs_medal

def athletes_age_vs_gold_medal_analysis(df: pd.DataFrame):
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    age_vs_sport_gold_medal = {}
    for sport in famous_sports:
        temp_df = df.query("Sport == @sport")
        age_df = temp_df.query('Medal == "Gold"')['Age'].dropna()
        age_vs_sport_gold_medal[sport] = age_df
    return age_vs_sport_gold_medal
    
def male_vs_female(df:pd.DataFrame):
    athlete_df = df.drop_duplicates(subset = ['Name','region'])
    
    male = athlete_df.query('Sex == "M"').groupby('Year').count()['Name'].reset_index()
    female = athlete_df.query('Sex == "F"').groupby('Year').count()['Name'].reset_index()
    final = male.merge(female,on ='Year')
    final.rename(columns ={'Name_x':'Male', 'Name_y':'Female'}, inplace = True)
    return final

    
    
    