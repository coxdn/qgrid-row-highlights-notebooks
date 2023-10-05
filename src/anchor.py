from ipywidgets import widgets


def create_anchor(name):
    return widgets.HTML(value=f'<div id="{name}" style="display:none;"></div>')
