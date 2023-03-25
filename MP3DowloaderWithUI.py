import os
from tkinter import *
from tkinter import filedialog
from pytube import YouTube

def download_audio():
    # Obtenemos la URL del video de YouTube ingresada por el usuario
    video_url = url_entry.get()

    # Pedimos al usuario que seleccione la ubicación donde quiere guardar el archivo de audio
    audio_path = filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=[('Archivo de audio', '*.mp3')])

    # Descargamos el video y extraemos el audio en formato mp3
    yt = YouTube(video_url)
    audio = yt.streams \
        .filter(only_audio=True, file_extension='mp4') \
        .order_by('abr') \
        .desc() \
        .first()

    if audio:
        output_file = audio.download(output_path='/tmp')
        base, ext = os.path.splitext(output_file)
        new_file = base + '.mp3'
        os.rename(output_file, new_file)
        os.replace(new_file, audio_path)
        status_label.config(text='Audio descargado en ' + audio_path)
    else:
        status_label.config(text='No se encontró ningún audio en formato mp3 en el video.')

# Creamos la ventana principal
root = Tk()
root.title('Descargar audio de YouTube')

# Creamos los widgets de la interfaz gráfica
url_label = Label(root, text='Ingresa la URL del video de YouTube:')
url_entry = Entry(root, width=50)
download_button = Button(root, text='Descargar audio', command=download_audio)
status_label = Label(root, text='')

# Acomodamos los widgets en la ventana principal
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry.grid(row=0, column=1, padx=10, pady=10)
download_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutamos el bucle principal de la ventana
root.mainloop()
