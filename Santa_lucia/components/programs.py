import reflex as rx


from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def programs() -> rx.Component:
    return rx.vstack(
        # region MAS
        rx.flex(

            rx.heading(
                'Programas',
                size='9',
                weight='bold',
                margin_bottom='1.5em',
                # margin_top='1em',
                # box_shadow="20px 20px 50px 15px rgba(0, 0, 0,0.1) inset",
                # box_shadow= 'rgba(0, 0, 0, 0.17) 0px -23px 25px 0px inset, rgba(0, 0, 0, 0.15) 0px -36px 30px 0px inset, rgba(0, 0, 0, 0.1) 0px -79px 40px 0px inset, rgba(0, 0, 0, 0.06) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;',
                # box-shadow:
                color='#ffff',
                # border_radius = '1em'
            ),
            rx.hstack(
                rx.link(


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
                        align='center',
                        spacing='5'
                    ),
                    href='#'
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
                spacing='9'
            ),
            direction='column',
            align='center',

        ),

        align='center',
        margin_top='5em',
        border_radius='3em 3em 0em 0em',
        # bg='#0088E5',
        width='100%'

    )
