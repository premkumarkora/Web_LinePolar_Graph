# Web_LinePolar_Graph

Data file is also included with this


line_polar Visual displaying the rating of Three Hotel out of 18 Hotel in that area

A Line Polar graph from plotly express is below.

px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
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
                   
It compares the rating of three hotel. This is version 1, My next version will be to give user option to select three hotels and display the graph.
