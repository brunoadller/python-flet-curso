import flet as ft


def main(page: ft.Page):
    def add_task(e):
        value = ft.Text(value=new_task.value)
        page.add(value)
        
        
    new_task =ft.TextField(hint_text="Insira uma Tarefa")
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)
  
    page.add(new_task, new_button)



ft.app(target=main, view=ft.FLET_APP)