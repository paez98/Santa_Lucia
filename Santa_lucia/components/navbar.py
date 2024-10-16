import reflex as rx
# from .link_button import create_navigation_menu, create_menu_item_with_submenu
from Santa_lucia.styles.style import Size
from .dropdown_menu import create_dropdown_button, create_nav_link, create_nav_dropdown, items, nav_dropdown


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium",), href=url,
        text_decoration=None,
    )


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="favicon.ico",
            width="2.25em",
            height="auto",
            border_radius="25%",
            align='start'
        ),
        # create_menu_item_with_submenu('texto1', 'item1', 'item2', 'item3'),
        rx.center(
            create_dropdown_button('Algo'),
            nav_dropdown,
            create_nav_link('aldaasdkm'),
            # create_navigation_menu(),

            width='100%'),

        rx.color_mode.button(position='absolute', right='0'),
        # justify='center',
        padding_y=Size.SMALL.value,
        padding_x=Size.DEFAULT.value,
        align='center',
        width='100%',
        spacing=Size.DEFAULT.value,
        backdrop_filter='blur(5px)',
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        backdrop_blur="blur(1.5rem)",
        position="sticky",
        top="0",
        z_index="50"
    )
