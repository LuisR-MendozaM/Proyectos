import flet as ft
import threading
import time
import serial
from cajaAzul3 import BlueBox



class UI(ft.Container):
    def __init__(self):
        super().__init__(expand=True)
        
        self.color_teal = ft.Colors.GREY_300

        # Inicializar componentes de UI
        self._initialize_ui_components()
        
        # ESTA ES LA LÍNEA CLAVE QUE FALTABA:
        self.content = self.resp_container

    def _initialize_ui_components(self):
        """Inicializa todos los componentes de la interfaz de usuario"""

    #################### TEMPERATURA ####################
        # Variable para almacenar el valor de la temperatura
        self.temperatura = 20

        # Texto para mostrar la temperatura
        self.texto_temperatura = ft.Text(
            value=(f"{self.temperatura}°C"), # Muestra el valor inicial de la temperatura
            font_family="Arial",
            size=20,
            weight=ft.FontWeight.BOLD
        )

#################### HUMEDAD ####################
        # Variable para almacenar el valor de la humedad
        self.humedad = 70

        # Texto para mostrar la humedad
        self.texto_humedad = ft.Text(
            value=(f"{self.humedad}%"),# Muestra el valor inicial de la humedad
            font_family="Arial",
            size=20,
            weight=ft.FontWeight.BOLD
        )

#################### presion ####################
        # Variable para almacenar el valor de la humedad
        self.presion = 90

        # Texto para mostrar la humedad
        self.texto_presion = ft.Text(
            value=(f"{self.presion}Pa"),# Muestra el valor inicial de la humedad
            font_family="Arial",
            size=20,
            weight=ft.FontWeight.BOLD
        )

#################### HUMEDAD ####################
        # Variable para almacenar el valor de la humedad
        self.frecuencia = 60

        # Texto para mostrar la humedad
        self.texto_frecuencia = ft.Text(
            value=(f"{self.frecuencia}Hz"),# Muestra el valor inicial de la humedad
            font_family="Arial",
            size=20,
            weight=ft.FontWeight.BOLD
        )



        # Contenedores principales con contenido
        self.home_container_1 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            expand=True,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text("Home", 
                            font_family="FontAwesome", 
                            size=15, 
                            weight=ft.FontWeight.BOLD,
                    ),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.location_container_1 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            expand=True,
            padding=20,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Ubicacion", 
                            font_family="FontAwesome", 
                            size=15, 
                            weight=ft.FontWeight.BOLD,
                    ),
                    ft.Container(
                        expand=True,
                        bgcolor="red",
                        border_radius=20,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    # scroll=ft.ScrollMode.AUTO,
                                    controls=[
                                        BlueBox(f"{self.temperatura}°C", mostrar_boton=False, ancho=100, alto=100),
                                        # BlueBox(f"{self.humedad}%"),
                                        # BlueBox(f"{self.presion}Pa"),
                                        # BlueBox(f"{self.frecuencia}Hz"),

                                        BlueBox(f"{self.humedad}%", on_click_fn=self.accion_humedad),
                                        BlueBox(f"{self.presion}Pa", on_click_fn=self.accion_presion),
                                        BlueBox(f"{self.frecuencia}Hz", on_click_fn=self.accion_frecuencia),


                                        # ft.Container(
                                        #     bgcolor="blue",
                                        #     border_radius=20,
                                        #     width=200,
                                        #     height=300,
                                        #     alignment=ft.alignment.center,
                                        #     content=self.texto_temperatura
                                        # ),
                                        # ft.Container(
                                        #     bgcolor="blue",
                                        #     border_radius=20,
                                        #     width=200,
                                        #     height=300,
                                        #     alignment=ft.alignment.center,
                                        #     content=self.texto_humedad
                                        # ),
                                        # ft.Container(
                                        #     bgcolor="blue",
                                        #     border_radius=20,
                                        #     width=200,
                                        #     height=300,
                                        #     alignment=ft.alignment.center,
                                        #     content=self.texto_presion
                                        # ),
                                        # ft.Container(
                                        #     bgcolor="blue",
                                        #     border_radius=20,
                                        #     width=200,
                                        #     height=300,
                                        #     alignment=ft.alignment.center,
                                        #     content=self.texto_frecuencia
                                        # ),
                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    # scroll=ft.ScrollMode.AUTO,
                                    controls=[
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    # scroll=ft.ScrollMode.AUTO,
                                    controls=[
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                        ft.Container(
                                            bgcolor="blue",
                                            border_radius=20,
                                            width=200,
                                            height=300,
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.calendar_container_1 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            expand=True,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text("Calendario", 
                            font_family="FontAwesome", 
                            size=15, 
                            weight=ft.FontWeight.BOLD,
                    ),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.setting_container_1 = ft.Container(
            bgcolor=self.color_teal,
            border_radius=20,
            expand=True,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text("Configuracion", 
                            font_family="FontAwesome", 
                            size=15, 
                            weight=ft.FontWeight.BOLD
                    ),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.container_list_1 = [
            self.home_container_1, 
            self.location_container_1, 
            self.calendar_container_1, 
            self.setting_container_1
        ]
        
        self.container_1 = ft.Container(content=self.container_list_1[0], expand=True)

        # BUTTON CONNECT
        self.btn_connect = ft.Container(
            width=130,
            height=50,
            bgcolor=ft.Colors.AMBER,
            border_radius=50,
            alignment=ft.alignment.center,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            on_hover=self.Check_On_Hover,
            content=ft.Text("Texto"),
            on_click = lambda e: self.change_page_manual(0)
        )

        self.btn_connect2 = ft.Container(
            width=130,
            height=50,
            bgcolor=ft.Colors.AMBER,
            border_radius=50,
            alignment=ft.alignment.center,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            on_hover=self.Check_On_Hover,
            content=ft.Text("Texto"),
            on_click = lambda e: self.change_page_manual(1)
        )

        self.navigation_container = ft.Container(
            col=1.6,
            expand=True,
            bgcolor=self.color_teal,
            border_radius=10,
            padding=ft.padding.only(top=20),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[
                    self.btn_connect,
                    self.btn_connect2,
                ]
            )
        )

        self.frame_2 = ft.Container(
            col=10,
            bgcolor="blue",
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    self.container_1,
                ]
            )   
        )

        self.container_3 = ft.Container(
            bgcolor="blue",
            expand=True,
            border_radius=10,
            alignment=ft.alignment.center,
            padding=10
        )

        # Contenedores de configuración
        self.comunicacion_container = ft.Container(
            # bgcolor="pink",
            expand=True,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        self.variables_container = ft.Container(
            expand=True,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                bgcolor=self.color_teal,
                                alignment=ft.alignment.center,
                                border_radius=10,
                                width=10,
                                height=100,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "Set point",
                                            font_family="FontAwesome",
                                            size=15,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )

        self.container_3.content = self.comunicacion_container
        
        # Layout responsivo principal
        self.resp_container = ft.ResponsiveRow(
            controls=[
                self.navigation_container,
                self.frame_2,
            ]
        )

    def accion_temperatura(self, e):
        print("Botón de temperatura presionado")

    def accion_humedad(self, e):
        print("Botón de humedad presionado")

    def accion_presion(self, e):
        print("Botón de presión presionado")

    def accion_frecuencia(self, e):
        print("Botón de frecuencia presionado")

    def change_page_manual(self, index):
        self.container_1.content = self.container_list_1[index]
        self.update()


    def Check_On_Hover(self, e):
        ctrl = e.control  # el control que generó el evento
        is_hover = (e.data == "true" or e.data is True)  # cubre string y booleano

        if is_hover:
            ctrl.border = ft.border.all(3, ft.Colors.GREEN_700)
        else:
            ctrl.border = ft.border.all(2, ft.Colors.TRANSPARENT)

        ctrl.update()
    
    def change_page(self, e):
        index = e.control.selected_index
        self.container_1.content = self.container_list_1[index]
        self.update()
        # print(index)

    


def main(page: ft.Page):
    page.title = "Sistema de Monitoreo"
    page.window_width = 1316
    page.window_height = 570
    page.window_resizable = False
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    # page.bgcolor = ft.Colors.WHITE
    page.window.bgcolor = ft.Colors.TRANSPARENT
    

    ui = UI()
    page.add(ui)


if __name__ == "__main__":
    ft.app(target=main)
