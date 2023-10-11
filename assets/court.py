import plotly.express as px
import plotly.graph_objects as go
from dash import html, dcc
import plotly.io as pio

def draw_plotly_court(fig, court_id, fig_width=500, margins=0):

    import numpy as np

    # From: https://community.plot.ly/t/arc-shape-with-path/7205/5
    def ellipse_arc(x_center=0.0, y_center=0.0, a=10.5, b=10.5, start_angle=0.0, end_angle=2 * np.pi, N=200, closed=False):
        t = np.linspace(start_angle, end_angle, N)
        x = x_center + a * np.cos(t)
        y = y_center + b * np.sin(t)
        path = f'M {x[0]}, {y[0]}'
        for k in range(1, len(t)):
            path += f'L{x[k]}, {y[k]}'
        if closed:
            path += ' Z'
        return path

    fig_height = fig_width * (470 + 2) / (500 + 2)
    fig.update_layout(width=fig_width, height=fig_height, showlegend=False)

    # Set axes ranges
    fig.update_xaxes(range=[-250 - margins, 250 + margins])
    fig.update_yaxes(range=[-52.5 - margins, 417.5 + margins])

    threept_break_y = 89.47765084
    three_line_col = "#2f2f2f"
    main_line_col = "#2f2f2f"
    zone_line_col = 'red'

    fig.update_layout(
        # Line Horizontal
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#f2f2f2",
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        shapes=[
            dict(
                type="rect", x0=-250, y0=-52.5, x1=250, y1=417.5,
                line=dict(color=main_line_col, width=2),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=-80, y0=-52.5, x1=80, y1=137.5,
                line=dict(color=main_line_col, width=2),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=-60, y0=-52.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=2),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="circle", x0=-60, y0=77.5, x1=60, y1=197.5, xref="x", yref="y",
                line=dict(color=main_line_col, width=2),
                #fillcolor='#dddddd',
                layer='below'
            ),
            dict(
                type="line", x0=-60, y0=137.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=2),
                layer='below'
            ),

            dict(
                type="rect", x0=-2, y0=-7.25, x1=2, y1=-12.5,
                line=dict(color="#ec7607", width=2),
                fillcolor='#ec7607',
            ),
            dict(
                type="circle", x0=-7.5, y0=-7.5, x1=7.5, y1=7.5, xref="x", yref="y",
                line=dict(color="#ec7607", width=2),
            ),
            dict(
                type="line", x0=-30, y0=-12.5, x1=30, y1=-12.5,
                line=dict(color="#ec7607", width=2),
            ),

            dict(type="path",
                 path=ellipse_arc(a=40, b=40, start_angle=0, end_angle=np.pi),
                 line=dict(color=main_line_col, width=2), layer='below'),
                 
            # THREE POINT ARC
            dict(type="path",
                 path=ellipse_arc(
                     a=237.5, b=237.5, start_angle=0.386283101, end_angle=np.pi - 0.386283101),
                 line=dict(color=main_line_col, width=2), layer='below'),

            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=220, y0=-52.5, x1=220, y1=threept_break_y,
                line=dict(color=three_line_col, width=2), layer='below'
            ),

            dict(
                type="line", x0=-250, y0=227.5, x1=-220, y1=227.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=250, y0=227.5, x1=220, y1=227.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=17.5, x1=-80, y1=17.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=27.5, x1=-80, y1=27.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=57.5, x1=-80, y1=57.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=87.5, x1=-80, y1=87.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=90, y0=17.5, x1=80, y1=17.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=90, y0=27.5, x1=80, y1=27.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=90, y0=57.5, x1=80, y1=57.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),
            dict(
                type="line", x0=90, y0=87.5, x1=80, y1=87.5,
                line=dict(color=main_line_col, width=2), layer='below'
            ),

            dict(type="path",
                 path=ellipse_arc(y_center=417.5, a=60, b=60,
                                  start_angle=-0, end_angle=-np.pi),
                 line=dict(color=main_line_col, width=2), layer='below'),
        ]
    )
    
   # EXPORT COURT AS JPG 
    '''
    court_graph =  dcc.Graph(
        figure=fig,
        config={'displayModeBar': False},
        style={'width': f'{fig_width}px',
               'height': f'{fig_height}px',
                'marginLeft': 5},
        id=f'{court_id}-court-graph',
        className='court-graph'
    ),
    
    # Export the figure as a JPG image
    image_file_path = 'court_image.jpg'  # Set the desired file path
    pio.write_image(fig, image_file_path, format='jpg')
    '''
    
    draw_scatter_trace(fig)
    
    return dcc.Graph(
        figure=fig,
        config={'displayModeBar': False},
        style={'width': f'{fig_width}px',
               'height': f'{fig_height}px',
                'marginLeft': 5},
        id=f'{court_id}-court-graph',
        className='court-graph'
    ),



def draw_scatter_trace(fig):
    
    # Create a list of all possible coordinates (x, y) for scatter points
    scatter_points = []
    for x in range(-249, 250, 6):
        for y in range(-51, 418, 6):
            scatter_points.append((x, y))

    # Add a new scatter trace for all the points
    fig.add_trace(
        go.Scatter(
            x=[point[0] for point in scatter_points],
            y=[point[1] for point in scatter_points],
            mode="markers",
            marker=dict(
                opacity=0,
                size=2,
            ),
            hoverinfo='none',
        )
    )
    
    return fig

def is_inside_three_point_line(click_data):
    if click_data is None:
        return False

    # Extract the x and y coordinates of the clicked point
    x, y = click_data['points'][0]['x'], click_data['points'][0]['y']

    # Parameters of the 3-point arc ellipse
    x_center, y_center = 0, 0
    a, b = 237.5, 237.5

    # Check if the x value is within the range [-220, 220]
    is_within_x_range = -220 <= x <= 220

    # Equation of the ellipse: ((x-x_center)/a)**2 + ((y-y_center)/b)**2 = 1
    # Check if the clicked point satisfies the ellipse equation
    is_inside_ellipse = (((x - x_center) / a) ** 2 + ((y - y_center) / b) ** 2) <= 1

    return is_within_x_range and is_inside_ellipse


'''
            ###   SHOOTING ZONES   ###
            ### RIM ###
            # ARC #
            dict(type="path",
                 path=ellipse_arc(a=80, b=80, start_angle=0, end_angle=np.pi),
                 line=dict(color=zone_line_col, width=1), layer='below'),
                 
            dict(
                type="line", x0=80, y0=-51, x1=80, y1=0,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=-80, y0=-51, x1=-80, y1=0,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            ### Short Mid-Range  ###
            # ARC #
            dict(type="path",
                 path=ellipse_arc(
                     a=160, b=160, start_angle=0.1, end_angle=np.pi - 0.1),
                 line=dict(color=zone_line_col, width=1), layer='below'),
            
            dict(
                type="line", x0=159, y0=-51, x1=159, y1=16,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=-159, y0=-51, x1=-159, y1=16,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            # LINES #
            dict(
                type="line", x0=55, y0=59, x1=101, y1=124,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=-55, y0=59, x1=-101, y1=124,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            ### Long Mid-Range ###
            # ARC#
            dict(type="path",
                 path=ellipse_arc(
                     a=237.5, b=237.5, start_angle=0.386283101, end_angle=np.pi - 0.386283101),
                 line=dict(color=zone_line_col, width=1), layer='below'),
            
            dict(
                type="line", x0=220, y0=-52.5, x1=220, y1=threept_break_y,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            # LINES #
            dict(
                type="line", x0=61, y0=149, x1=185, y1=420,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=-61, y0=149, x1=-185, y1=420,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=138, y0=79, x1=206, y1=119,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=-138, y0=79, x1=-206, y1=119,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            ### THREE POINT BREAK ###
            # LINES #
            dict(
                type="line", x0=221, y0=89, x1=250, y1=89,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            
            dict(
                type="line", x0=-221, y0=89, x1=-250, y1=89,
                line=dict(color=zone_line_col, width=1), layer='below'
            ),
            '''