# BlueBox.py
import flet as ft

class BlueBox(ft.Container):
    def __init__(self, texto: str, ancho=200, alto=300):
        super().__init__(
            bgcolor="yellow",
            border_radius=20,
            width=ancho,
            height=alto,
            alignment=ft.alignment.center,
            content=ft.Text(
                value=texto,
                size=20,
                weight=ft.FontWeight.BOLD,
                font_family="Arial"
            )
        )
