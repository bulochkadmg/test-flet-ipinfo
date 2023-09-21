# https://ipapi.co/{IP}/json/ - узнать инфу по любому IP
# https://api.ipify.org/?format=json - узнать свой IP
import requests
import flet as ft

def main(page):

    # find_ip = ft.TextField(label="Введи IP для поиска", autofocus=True)
    result = ft.Column()

    def get_ip(e):
        req = requests.get(url="https://ipapi.co/91.193.172.4/json/")
        get_ip = req.json()
        result.controls.append(ft.Text(f"Твой ip - {get_ip['ip']}\nГород - {get_ip['city']}\nСтрана - {get_ip['country_name']}"))
        page.update()
    
    page.add(
        ft.ElevatedButton('Узнать свой IP', on_click=get_ip),
        result
        )


ft.app(target=main)