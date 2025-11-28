import flet as ft
import datetime
import asyncio


class Reloj(ft.Column):
    def __init__(self, page, hora_objetivo: str, on_trigger):
        super().__init__()

        self.page = page
        self.hora_objetivo = hora_objetivo      # ej. "08:30 PM"
        self.on_trigger = on_trigger            # función a ejecutar
        self.ejecutado_hoy = None              # para evitar ejecución múltiple

        # Texto que muestra la hora actual
        self.texto_hora = ft.Text(
            "–:– ––",
            size=28,
            weight="bold"
        )

        self.controls = [self.texto_hora]

        # Iniciar tarea de reloj
        self.page.run_task(self.reloj_loop)

    # Tarea asincrónica
    async def reloj_loop(self):
        while True:
            ahora = datetime.datetime.now()

            # Hora formateada en AM/PM
            hora_actual_str = ahora.strftime("%I:%M:%S %p")
            self.texto_hora.value = hora_actual_str

            # ============================
            # DETECCIÓN DE HORA OBJETIVO
            # ============================
            hora_actual_sin_segundos = ahora.strftime("%I:%M %p")

            if hora_actual_sin_segundos == self.hora_objetivo:
                hoy = ahora.date()

                if self.ejecutado_hoy != hoy:
                    self.on_trigger()          # Ejecutar acción
                    self.ejecutado_hoy = hoy   # Marcar ejecución del día

            self.update()
            await asyncio.sleep(1)


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.expand = True

    # Acción a ejecutar cuando llegue la hora
    def mi_accion():
        page.add(ft.Text("¡SE EJECUTÓ LA ACCIÓN A LA HORA PROGRAMADA!", color="green"))

    # Crear reloj con hora objetivo
    reloj = Reloj(page, "10:15 PM", mi_accion)

    page.add(reloj)


ft.app(target=main)
