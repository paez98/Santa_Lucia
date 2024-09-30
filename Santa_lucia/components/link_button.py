import reflex as rx


def link_button(text: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.text(
                text,
                weight='medium',
            ),
            variant='ghost',
            border_radius='full',
            size='4',
        ),
        href=link,

    )
