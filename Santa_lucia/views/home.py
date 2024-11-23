import reflex as rx
import requests
from Santa_lucia.styles.style import Size
from Santa_lucia.components.expandible_card import render_card_component

# region HEADER


def home() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.flex(
                rx.heading('Unidad Educativa \nColegio \nSanta Lucia',
                           white_space='pre-line', align='center', size='7'),
                border='1px solid',
                height='30em',
                width='100%',
                justify='center',
                align='center',
                margin_x=Size.VERY_BIG.value,

            ),
            rx.image(src='img1.png'),
            width='100%',
            justify='center',
            align='center',
            margin=Size.ZERO.value,
            padding=Size.ZERO.value

        ),
        rx.divider(size='4',),
        rx.heading('Quienes Somos', size='9', margin_y='0.8em'),

        rx.hstack(
            # region NOSOTROS
            render_card_component(),
            justify='center',
            width='100%',
            height='400px'

        ),
        align='center',
        width='100%',
    )
