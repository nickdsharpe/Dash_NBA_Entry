from maindash import app

def is_inside_rim_shot_zone(click_data):
    if click_data is None:
        return False

    # Extract the x and y coordinates of the clicked point
    x, y = click_data['points'][0]['x'], click_data['points'][0]['y']

    # Parameters of the rim ellipse
    x_center, y_center = 0, 0
    a, b = 80, 80
    
    if y < 0:
        is_within_lower_entension = -80 <= x <= 80
    else:
        is_within_lower_entension = False
    
    # Check if the clicked point satisfies the ellipse equation and is within y-range
    is_inside_ellipse = (((x - x_center) / a) ** 2 + ((y - y_center) / b) ** 2) <= 1

    return is_inside_ellipse or is_within_lower_entension

def is_inside_short_mid_range_shot_zone_3(click_data):
    if click_data is None:
        return False
    
    # Extract the x and y coordinates of the clicked point
    x, y = click_data['points'][0]['x'], click_data['points'][0]['y']

    # Parameters of the rim ellipse
    x_center, y_center = 0, 0
    a, b = 160, 160
    
    if y < 16:
        is_within_lower_entension = -160 <= x <= 160
    else:
        is_within_lower_entension = False
        
    is_on_right_side_of_line = x > 55 and y < 59 + (65/46) * (x - 55)
    
    # Check if the clicked point satisfies the ellipse equation and is within y-range
    is_inside_ellipse = (((x - x_center) / a) ** 2 + ((y - y_center) / b) ** 2) <= 1
    
    if ((is_inside_ellipse or is_within_lower_entension) and is_on_right_side_of_line) and not is_inside_rim_shot_zone(click_data):
        return 'Mid-range Zone 3'
    else:
        return None
    
def is_inside_short_mid_range_shot_zone_1(click_data):
    if click_data is None:
        return False
    
    # Extract the x and y coordinates of the clicked point
    x, y = click_data['points'][0]['x'], click_data['points'][0]['y']

    # Parameters of the rim ellipse
    x_center, y_center = 0, 0
    a, b = 160, 160
    
    if y < 16:
        is_within_lower_entension = -160 <= x <= 160
    else:
        is_within_lower_entension = False
        
    is_on_left_side_of_line = x < -55 and y < 59 - (65/46) * (x + 55)
    
    # Check if the clicked point satisfies the ellipse equation and is within y-range
    is_inside_ellipse = (((x - x_center) / a) ** 2 + ((y - y_center) / b) ** 2) <= 1
    
    if ((is_inside_ellipse or is_within_lower_entension) and is_on_left_side_of_line) and not is_inside_rim_shot_zone(click_data):
        return 'Mid-range Zone 1'
    else:
        return None
    
    
def is_inside_short_mid_range_shot_zone_2(click_data):
    if click_data is None:
        return False
    
    # Extract the x and y coordinates of the clicked point
    x, y = click_data['points'][0]['x'], click_data['points'][0]['y']

    # Parameters of the rim ellipse
    x_center, y_center = 0, 0
    a, b = 160, 160
    
    # Check if the clicked point satisfies the ellipse equation and is within y-range
    is_inside_ellipse = (((x - x_center) / a) ** 2 + ((y - y_center) / b) ** 2) <= 1
    
    if (is_inside_ellipse and not is_inside_rim_shot_zone(click_data)) and not (is_inside_short_mid_range_shot_zone_1(click_data) or is_inside_short_mid_range_shot_zone_3(click_data)):
        return 'Mid-range Zone 2'
    else:
        return None