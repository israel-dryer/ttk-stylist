import tkinter as tk
from tkinter import ttk
from uuid import uuid4

class Stylist:

    @staticmethod
    def get_elements(layout):
        """Return a list of elements contained in the style"""
        elements = []
        element = layout[0][0]
        elements.append(element)
        sublayout = layout[0][1]

        if 'children' in sublayout:
            child_elements = Stylist.get_elements(sublayout['children'])
            elements.extend(child_elements)
        return elements

    @staticmethod
    def get_options(ttkstyle, theme=None):
        style = ttk.Style()
        if theme is not None:
            style.theme_use(theme)
        layout = style.layout(ttkstyle)
        elements = Stylist.get_elements(layout)
        options = []
        for e in elements:
            _opts = style.element_options(e)
            if _opts:
                options.extend(list(_opts))
        return list(set(options))

    @staticmethod
    def create_style(base_style: str, theme=None, **kwargs):
        style = ttk.Style()
        if theme is not None:
            style.theme_use(theme)
        style_id = uuid4()
        ttkstyle = '{}.{}'.format(style_id, base_style)
        style.configure(ttkstyle, **kwargs)
        return ttkstyle


if __name__ == '__main__':

    root = tk.Tk()

    # find out what options are available for the theme and widget style
    options = Stylist.get_options('TFrame', 'default')
    print('The options for this style and theme are', options)

    # create a new style
    frame_style = Stylist.create_style('TFrame', 'alt', relief=tk.RAISED, borderwidth=1)

    # apply the new style
    ttk.Frame(style=frame_style, width=100, height=100).pack(padx=10, pady=10)
    
    root.mainloop()


