import reflex as rx
# from .link_button import create_navigation_menu, create_menu_item_with_submenu
from Santa_lucia.styles.style import Size
from .dropdown_menu import nav_dropdown, nav_dropdown_2, create_nav_link


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
        rx.center(
            create_nav_link("Inicio", '#'),
            nav_dropdown,
            nav_dropdown_2,
            create_nav_link('Admisión', '#'),
            create_nav_link('Contacto', '#'),
            width='100%'),

        rx.color_mode.button(position='absolute', right='0'),
        padding_y=Size.SMALL.value,
        padding_x=Size.DEFAULT.value,
        align='center',
        width='100%',
        spacing=Size.DEFAULT.value,
        bg='rgba(0,136,229, 0.7)',
        backdrop_filter='blur(5px)',
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        backdrop_blur="blur(1.5rem)",
        position="sticky",
        top="0",
        z_index="50",
        margin=Size.ZERO.value
    )
