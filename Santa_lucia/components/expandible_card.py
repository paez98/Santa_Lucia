import reflex as rx

# Constantes para colores y estilos
COLOR_PRINCIPAL = "#374151"
TRANSICION_RAPIDA = {
    "duration": "300ms",
    "timing_function": "cubic-bezier(0.4, 0, 0.2, 1)",
    "property": "all"
}


def aplicar_transicion(estilos):
    """Aplica configuraciones de transición comunes a los estilos dados."""
    estilos.update({
        "transition_duration": TRANSICION_RAPIDA["duration"],
        "transition_timing_function": TRANSICION_RAPIDA["timing_function"],
        "transition_property": TRANSICION_RAPIDA["property"]
    })
    return estilos


def create_body_text(content):
    """Crea un elemento de texto estilizado para el contenido del cuerpo de la tarjeta."""
    return rx.text(
        content,
        margin_top="1rem",
        color=COLOR_PRINCIPAL
    )


def create_card_content(tittle, text_body):
    """Crea el contenido principal de la tarjeta, incluyendo título y texto del cuerpo."""
    return rx.box(
        # rx.image(srg),
        rx.heading(tittle, font_weight="700", margin_bottom="1rem",
                   font_size="1.5rem", line_height="2rem", as_="h2"),
        rx.text(text_body,
                margin_bottom="1.5rem", color=COLOR_PRINCIPAL),
        text_align="center",
    )


def create_learn_more_button():
    """Crea un botón 'Aprende Más' estilizado con efectos de hover."""
    return rx.el.a(
        "Aprende Más",
        href="#",
        background_color="#3B82F6",
        font_weight="700",
        _hover={"background-color": "#2563EB"},
        display="inline-block",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
        **aplicar_transicion({"transition_property": "background-color, border-color, color, fill, stroke, opacity, box-shadow, transform"})
    )


def create_expandable_card_content(tittle, text_body, content):
    """Create the expandable content of the card, including main content, additional information, and a button."""
    return rx.box(
        create_card_content(tittle=tittle, text_body=text_body),
        rx.box(
            create_body_text(
                content=content
            ),
            class_name="group-hover:max-h-96",
            transition_duration="300ms",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
            max_height="0",
            overflow="hidden",
            transition_property="all",
        ),
        rx.box(
            create_learn_more_button(),
            class_name="group-hover:opacity-100 group-hover:translate-y-0 transform",
            transition_duration="300ms",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
            margin_top="1.5rem",
            opacity="0",
            text_align="center",
            transition_property="all",
            transform="translateY(1rem)",
        ),
        padding="2rem",
    )


def create_interactive_card(tittle, text_body, content):
    """Create an interactive card with hover effects and expandable content."""
    return rx.box(
        create_expandable_card_content(
            tittle=tittle, text_body=text_body, content=content, ),
        class_name="group",
        background_color="#ffffff",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={
            "box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
        },
        max_width="24rem",
        margin_left="auto",
        margin_right="auto",
        overflow="hidden",
        border_radius="0.75rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        transition_property="all",
    )


def render_card_component():
    """Render the complete card component within a fragment and box container."""
    return rx.flex(
        rx.box(
            create_interactive_card(
                'Sobre nosotros',
                'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s',
                'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industryLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500ss standard dummy text ever since the 1500s',
                'img1.png'),
        ),
        rx.box(
            create_interactive_card('Misión', 'ALgo', 'algo2', 'img.jpg'),
        ),
        rx.box(
            create_interactive_card('Visión', 'ALgo', 'algo2', 'img1.png'),
        ),
        direction='row',
        spacing='4',
    )
