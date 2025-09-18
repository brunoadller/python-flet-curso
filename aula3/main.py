import flet as ft


def main(page: ft.Page):
    
    def add_task(e):
        print(new_button)
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()
    
    new_task = ft.TextField(hint_text="Insira uma tarefa...", expand=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    card  = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls= [
                    new_task,
                    new_button
                ]
            )
        ]
    )
    page.add(card)

ft.app(target= main, view=ft.FLET_APP)