import reflex as rx


@rx.page(route='programas')
def programas() -> rx.Component:
    return rx.text('Algo')
