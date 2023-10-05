import reflex as rx
import calendar
import locale
from datetime import datetime


locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

dias_lista: list = [x for x in range(1, 32)]
meses_lista: list = [x.capitalize() for x in calendar.month_name[1:]]
year_lista: list = [x for x in range(2021, 2030)]


class MainState(rx.State):
    dia: str = ''
    mes: str = ''
    year: str = ''
    fecha: str = ''

    @rx.var
    def establecer_fecha(self):
        if self.dia and self.mes and self.year:
            self.fecha = f'{self.dia}/{str(meses_lista.index(self.mes) + 1)}/{self.year}'
            formato_fecha: str = '%d/%m/%Y'
            try:
                datetime.strptime(self.fecha, formato_fecha)
                return self.fecha
            except ValueError:
                self.fecha = 'la fecha no es correcta'
        else:
            self.fecha = ''
        return self.fecha


def caja_fecha():
    return rx.box(
        rx.hstack(
            rx.text(
                'Fecha:',
                color='#6b888f',
                fontStyle='italic'
            ),
            rx.box(
                rx.select(
                    dias_lista,
                    placeholder='Día',
                    on_change=MainState.set_dia,
                ),
            ),
            rx.box(
                rx.select(
                    meses_lista,
                    placeholder='Mes',
                    on_change=MainState.set_mes,
                ),
            ),
            rx.box(
                rx.select(
                    year_lista,
                    placeholder='Año',
                    on_change=MainState.set_year,
                ),
            ),
        ),
        mt='20px',
        bg='#d4f5ce',
        padding='10px',
        borderRadius='7px'
    )


def mensaje_fecha() -> rx.box:
    return rx.box(
        rx.heading(
            MainState.establecer_fecha,
            fontWeight='400',
            color='#0080ff',
            textAlign='center',
            fontSize='20px'
        )
    )


def index() -> rx.component:
    return rx.vstack(
        caja_fecha(),
        mensaje_fecha()
    )


app = rx.App()
app.add_page(index)
app.compile()
