from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from from_number_to_letters import Thousands_Separator
from reportlab.platypus import Table, TableStyle
from datetime import date
import sys, os, json, env
    
def crear_reporte_caja(nombre_archivo, encabezado, etiquetas, valores_1, valores_2, valores_3, totales,data, data_fp, data_totales,totales_valiva, totales_withtax, total_withouttax,vta):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    ancho_pagina, alto_pagina = letter
    fuente = "Helvetica"
    tamano_fuente = 12
    c.setFont(fuente, tamano_fuente + 2)
    c.drawCentredString(ancho_pagina / 2, alto_pagina - 50, f"Informe de caja generado el {date.today().strftime('%d %B %Y')}")
    c.drawCentredString(ancho_pagina / 2, alto_pagina - 70, f"Sucursal: {vta}")
    c.drawCentredString(ancho_pagina / 2, alto_pagina - 30, encabezado)
    x_etiquetas = 100
    x_valores = 400
    y_inicial = alto_pagina - 100
    espacio_vertical = 20
    espacio_horizontal = 20
    c.line(x_etiquetas, alto_pagina - 105, x_etiquetas + 400, alto_pagina - 105)
    c.setFont(fuente, tamano_fuente)
    for etiqueta, valor1, valor2 in zip(etiquetas, valores_1, valores_2):
        c.drawString(x_etiquetas, y_inicial, etiqueta)
        c.drawRightString(x_valores, y_inicial, str(valor1))
        c.drawRightString(x_valores + 100, y_inicial, str(valor2))
        y_inicial -= espacio_vertical
    c.drawCentredString(ancho_pagina / 2, alto_pagina - 200, "RESUMEN DE VENTA")
    x_etiquetas = 100
    x_valores = 400
    y_inicial = alto_pagina - 250
    x_valores = 80
    c.line(80, alto_pagina - 255, 80 + 485, alto_pagina - 255)
    for etiquetas in valores_3:
        c.drawString(x_valores, y_inicial, str(etiquetas))
        x_valores += 100
    x_data = 135
    y_data = alto_pagina - 275
    for rows in range(3):
        for i in data[rows]:
            c.drawRightString(x_data, y_data, str(i))
            x_data += 100
        y_data -= 20
        x_data = 135
    c.line(80, 465, 85 + 480, 465)
    x_totales = 135
    y_totales = alto_pagina - 340
    x_valores = 80
    for total in totales_valiva:
        c.drawRightString(x_totales, y_totales, str(total))
        x_totales += 100
    c.drawRightString(145, alto_pagina - 370, "Total Ventas:")
    c.drawRightString(223, alto_pagina - 371, str(Thousands_Separator(total_withouttax)))
    c.drawRightString(142, alto_pagina - 395, "Total Ventas")
    c.drawRightString(142, alto_pagina - 405, "+ Impuestos:")
    c.drawRightString(223, alto_pagina - 405, str(totales_withtax))
    c.drawCentredString(ancho_pagina / 2, alto_pagina - 450, "RESUMEN DE VENTA POR FORMA DE PAGO")
    totales = ["Forma De Pago","Valor Pago","Retención","Pago Neto"]
    x_totales = 180
    y_totales = alto_pagina - 480
    x_valores = 80
    for total in totales:
        c.drawRightString(x_totales, y_totales, str(total))
        x_totales += 100

    c.line(80, alto_pagina - 485, 80 + 485, alto_pagina - 485)
    x_data = 165
    y_data = alto_pagina - 500
    len_fp = len(data_fp)
    for rows in range(len_fp):
        for i in data_fp[rows]:
            c.drawRightString(x_data, y_data, str(i))
            x_data += 105
        y_data -= 20
        x_data = 165
    c.line(80, 155, 85 + 480, 155)
    x_data = 165
    y_data = alto_pagina - 650
    for rows in range(1):
        for i in data_totales[rows]:
            c.drawRightString(x_data, y_data, str(i))
            x_data += 105
        y_data -= 20
        x_data = 165
    c.save()

def PDF(date_start, date_end,data, path, name_branch):
    result = False
    message = None
    nombre_archivo = None
    try:
        path_dir = f"{path}"
        if not os.path.exists(path_dir):
            os.mkdir(path_dir)
        nombre_archivo = f"{path_dir}/Informe.pdf"
        encabezado = f"Reporte de caja desde {date_start} hasta {date_end}"
        etiquetas = ["Tipo Documento", "Gastos", "Facturas Compras", "Facturas Ventas"]
        valores_1 = ["Entrada", 0, 0, Thousands_Separator(data['total_pf']),0]
        valores_2 = ["Salida", 0, 0, 0,0]
        valores_3 = ['% IVA', "Grabado", "Excluido", "Vr IVA", "ImpoConsumo"]
        totales = ["Forma De Pago","Valor Pago","Retención","Pago Neto"]
        _data = [
            [0,0,Thousands_Separator(data['base_0']),0,Thousands_Separator(data['ipo_0'])],
            [5,Thousands_Separator(data['base_5']),0,Thousands_Separator(data['tax_5']),Thousands_Separator(data['ipo_5'])],
            [19,Thousands_Separator(data['base_19']),0,Thousands_Separator(data['tax_19']),Thousands_Separator(data['ipo_19'])]
        ]
        data_fp = [
            ["Consignación",0,0,0],
            ["Crédito",Thousands_Separator(data['cred']),0,Thousands_Separator(data['cred'])],
            ["Efectivo_POS",Thousands_Separator(data['efec_pos']),0,Thousands_Separator(data['efec_pos'])],
            ["Efectivo_Elec",Thousands_Separator(data['efec_elect']),0,Thousands_Separator(data['efec_elect'])],
            # ["Tarjeta Crédito",Thousands_Separator(data['tc']),0,Thousands_Separator(data['tc'])],
            # ["Tarjeta Débito",Thousands_Separator(data['td']),0,Thousands_Separator(data['td'])]
        ]
        data_totales = [
            ["Totales FP",Thousands_Separator(data['total_pf']),0,Thousands_Separator(data['total_pf'])]
        ]
        totales_valiva = ["Totales",Thousands_Separator(data['total_base']),0,Thousands_Separator(data['total_tax']),Thousands_Separator(data['total_ipo'])]
        crear_reporte_caja(nombre_archivo, encabezado, etiquetas, valores_1,
            valores_2, valores_3,totales, _data, data_fp, data_totales,totales_valiva, 
            Thousands_Separator(data['totals']), data['total_base'], name_branch
        )
        result = True
        message = "Success"
        partes = nombre_archivo.partition("evangeli")
        nombre_archivo_ = f"{env.URL_APPLICATION}{partes[2]}"
    except Exception as e:
        message = str(e)

    return json.dumps({'result':result, 'message':message,'path_file':nombre_archivo_})