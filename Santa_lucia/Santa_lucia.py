"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.navbar import navbar
from .views.home import home
from .components.programs import programs
from .components.exp import experience
from .components.footer import footer


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        home(),
        programs(),
        experience(),
        footer(),
        widht='100%'
    )


app = rx.App()
app.add_page(index)
