# ads-file-scraping
Scraper dos arquivos das disciplinas do curso de ADS do IFBA Salvador

## Requisitos
   * python3-lxml
   * python3-requests
   
## Como usar

- Execute a aplicação, informe o nome do diretório que será criado na pasta atual do aplicativo, que será onde os arquivos devem ser salvos. 

- Informe o file page. Essa informação representa o id da disciplina na wiki, por exemplo: 

    - https://ads.ifba.edu.br/file11 é o link para a página de Banco de Dados, onde o id da mesma é "file11", que é a informação a ser informada como file page.

- Após isso, o script irá baixar todo o conteúdo da página e de seus subdiretórios e salvará dentro do diretório informado.
