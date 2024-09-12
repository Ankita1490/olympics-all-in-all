from operator import ge
from statistics import median_low
import streamlit as st 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff
from OlympicsDataAnalysis.config.configuration import ConfigurationManager
from OlympicsDataAnalysis.helpers.helpers import (country_year_list, 
                                                filter_medal_tally,
                                                participating_nations_over_time,
                                                no_of_events_over_the_year,
                                                no_of_athletes_over_the_year,
                                                sports_over_the_year,
                                                most_sucessful_athletes,
                                                countrywise_medal_tally, 
                                                sport_wise_medal_tally,
                                                most_sucessful_athletes_country_wise, 
                                                athletes_age_analysis,
                                                athletes_age_vs_gold_medal_analysis,
                                                male_vs_female)


config = ConfigurationManager()
preprocessed_df = pd.read_csv(config.config.data_preprocesing.preprocessed_data_file_path)
st.sidebar.title("Olympics analysis")
user_menu = st.sidebar.radio(
    'Select an option',
    (
    'Medal Tally', 
    'Overall Analysis', 
    'Country-wise Analysis', 
    'Athelete wise Analysis'
    )
)
if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, regions = country_year_list(preprocessed_df)
    selected_years = st.sidebar.selectbox("Select Year", years)
    selected_region =st.sidebar.selectbox("Select Country", regions)
    medal_tally = filter_medal_tally(preprocessed_df, selected_years,selected_region)
    
    if selected_years == 'Overall' and selected_region == 'Overall':
        st.title("Overall Tally")
    if selected_years =='Overall' and selected_region !='Overall':
        medal_tally['Year'] = medal_tally['Year'].map("{:.0f}".format)
        st.title(f"Overall Medal Tally for {selected_region}")
    if selected_years !='Overall' and selected_region =='Overall':
        st.title(f"Overall Medal Tally for {selected_years}")
    if selected_years !='Overall' and selected_region !='Overall':
        st.title(f" Medal Tally for {selected_region} in {selected_years}")  
    st.table(medal_tally)
    
    
if user_menu == "Overall Analysis":
    st.title('Top Statistics')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label ='Editions', value= len(preprocessed_df['Year'].unique()))
    with col2:
        st.metric(label ='Cities', value=len(preprocessed_df['City'].unique()))
    with col3:
        st.metric(label ='Events', value=len(preprocessed_df['Event'].unique()))
    with col4:
        st.metric(label ='Althletes', value=len(preprocessed_df['Name'].unique()))
    with col5:
        st.metric(label ='Countries', value=len(preprocessed_df['region'].unique()))

    years_vs_no_of_nation = participating_nations_over_time(preprocessed_df)
    events_over_the_year = no_of_events_over_the_year(preprocessed_df)
    athletes_overtime = no_of_athletes_over_the_year(preprocessed_df)
    sports_overtime = sports_over_the_year(preprocessed_df)
   
    
    with st.container():
        tab1, tab2, tab3, tab4, tab5 = st.tabs(['No. of Nation','No. of Events', 
                                            'No. of Athletes','No. of sports','Top 15 Athletes'])
        with tab1:
            st.subheader('Nations participated over the years')
            fig =px.line(years_vs_no_of_nation, x ="Edition", y = 'No of nation')
            st.plotly_chart(fig)
        with tab2:
            st.subheader('No. of Events  over the years')
            fig =px.line(events_over_the_year, x ="Edition", y = 'No of Events')
            st.plotly_chart(fig)
        with tab3:
            st.subheader('No. of Athletes  over the years')
            fig =px.line(athletes_overtime, x ="Edition", y = 'No of Athletes')
            st.plotly_chart(fig)
        with tab4:
            st.subheader('No. of sports over the years')
            fig, ax = plt.subplots(figsize = (20,20))
            sns.heatmap(sports_overtime, annot = True)
            st.pyplot(fig)
        with tab5:
            sport_list = preprocessed_df['Sport'].unique().tolist()
            sport_list.sort()
            sport_list.insert(0,"Overall")
            sport_selected = st.selectbox('Select a Sport', sport_list)
            st.subheader("Most sucessfull Athletes")
            sucessful_athletes = most_sucessful_athletes(preprocessed_df, sport_selected)
            st.table(sucessful_athletes)
            
if user_menu == "Country-wise Analysis":
    st.sidebar.title("Country wise Analysis")
    country_list = preprocessed_df['region'].dropna().unique().tolist()
    country_list.sort()
    country_list.insert(0,"Overall")
    country_selected = st.sidebar.selectbox('Select a country', country_list, placeholder='Overall')
    
    
    tab1, tab2, tab3 = st.tabs(['No. of medals by year','No. of medals per sport', 'Top 10 athlete'])
    with tab1:
        st.subheader(country_selected + " Medal tally over the years")
        country_medal_tally = countrywise_medal_tally(preprocessed_df,country_selected)
        fig = px.line(country_medal_tally,x ='Year', y ='Medal') 
        st.plotly_chart(fig)
    with tab2:
        st.subheader(country_selected + "'s sports wise Medal Tally")
        sports_wise_medal_tally = sport_wise_medal_tally(preprocessed_df, country_selected)
        fig, ax =plt.subplots(figsize =(20,10))
        sns.heatmap(sports_wise_medal_tally, annot =True)
        st.pyplot(fig)
    with tab3:
        st.subheader(country_selected+'s top 10 athletes')
        top_athelete = most_sucessful_athletes_country_wise(preprocessed_df, country_selected)
        st.table(top_athelete)
        
if user_menu == "Athelete wise Analysis":
    st.title("Athlete wise analysis")
    tab1,tab2,tab3,tab4 = st.tabs(['Male Vs Female Participation','Age vs Medal', 
                            'Age wrt Sports(Gold Medalist)', 'Athletes stats vs sport'])
    with tab2:
        age_vs_medal = athletes_age_analysis(preprocessed_df)
        fig =ff.create_distplot(list(age_vs_medal.values()),list(age_vs_medal.keys()), show_hist = False, show_rug = False)
        st.plotly_chart(fig)
    with tab3:
        age_vs_gold_medal = athletes_age_vs_gold_medal_analysis(preprocessed_df)
        values = list(age_vs_gold_medal.values())

        keys =list(age_vs_gold_medal.keys())
        fig_ = ff.create_distplot(values,keys, show_hist = False, show_rug = False)
        st.plotly_chart(fig_)
    with tab4:   
        athlete_df = preprocessed_df.drop_duplicates(subset = ['Name','region'])
        athlete_df['Medal'].fillna('No Medal', inplace=True)
        sport_list = preprocessed_df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0,'Overall')
        sport_selected = st.selectbox('Select a Sport', sport_list, index = 6)
        if sport_selected != 'Overall':
            athlete_df = athlete_df.query('Sport == @sport_selected') 
        fig =px.scatter(athlete_df, x= 'Weight', y = 'Height', color='Medal', symbol ='Sex', size_max=60, template = "simple_white")
        st.plotly_chart(fig)
    with tab1:
        athlete_df = male_vs_female(preprocessed_df)
        fig = px.line(athlete_df, x ="Year", y=['Male','Female'])
        st.plotly_chart(fig)
        
        
            
        
        
    
        
        
        
        
    
        
        
            

            
            
        
            
            
            
            


