import reflex as rx
from PIL import Image
from Santa_lucia.styles.style import Size
import requests


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
        ),

        rx.heading('Quienes Somos', size='9', margin_y='0.8em'),

        rx.hstack(
            # region NOSOTROS

            rx.card(
                rx.flex(
                    rx.icon('users', size=50),
                    rx.heading(
                        'Nosotros',
                        size='9',
                        margin='0.2em'
                    ),
                    rx.text(
                        'La Unidad Educativa "Santa Lucia" brinda servicios educativos fundamentos en los preceptivos de la constitución...',
                        size='6',
                        # margin_y='1em',
                        align='center',
                        width='100%'
                    ),
                    rx.button(
                        'Descubre mas',
                        rx.icon('arrow-right-from-line'),
                        margin_top='2em'
                        # width='50%'
                    ),
                    direction='column',
                    align='center',


                ),
                bg='center/cover url(/img.jpg)',
                padding='1.5em',
                margin='1.5em',
                width='25%',
                border_radius='20px',
                height='auto',
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
            ),

            # region MISION
            rx.card(
                rx.flex(
                    rx.icon('target', size=50),
                    rx.heading(
                        'Misión',
                        size='9',
                        margin='0.2em'
                    ),
                    rx.text(
                        'Brindar una información integral, moduladora de los Deberes y Derechos inherentes al ejercicio de la ciudadanía...',
                        align='center',
                        size='6',
                        # margin_y='1em',
                    ),
                    rx.button(
                        'Descubre mas',
                        rx.icon('arrow-right-from-line'),
                        margin_top='2em'

                        # width='50%'
                    ),
                    # border='5px dashed',
                    # width='100%',
                    # border_radius='3px',
                    # text_align='center',
                    # height="100%",
                    # justify='center',
                    align='center',
                    direction='column'
                ),
                bg='center/cover url(/img.jpg)',
                padding='1.5em',
                margin='1.5em',
                width='25%',
                border_radius='20px',
                height='auto',
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
            ),

            # region VISION
            rx.card(
                rx.flex(
                    rx.icon('book-open-text', size=50),
                    rx.heading('Visión', size='9', margin='0.2em'),
                    rx.text(
                        # integral en el Respeto a los derechos Humanos y el ejercicio activo de la Responsabilidad social individual, estará contribuyendo a la formación en las nuevas generaciones de Lideres con profunda consciencia de su misión para el logro de una sociedad mejor, libre, justa con calidad de Vida y en Paz como patrimonio moral a ser preservado y transmitido.
                        '''La Unidad Educativa Lucia I al Presentar Servicios Educativos enmarcados de manera integral...''',
                        align='center',
                        size='6',
                        # margin_y='1em'
                    ),
                    rx.button(
                        'Descubre más',
                        rx.icon('arrow-right-from-line'),
                        margin_top='2em'
                    ),
                    direction='column',
                    align='center'
                ),
                bg='center/cover url(/img.jpg)',
                padding='1.5em',
                margin='1.5em',
                width='25%',
                border_radius='20px',
                height='auto',
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
            ),
            justify='center',
            width='100%',

        ),
        align='center'
    )
