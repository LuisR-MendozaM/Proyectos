import flet as ft

class BlueBox(ft.Container):
    def __init__(self, texto: str, on_click_fn=None, ancho=200, alto=300):
        super().__init__(
            bgcolor="yellow",
            border_radius=20,
            width=ancho,
            height=alto,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        value=texto,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        font_family="Arial"
                    ),
                    ft.ElevatedButton(
                        text="Acción",
                        on_click=on_click_fn  # ← función diferente por recuadro
                    )
                ]
            )
        )
