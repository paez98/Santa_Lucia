import reflex as rx

from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def body() -> rx.Component:
    return rx.vstack(
        # region PROGRAMAS
        rx.flex(

            rx.heading(
                'Programas',
                size='9',
                weight='bold',
                margin_bottom='1.5em',
                color='#ffff',
            ),
            rx.hstack(
                rx.flex(
                    rx.box(
                        rx.icon(
                            tag='puzzle',
                            size=100,
                            padding='1em',
                            color='#ffff'
                        ),
                        # border='1px solid #ffff',
                        border_radius='50em',
                        width='auto',
                        height='100%',
                        bg='#5FB4EE',

                    ),
                    rx.heading('PREESCOLAR', color='#ffff'),

                    direction='column',
                ),

                # align='center',
                # spacing='5'

                rx.flex(
                    rx.box(
                        rx.icon(tag='rocket', size=100,
                                padding='1em', color='#ffff'),
                        border_radius='50em',
                        width='auto',
                        bg='#5FB4EE',
                        height='100%'

                    ),
                    rx.heading('PRIMARIA', color='#ffff'),
                    direction='column',
                    align='center',
                    spacing='5'
                ),
                rx.flex(
                    rx.box(
                        rx.icon(tag='graduation-cap', size=100,
                                padding='1em', color='#ffff'),
                        bg='#5FB4EE',
                        border_radius='50em',
                        width='auto',
                        height='100%'

                    ),
                    rx.heading('MEDIA-GENERAL', color='#ffff', align='center'),
                    direction='column',
                    align='center',
                    spacing='5'
                ),
                rx.flex(
                    rx.box(
                        rx.icon(tag='chevrons-up', size=100,
                                padding='1em', color='#ffff'),
                        bg='#5FB4EE',
                        border_radius='50em',
                        width='auto',
                        height='100%'

                    ),
                    rx.heading('ACTIVIDADES EXTRAS',
                               color='#ffff', align='center'),
                    direction='column',
                    align='center',
                    spacing='5'
                ),
                spacing='9',

                widht='auto'
            ),
            direction='column',
            align='center',
            width='100%',
            bg='#0088E5',
            padding_y='4em'
        ),

        # region EVENTOS
        rx.flex(


            rx.heading('Eventos', size='9', weight='bold'),
            rx.hstack(
                rx.box(
                    '1',
                    rx.image(src='img.jpg'),
                    width='35em'
                ),
                rx.box(
                    '2',
                    rx.image(src='img.jpg'),
                    width='35em',
                    # height='40em'
                ),
                spacing='9',
                id='evento1'
            ),
            rx.hstack(
                rx.box(
                    '1',
                    rx.image(src='img.jpg'),
                    width='35em',
                    # height='40em'
                ),
                rx.box(
                    '1',
                    rx.image(src='img.jpg'),
                    width='35em',
                    # height='40em'
                ),
                rx.box(
                    rx.avatar(
                        rx.icon(tag="arrow_up"),
                        on_click=rx.scroll_to(elem_id='evento1'),
                    ),
                    position="fixed",
                    bottom="20px",
                    right="20px",
                    z_index="999",
                ),
                spacing='9'
            ),
            direction='column',
            align='center',

        ),
        rx.box(
            rx.heading('Experiencia', size='9'),
            bg='rgba(0,151,255, 0.5)',
            width='100%'
        ),
        align='center',
        margin_top='5em',
        border_radius='3em 3em 0em 0em',
        # bg='#0088E5',
        width='100%'

    )
