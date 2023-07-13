import dash

def set_value(id, value):
    """
    Clears the value of a Dash component.

    Args:
        id (str): The id of the Dash component.
        value (str): The value to set the component to.
    """

    ctx = dash.callback_context
    if not ctx.triggered:
        return
    else:
        input_id = ctx.triggered[0]['prop_id']
        if input_id == id:
            return value