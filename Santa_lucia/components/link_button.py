import reflex as rx
from typing import Optional


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


# ICONO DE FLECHA
def create_chevron_down_icon():
    """Creates a chevron-down icon with specific styling."""
    return rx.icon(
        tag="chevron-down",
        height="1rem",
        margin_left="0.25rem",
        width="1rem",
    )


def create_dropdown_link(link_text):
    """Creates a dropdown link with hover effects and a chevron-down icon."""
    return rx.el.a(
        link_text,
        create_chevron_down_icon(),
        href="#",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        display="flex",
        _hover={"color": "#FCD34D"},
        align_items="center",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )

# region submenu item


def create_submenu_item(item_text, url: Optional[str] = None):
    """Creates a submenu item with hover effects."""
    return rx.el.a(
        item_text,
        href=url,
        display="block",
        color='#1D4ED8',
        # _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def wrap_submenu_item_in_list_item(item_text, ):
    """Wraps a submenu item in a list item element."""
    return rx.el.li(
        create_submenu_item(item_text=item_text)
    )


def create_dropdown_submenu(
    item1_text, item2_text, item3_text
):
    """Creates a dropdown submenu with three items and specific styling."""
    return rx.list(
        wrap_submenu_item_in_list_item(
            item_text=item1_text,

        ),
        wrap_submenu_item_in_list_item(
            item_text=item2_text
        ),
        wrap_submenu_item_in_list_item(
            item_text=item3_text
        ),
        class_name="group-hover:block",
        position="absolute",
        background_color="#95bef9",
        display="none",
        flex_direction="column",
        left="0",
        padding_top="0.5rem",
        border_radius="0.375rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        gap="0.5rem",
    )

# region crear menu


def create_menu_item_with_submenu(
    main_item_text,
    submenu_item1_text,
    submenu_item2_text,
    submenu_item3_text,
):
    """Creates a menu item with a submenu containing three items."""
    return rx.list(
        rx.el.li(
            create_dropdown_link(link_text=main_item_text),
            create_dropdown_submenu(
                item1_text=submenu_item1_text,
                item2_text=submenu_item2_text,
                item3_text=submenu_item3_text,
            ),
            class_name="group",
            position="relative",
        ))


def create_school_logo_and_name():
    """Creates a flex container with the school logo and name."""
    return rx.flex(
        rx.image(
            alt="School logo",
            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/ngXkpIbc6vqee097fUy2eeucXfmKfx0PKw619W3LDc7085CyJA/out-0.webp",
            height="2.5rem",
            border_radius="9999px",
            width="2.5rem",
        ),
        rx.text.span(
            "Excellence Academy",
            font_weight="700",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        display="flex",
        align_items="center",
        column_gap="0.875rem",
    )

# region navMenu


def create_navigation_menu():
    """Creates the main navigation menu with dropdown submenus."""
    """Crea el menu de navegacion con los submenus desplegables"""
    return rx.list(
        rx.el.li(
            rx.el.a(
                "Home",
                href='#',
                transition_duration="300ms",
                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                _hover={"color": "#FCD34D"},
                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
            )
        ),
        # rx.el.li(
        #     rx.el.a(
        #         "Sobre nosotros",
        #         href='#',
        #         weight='bold',
        #         transition_duration="300ms",
        #         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        #         _hover={"color": "#FCD34D"},
        #         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        #     )
        # ),
        # create_menu_item_with_submenu(
        #     main_item_text=" Sobre Nosotros ",
        #     submenu_item1_text=" Historia ",
        #     submenu_item2_text=" Misi",
        #     submenu_item3_text="Faculty & Staff",
        # ),
        create_menu_item_with_submenu(
            main_item_text=" Colegio ",
            submenu_item1_text="Quienes somos",
            submenu_item2_text="Instalaciones",
            submenu_item3_text="Instalaciones",
        ),
        create_menu_item_with_submenu(
            main_item_text=" Admissions ",
            submenu_item1_text="Application Process",
            submenu_item2_text="Tuition & Fees",
            submenu_item3_text="Financial Aid",
        ),
        create_menu_item_with_submenu(
            main_item_text=" Contact ",
            submenu_item1_text="Directory",
            submenu_item2_text="Location",
            submenu_item3_text="Support",
        ),
        display="flex",
        column_gap="1.5rem",
    )


def create_apply_now_button():
    """Creates an 'Apply Now' button with specific styling and hover effects."""
    return rx.el.button(
        "Apply Now",
        background_color="#FBBF24",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        font_weight="600",
        _hover={"background-color": "#FCD34D"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        # color="#1E40AF",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )


def create_header_layout():
    """Creates the overall header layout, including logo, navigation, and apply button."""
    return rx.flex(
        create_school_logo_and_name(),
        create_navigation_menu(),
        create_apply_now_button(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
    )


def create_page_header():
    """Creates the complete page header, including styles and layout."""
    return rx.fragment(
        rx.el.style(
            """
    @font-face {
        font-family: 'LucideIcons';
        src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
    }
    """
        ),
        rx.box(
            rx.box(
                create_header_layout(),
                background_color="#1E40AF",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                color="#ffffff",
            )
        ),
    )
