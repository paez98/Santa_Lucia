import reflex as rx


@rx.page(route='/colegio', title='Sobre nosotros')
def colegio():
    return rx.text('hola')
