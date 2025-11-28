# import flet as ft

# def main(page: ft.Page):

#     # Muy importante:
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     avatar = ft.Container(
#         width=60,
#         height=60,
#         bgcolor="yellow",
#         border_radius=30
#     )

#     indicador_activo = ft.Container(
#         width=15,
#         height=15,
#         bgcolor="green",
#         border_radius=20,
#         border=ft.border.all(2, "white"),
#     )

#     wrapper = ft.Stack(
#         [
#             avatar,
#             ft.Container(
#                 indicador_activo,
#                 alignment=ft.alignment.bottom_right
#             )
#         ],
#         width=60,
#         height=60
#     )

#     page.add(wrapper)

# ft.app(target=main)





















# import flet as ft

# def main(page: ft.Page):

#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     avatar = ft.Container(
#         width=200,
#         height=200,
#         bgcolor="yellow",
#         border_radius=100
#     )

#     indicador_activo = ft.Container(
#         width=40,
#         height=40,
#         bgcolor="green",
#         border_radius=20,
#         border=ft.border.all(2, "white"),
#     )

#     wrapper = ft.Stack(
#         [
#             avatar,
#             ft.Container(
#                 indicador_activo,
#                 alignment=ft.alignment.bottom_right
#             )
#         ],
#         width=150,
#         height=150
#     )

#     page.add(
#         ft.Row(
#             alignment=ft.MainAxisAlignment.CENTER,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[wrapper]
#         )
#     )

# ft.app(target=main)


























# import flet as ft
# import datetime
# import asyncio

# def main(page: ft.Page):

#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.expand = True

#     # Texto donde mostraremos la hora
#     hora_actual = ft.Text(
#         value=datetime.datetime.now().strftime("%H:%M:%S"),
#         size=30,
#         weight="bold"
#     )

#     # Hora objetivo (FORMATO HH:MM)
#     hora_objetivo = "21:31"

#     # Para evitar imprimir muchas veces en el mismo día
#     last_run_date = None  # guardará la fecha en la que ya ejecutó

#     async def actualizar_hora():
#         nonlocal last_run_date

#         while True:
#             ahora_hms = datetime.datetime.now()
#             ahora_str_hms = ahora_hms.strftime("%H:%M:%S")
#             ahora_str_hm = ahora_hms.strftime("%H:%M")  # formato HH:MM

#             hora_actual.value = ahora_str_hms

#             # Cuando llegue la hora (HH:MM) y aún no se haya ejecutado hoy:
#             if ahora_str_hm == hora_objetivo:
#                 hoy = ahora_hms.date()
#                 if last_run_date != hoy:
#                     # Acción a ejecutar
#                     mensaje = ft.Text("¡Ya es la hora establecida!")
#                     page.add(mensaje)
#                     last_run_date = hoy

#             page.update()
#             await asyncio.sleep(1)

#     # IMPORTANTE: pasar la función, NO llamarla
#     page.run_task(actualizar_hora)

#     # Avatar de ejemplo
#     avatar = ft.Container(width=200, height=200, bgcolor="yellow", border_radius=100)
#     indicador = ft.Container(width=40, height=40, bgcolor="green", border_radius=20)

#     wrapper = ft.Stack(
#         [avatar, ft.Container(indicador, alignment=ft.alignment.bottom_right)],
#         width=200,
#         height=200
#     )

#     page.add(
#         ft.Row(
#             alignment=ft.MainAxisAlignment.CENTER,
#             spacing=30,
#             controls=[wrapper, hora_actual]
#         )
#     )

# ft.app(target=main)

























import flet as ft
import datetime
import asyncio

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    texto_estado = ft.Text("Esperando la hora...", size=25)

    page.add(texto_estado)

    # Hora objetivo (HH:MM)
    hora_objetivo = "21:45"
    ejecutado = False

    async def reloj_tarea():
        nonlocal ejecutado

        while True:
            ahora = datetime.datetime.now().strftime("%H:%M")
            
            if ahora == hora_objetivo and not ejecutado:
                texto_estado.value = "¡YA ES LA HORA!"
                page.update()
                ejecutado = True

            await asyncio.sleep(1)

    page.run_task(reloj_tarea)

ft.app(target=main)
