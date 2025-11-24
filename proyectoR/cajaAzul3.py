import flet as ft

class BlueBox(ft.Container):
    def __init__( #Constructor
        self,
        texto: str,
        on_click_fn=None,
        mostrar_boton=True,
        ancho=200,
        alto=300
    ):
        # Lista de controles que va a contener el recuadro
        controls = [
            ft.Text(
                value=texto,
                size=20,
                weight=ft.FontWeight.BOLD,
                font_family="Arial"
            )
        ]

        # Solo agregar botón si mostrar_boton es True
        if mostrar_boton:
            controls.append(
                ft.ElevatedButton(
                    text="Acción",
                    on_click=on_click_fn  # función que se ejecutará al hacer clic
                )
            )

        # Inicializar el contenedor como siempre
        super().__init__(
            bgcolor="yellow",
            border_radius=20,
            width=ancho,
            height=alto,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=controls
            )
        )
