from pytube import YouTube
import os
import shutil

# Substitua o URL abaixo pelo URL do vídeo que você deseja baixar
url = "https://www.youtube.com/watch?v=-WjTYUfWIgg"

# Cria um objeto YouTube
youtube = YouTube(url)

# BAIXANDO AUDIO DO VÍDEO
# Escolhe a melhor qualidade disponível
audio = youtube.streams.get_audio_only()
print(audio)
# Baixa o audio
audio.download()

# Obtém o nome original do arquivo baixado
original_filename = audio.default_filename
print(original_filename)

# Renomeia o arquivo para um nome desejado
novo_nome = f"(audio)_{original_filename}"
novo_caminho = os.path.join(os.getcwd(), novo_nome)
os.rename(original_filename, novo_caminho)

# Mova o arquivo para a pasta 'downloads'
pasta_destino = os.path.join(os.getcwd(), 'downloads')
shutil.move(novo_caminho, pasta_destino)

print(f"Download concluído. Arquivo renomeado para: {novo_nome} e movido para a pasta 'downloads")


