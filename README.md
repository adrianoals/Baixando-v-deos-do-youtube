# YouTube Downloader

Este projeto é um simples YouTube Downloader que permite baixar vídeos e áudios do YouTube. Ele utiliza a biblioteca `pytube` para realizar as operações de download.

## Estrutura do Projeto

- **src**: Contém dois módulos principais, um para downloads de vídeos e outro para downloads de áudios.
  - **video**: Módulo para download de vídeos.
    - **main.py**: Arquivo principal para executar o download de vídeos.
  - **audio**: Módulo para download de áudios.
    - **main.py**: Arquivo principal para executar o download de áudios.
- **utils**: Pasta com utilitários que exploram funções adicionais da biblioteca `pytube`.
- **downloads**: Pasta onde os arquivos baixados são armazenados.
- **requirements.txt**: Arquivo que lista as dependências necessárias para executar o projeto.

## Como Usar

1. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

2. Execute o downloader de vídeos:

    ```bash
    cd src/video
    python main.py
    ```

3. Execute o downloader de áudios:

    ```bash
    cd src/audio
    python main.py
    ```

## Dependências

- `pytube`: Biblioteca para interagir com a API do YouTube e realizar downloads.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou propor melhorias.

## Autor

Seu Nome

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

