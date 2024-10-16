import reflex as rx

# LINK DE NAVEGACION


def create_nav_link(text):
    """Create a navigation link with hover effects and styling."""
    return rx.el.a(
        text,
        href="#",
        transition_duration="300ms",
        font_weight="600",
        _hover={"color": "#10B981"},
        padding_left="0.5rem",
        padding_right="0.5rem",
        padding_top="1rem",
        padding_bottom="1rem",
        color="#6B7280",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )

# ITEM DEL MENU


# def create_menu_item(hover_style, text):
#     """Create a menu item with hover effects and styling."""
#     return rx.el.a(
#         text,
#         href="",
#         role="menuitem",
#         display="block",
#         _hover=hover_style,
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         color="#374151",
#         font_size="0.875rem",
#         line_height="1.25rem",
#     )

# # BOTON DE MENU


# def create_dropdown_button(text):
#     """Create a dropdown button with hover effects and a chevron icon."""
#     return rx.el.button(
#         text,
#         rx.icon(tag='chevron-down'),
#         display="flex",
#         transition_duration="300ms",
#         font_weight="600",
#         _hover={"color": "#10B981"},
#         padding_left="0.5rem",
#         padding_right="0.5rem",
#         padding_top="1rem",
#         padding_bottom="1rem",
#         color="#6B7280",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )

# # MENU DESPLEGABLE


# def create_dropdown_menu(
#     item1_text, item2_text, item3_text
# ):
#     """Create a dropdown menu with three items and styling."""
#     return rx.box(
#         create_menu_item(
#             hover_style={
#                 "background-color": "#F3F4F6",
#                 "color": "#111827",
#             },
#             text=item1_text,
#         ),
#         create_menu_item(
#             hover_style={
#                 "background-color": "#F3F4F6",
#                 "color": "#111827",
#             },
#             text=item2_text,
#         ),
#         create_menu_item(
#             hover_style={
#                 "background-color": "#F3F4F6",
#                 "color": "#111827",
#             },
#             text=item3_text,
#         ),
#         role="menu",
#         aria_orientation="vertical",
#         aria_labelledby="options-menu",
#         padding_top="0.25rem",
#         padding_bottom="0.25rem",
#     )


# def create_dropdown_container(
#     item1_text, item2_text, item3_text
# ):
#     """Create a container for the dropdown menu with transition effects."""
#     return rx.box(
#         create_dropdown_menu(
#             item1_text=item1_text,
#             item2_text=item2_text,
#             item3_text=item3_text,
#         ),
#         class_name="group-hover:opacity-100 group-hover:visible",
#         position="absolute",
#         background_color="#ffffff",
#         transition_duration="300ms",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#         visibility="hidden",
#         left="0",
#         margin_top="0.5rem",
#         opacity="0",
#         box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
#         __ring_color="#000000",
#         __ring_opacity="0.05",
#         border_radius="0.375rem",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         width="12rem",
#     )


# def create_nav_dropdown(
#     button_text, item1_text, item2_text, item3_text
# ):
#     """Create a navigation dropdown with button and menu items."""
#     return rx.box(
#         create_dropdown_button(text=button_text),
#         create_dropdown_container(
#             item1_text=item1_text,
#             item2_text=item2_text,
#             item3_text=item3_text,
#         ),
#         class_name="group",
#         position="relative",
#     )


def create_dropdown_button(text):
    """Create a dropdown button with hover effects and a chevron icon."""
    return rx.el.button(
        text,
        rx.icon(tag='chevron-down'),
        display="flex",
        transition_duration="300ms",
        font_weight="600",
        _hover={"color": "#10B981"},
        padding="1rem 0.5rem",
        color="#6B7280",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_menu_item(text, hover_style, href):
    """Create a menu item with hover effects and styling."""
    return rx.el.a(
        text,
        href=href,
        role="menuitem",
        display="block",
        _hover=hover_style,
        padding="0.5rem 1rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_dropdown_menu(items):
    """Create a dropdown menu with items and styling."""
    hover_style = {"background-color": "#F3F4F6", "color": "#111827"}
    return rx.box(
        *[create_menu_item(item['text'], hover_style, item['href'])
          for item in items],
        role="menu",
        aria_orientation="vertical",
        aria_labelledby="options-menu",
        class_name="group-hover:opacity-100 group-hover:visible",
        padding="0.25rem 0",
    )


def create_dropdown_container(items):
    """Create a container for the dropdown menu with transition effects."""
    return rx.box(
        create_dropdown_menu(items),
        class_name="group-hover:opacity-100 group-hover:visible",
        position="absolute",
        background_color="#ffffff",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        visibility="hidden",
        left="0",
        margin_top="0rem",
        opacity="0",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        __ring_color="#000000",
        __ring_opacity="0.05",
        border_radius="0.375rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        width="12rem",
    )


def create_nav_dropdown(button_text, items):
    """Create a navigation dropdown with button and menu items."""
    return rx.box(
        create_dropdown_button(text=button_text),
        create_dropdown_container(items),
        class_name="group",
        position="relative",
    )


items = [
    {'text': 'Item 1', 'href': 'https://example.com/item1'},
    {'text': 'Item 2', 'href': 'https://youtube.com'},
    {'text': 'Item 3', 'href': 'https://example.com/item3'},
]

nav_dropdown = create_nav_dropdown("Dropdown", items)
