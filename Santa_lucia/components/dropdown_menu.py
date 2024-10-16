import reflex as rx


def create_dropdown_button(text):
    """Create a dropdown button with hover effects and a chevron icon."""
    return rx.el.button(
        text,
        rx.icon(tag='chevron-down'),
        # create_chevron_icon(),
        transition_duration="300ms",
        font_weight="600",
        _hover={"color": "#10B981"},
        padding_left="0.5rem",
        padding_right="0.5rem",
        padding_top="1rem",
        padding_bottom="1rem",
        color="#6B7280",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_nav_link(text):
    """Create a navigation link with hover effects and styling."""
    return rx.el.a(
        text,
        href="#",
        transition_duration="300ms",
        font_weight="600",
        _hover={"color": "#10B981"},
        padding_left="0.5rem",
        padding_right="0.5rem",
        padding_top="1rem",
        padding_bottom="1rem",
        color="#6B7280",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )
