import tkinter as tk
from tkinter import ttk
from uuid import uuid4


class Stylist:

    @staticmethod
    def get_options(ttkstyle, theme=None):
        """Return the available style configuration options
        
        Parameters
        ----------
        ttkstyle : str
            The style to query.

        theme : str, optional.
            The name of the theme to use when querying the style 
            options. Default=None.

        Returns
        -------
        List[str]
            A list of configuration options.

        Examples
        --------
        >>> options = Stylist.get_options('TFrame', 'default')
        >>> print(options)
        ['background', 'borderwidth', 'relief']
        """
        style = ttk.Style()
        if theme is not None:
            style.theme_use(theme)
        layout = style.layout(ttkstyle)
        elements = Stylist._get_elements(layout)
        options = []
        for e in elements:
            _opts = style.element_options(e)
            if _opts:
                options.extend(list(_opts))
        return list(set(options))

    @staticmethod
    def configure(ttkstyle, theme=None, **kwargs):
        """Create a new style based on the `base_style`
        
        Parameters
        ----------
        ttkstyle : str
            The ttk style that will be subclassed to create a new ttk
            style.

        theme : str, optional
            The name of the theme used for building the ttk style.
            Default=None.
            
        **kwargs : Dict[str, Any]
            Configuration options. Call the `Stylist.get_options` 
            method to get a list of available options.

        Returns
        -------
        str
            The name of the newly created ttk style.

        Examples
        --------
        >>> ttkstyle = Stylist.configure(
                ttkstyle='TFrame', 
                relief=tk.RAISED, 
                borderwidth=1
            )
        >>> print(ttkstyle)
        '60af9edd-1dce-4b16-82e5-df5539933549.TFrame'
        """
        style = ttk.Style()
        if theme is not None:
            style.theme_use(theme)
        style_id = uuid4()
        new_style = '{}.{}'.format(style_id, ttkstyle)
        style.configure(new_style, **kwargs)
        return new_style

    @staticmethod
    def map(ttkstyle, theme, **kwargs):
        """Customize state-based settings for ttk style options. 
        State based settings include those such as 'hover', 'disabled', 
        etc... Call the `Stylist.get_options` method for a list of 
        available options to configure.
        
        Parameters
        ----------
        ttkstyle : str
            The ttk style to configure.

        theme : str
            The name of the theme to use when configuring the style.

        *kwargs : Dict[str, List[str, Any]]
            The keyword represents the configuration option, and the 
            value is a list of tuples that contain 'state' and 'value' 
            pairs.

        Examples
        --------
        >>> Stylist.map(
                ttkstyle='TFrame',
                theme='default',
                background=[('hover', '#ddd'), ('!hover', '#fff')],
                borderwidth=[('hover', 1), ('!hover', 0)]
            )
        """
        style = ttk.Style()
        if theme is not None:
            style.theme_use(theme)
        style.map(ttkstyle, **kwargs)


    @staticmethod
    def _get_elements(layout):
        """Return a list of elements contained in the style"""
        elements = []
        element = layout[0][0]
        elements.append(element)
        sublayout = layout[0][1]

        if 'children' in sublayout:
            child_elements = Stylist._get_elements(sublayout['children'])
            elements.extend(child_elements)
        return elements


if __name__ == '__main__':

    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('default')

    # find out what options are available for the theme and widget style
    options = Stylist.get_options('TFrame', 'default')
    print('The options for this style and theme are', options)
    
    # create a new frame style (default states)
    frame_style = Stylist.configure(
        ttkstyle='TFrame', 
        theme='default', 
        relief=tk.RAISED,
        borderwidth=1
    )

    # set state-based style options
    Stylist.map(
        ttkstyle=frame_style,
        theme='default',
        background=[('hover', '#888')],
        borderwidth=[('hover', 10)]
    )

    # apply the new style
    ttk.Frame(style=frame_style, width=100, height=100).pack(padx=10, pady=10)

    root.mainloop()


