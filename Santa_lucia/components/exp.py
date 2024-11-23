import reflex as rx
from Santa_lucia.styles.style import Size


def experience() -> rx.Component:
    return rx.flex(
        rx.heading('Experiencia', size='9'),
        rx.hstack(
            rx.box(
                rx.heading('+240000', size='8'),
                rx.text('Estudiantes graduados', size='5')
            ),
            rx.box(
                rx.heading('+240000', size='8'),
                rx.text('Estudiantes actiovs', size='5')
            ),
            rx.box(
                rx.heading('48', size='8', align='center'),
                rx.text('Años de experiencia', size='5')
            ),
            spacing='7'
        ),
        bg='rgba(0,151,255, 0.5)',
        width='100%',
        align='center',
        justify='center',
        padding_y=Size.MEDIUM.value,
        direction='column',
        spacing='7'
    ),
