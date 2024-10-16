import reflex as rx
from Santa_lucia.styles.style import Size


def text_footer(icon, text, color) -> rx.Component:
    return rx.box(
        rx.text(
            rx.icon(icon, color=color, margin_right=Size.SMALL.value),
            text,
            color=color,
            display='flex',
            white_space='pre-line',
            justify_items='center',
            align='left',
            spacing='9',
            line_height='1',

        )
    )


def text_link_footer(icon, text, color, url) -> rx.Component:
    return rx.box(
        rx.link(
            rx.text(
                rx.icon(icon, color=color, margin_right=Size.SMALL.value),
                text,
                color=color,
                display='flex',
                white_space='pre-line',
                justify_items='center',
                align='left',
                spacing='9',
                line_height='1',

            ),
            href=url
        )
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.avatar(src='favicon.ico'),
            rx.heading(
                '''Colegio \nSanta Lucia''',
                white_space='pre-wrap',
                align='center',
                weight='bold',
                size='6'
            ),
            rx.hstack(
                # U E  SANTA LUCIA
                rx.flex(
                    rx.heading('U.E. Santa Lucia', color='hsl(0, 100%, 100%)'),
                    text_footer(
                        'map-pinned',
                        'Urb. Parque Valencia \nValencia, Carabobo',
                        'hsl(0, 100%, 100%)'
                    ),
                    text_footer(
                        'phone',
                        '(123) 456-7890',
                        'hsl(0, 100%, 100%)'
                    ),
                    text_footer(
                        'mail',
                        'info@schoolname.edu',
                        'hsl(0, 100%, 100%)'
                    ),
                    spacing='2',
                    direction='column',
                    # width='10em'
                ),
                # ENLACES
                rx.flex(
                    rx.heading('Enlaces rapidos',
                               color='hsl(0, 100%, 100%)'),
                    text_footer(
                        'puzzle',
                        'Preescolar',
                        'hsl(0, 100%, 100%)'
                    ),
                    text_footer('rocket', 'Primaria', 'hsl(0, 100%, 100%)'),
                    text_link_footer(
                        'graduation-cap', 'Media-general', 'hsl(0, 100%, 100%)', '#'),
                    direction='column',
                    spacing='3',
                    border_left='1px solid',
                    padding_x=Size.SMALL.value,
                    # align='center'
                ),
                # CONTACTO
                spacing='4'

            ),
            align='center',
            justify='center',
            heigth='100%'
        ),
        width='100%',
        padding=Size.DEFAULT.value,
        heigth='100%',
        bg="hsla(220, 100%, 50%, 0.8)",
        box_shadow='rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset'

    )
