import requests
from requests_html import HTML


url='https://www.rava.com/empresas/perfil.php?e=CEDEARGOLD'




def url_to_text(url,filename='algo.html'):
    import requests
    from requests_html import HTML
    r=requests.get(url)
    if r.status_code==200:
        html_text=r.text
        r_html=HTML(html=html_text)
        table=r_html.find('table')[7]
        rows=table.find('tr')
        #-----------------------------------------------#
        valor=rows[0].find('td')[0].find('tr')[0].text
        #print(valor)
        valor=float(valor.replace('.', '', 1).replace(',', '.', 1))
        #-----------------------------------------------#
        variacion=rows[0].find('td')[0].find('tr')[1].text
        variacion_en_porcentaje=float(variacion[0:5].replace('.','',1).replace(',','.',1))
        variacion_actualizado=variacion[8:-1]

    return valor, variacion_en_porcentaje, variacion_actualizado

def scrap(url):
    import requests
    from requests_html import HTML
    html_text=url_to_text(url)
    print(html_text)

#scrap(url)
#valor, variacion_en_porcentaje, variacion_actualizado=url_to_text(url)

#print('valor :', valor)
#print('variacion_en_porcentaje :', variacion_en_porcentaje)
#print('variacion_actualizado :', variacion_actualizado)
