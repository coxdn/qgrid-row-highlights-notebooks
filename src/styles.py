from ipywidgets import widgets
from IPython.display import display

BACKGROUND_COLOR = {
    'type-1': '#d5e7cd',
    'type-2': '#afe569',
    'type-3': '#9fcbca',
}

highlight_row_styles = f'''
<style>
div.slick-row.highlighted-row.row-type-1 {{
    background-color: {BACKGROUND_COLOR['type-1']};
}}
div.slick-row.highlighted-row.row-type-2 {{
    background-color: {BACKGROUND_COLOR['type-2']};
}}
div.slick-row.highlighted-row.row-type-3 {{
    background-color: {BACKGROUND_COLOR['type-3']};
}}
</style>
'''

highlight_styles_widget = widgets.HTML(value=highlight_row_styles)
highlight_styles_hbox = widgets.HBox([highlight_styles_widget])


def display_styles():
    display(highlight_styles_hbox)
