# INF1407-Prog-Web
Repo for PUC-Rio Web Programming course of 2021.2

## Trabalho 1
Um simples web server em python sem uso de bibliotecas HTTP
### Instalação
Baixe o diretório **ProgWebG1** e execute o arquivo **G1_PythonWebServer.py** com um interpretador Python. Alternativamente, você também pode abrir a solução **G1-PythonWebServer.sln** com o Visual Studio 2019 e executar o programa assim.
### Uso
Você pode rodar o servidor localmente na sua máquina e acessar algumas páginas HTML, imagens e GIFs fazendo uma requisição pelo seu browser.

**Exemplo:** localhost:8080/index.html
#### Páginas Web
* index.html
* 404.html
#### Imagens
* gaivota.jpg
* pato.png
#### GIFs
* party_parrot.gif

### Testes
* O servidor é hospedado localmente corretamente e serve na porta requisitada corretamente
* O servidor serve corretamente páginas HMTL, imagens e GIFs quando especificado o arquivo na URL
* O servidor serve corretamente a página default se nenhuma página foi requisitada pelo usuário
* O servidor consegue servir mais de um cliente assíncronamente, usando threads
* O servidor consegue utilizar as variaveis armazenadas no arquivo de configuração corretamente
