import streamlit as st
import pandas as pd
import plotly.express as px
st.markdown('<div style="text-align: center;"><h1>Comparing Hotel Ratings</H1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Data Table with line_polar / Web Graph</p>', unsafe_allow_html=True)

df = pd.read_csv("hotels_review.csv")
st.write(df)

df = df[df['Hotelid'].isin(['hotel_101','hotel_102','hotel_103'])]
#st.write(df.iloc[:20, :8])

df = df.groupby('Hotelid')[['Cleanliness_rating', 'Service_rating', 'Value_rating',
                            'Rooms_rating','Checkin_rating',
                            'Businessservice_rating']].mean().reset_index()
#st.write(df)

# Convert from wide data to long data to plot radar chart
df = pd.melt(df, id_vars=['Hotelid'], var_name='category', value_name='rating',
             value_vars=['Cleanliness_rating', 'Service_rating', 'Value_rating',
                         'Rooms_rating','Checkin_rating','Businessservice_rating'],
)
#st.write(df)

fig1 = px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
                            line_shape='linear',  # or spline
                    hover_name='Hotelid',
                    hover_data={'Hotelid':False},
                    markers=True,
                    # labels={'rating':'stars'},
                    # text='Hotelid',
                    # range_r=[0,10],
                    direction='clockwise',  # or counterclockwise
                    start_angle=45
                    )



st.plotly_chart(fig1)
