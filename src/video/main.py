from pytube import YouTube
import os
import shutil

# Substitua o URL abaixo pelo URL do vídeo que você deseja baixar
url = "https://www.youtube.com/watch?v=iay9vOPrVeI"

# Cria um objeto YouTube
youtube = YouTube(url)

# BAIXANDO VIDEO
# Escolhendo a melhor qualidade disponível
video = youtube.streams.get_highest_resolution()
print(video)
# Baixa o vídeo
video.download()

# Obtém o nome original do arquivo baixado
original_filename = video.default_filename
print(original_filename)

# Renomeia o arquivo para um nome desejado
novo_nome = f"(video4)_{original_filename}"
novo_caminho = os.path.join(os.getcwd(), novo_nome)
os.rename(original_filename, novo_caminho)

# Mova o arquivo para a pasta 'downloads'
pasta_destino = os.path.join(os.getcwd(), 'downloads')
shutil.move(novo_caminho, pasta_destino)

print(f"Download concluído. Arquivo renomeado para: {novo_nome} e movido para a pasta 'downloads")