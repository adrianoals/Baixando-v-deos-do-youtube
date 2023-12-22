# Como instalar o Pytube
# pip install pytube

# Documentação:
# https://pytube.io/en/latest/

# Este código apresenta algumas outras funcionalidades da biblioteca pytube, como verificar a lista de resoluçoes e formatos de arquivos

from pytube import YouTube
import os
import shutil

# Substitua o URL abaixo pelo URL do vídeo que você deseja baixar
url = "https://www.youtube.com/watch?v=iay9vOPrVeI"

# Cria um objeto YouTube
youtube = YouTube(url)

# Obtém a lista de todas as streams disponíveis para o vídeo
streams = youtube.streams
print(streams)
print()

# Filtra as streams para aquelas com extensão mp4
filtered_streams = streams.filter(file_extension="mp4")
print(filtered_streams)
print()

# Filtrando só por vídeo
video = streams.filter(only_video=True)
print(video)
print()

# Filtrando só por áudio
audio = streams.filter(only_audio=True)
print(audio)
print()

# BAIXANDO VIDEO
# Escolhe a stream com a maior resolução disponível de vídeo
video_high_resolution = streams.get_highest_resolution()
print(video_high_resolution)
print()

# Baixa o vídeo
video_high_resolution.download()
print("Download concluído.")

# Obtém o nome original do arquivo baixado
original_filename = video_high_resolution.default_filename
print(original_filename)

# Renomeia o arquivo para um nome desejado
novo_nome = f"video_teste{original_filename}"
novo_caminho = os.path.join(os.getcwd(), novo_nome)
os.rename(original_filename, novo_caminho)

# Movendo o arquivo para a pasta 'downloads'
pasta_destino = os.path.join(os.getcwd(), 'downloads')
shutil.move(novo_caminho, pasta_destino)

print(f"Download concluído. Arquivo renomeado para: {novo_nome} e movido para a pasta 'downloads")
