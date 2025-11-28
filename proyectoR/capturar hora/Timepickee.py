import flet as ft

def main(page: ft.Page):

    hora_seleccionada = ""   # ← variable donde guardarás la hora

    def seleccionar_hora(e):
        nonlocal hora_seleccionada
        hora_seleccionada = time_picker.value.strftime("%H:%M")
        texto.value = f"Hora guardada: {hora_seleccionada}"
        page.update()

    texto = ft.Text("No hay hora seleccionada")

    time_picker = ft.TimePicker(on_change=seleccionar_hora)

    btn_hora = ft.ElevatedButton(
        "Seleccionar hora",
        on_click=lambda e: page.open(time_picker)
    )

    page.add(texto, btn_hora, time_picker)

ft.app(target=main)
