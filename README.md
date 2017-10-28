# ads-file-scraping
Scraper dos arquivos das disciplinas do curso de ADS do IFBA Salvador

## Requisitos
   * python3-lxml
   * python3-requests
   
## Como usar

- Execute a aplicação com:
    - `python __main__.py`

- Informe o nome do novo diretório onde os arquivos devem ser salvos.

- Informe o file page. Essa informação representa o id da disciplina na wiki, por exemplo: 

    - A página https://ads.ifba.edu.br/file11 possui o file page como "file11".

- Após isso, o script irá baixar todo o conteúdo da página e de seus subdiretórios e salvará dentro do diretório informado anteriormente.
