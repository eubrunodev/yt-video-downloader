import PySimpleGUI as sg
from pytube import YouTube
import os

# Cria a pasta "musics" na raiz do projeto, se não existir
output_folder = "videos"

sg.theme('DarkAmber')

layout = [
    [sg.Text('Insira o link do vídeo do YouTube, abaixo:')],
    [sg.Input(key='link_video', size=(50, 10), background_color='white', text_color='black')],
    [sg.Button('Baixar', size=(50, 3), button_color=("black", "green"))]
]


window = sg.Window('Video Downloader', layout=layout, font='arial')


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        link_do_video = values['link_video']

        try:
            video = YouTube(link_do_video)
            stream = video.streams.get_highest_resolution()

            # Define o caminho completo do arquivo, combinando a pasta e o nome do vídeo
            output_path = os.path.join(output_folder, f"{video.title}.mp4")

            # Baixa o vídeo e salva no caminho especificado
            stream.download(output_path)
            
            print("Download concluído com sucesso!")
            # Limpa o campo de entrada
            window["link_video"].update("")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break