## Projeto 5: Crawler de PDFs (A Solução Completa)

* **O que ele faz?** <br>O script combina Web Scraping e Download de arquivos em uma única ferramenta. Ele varre uma página web, identifica todos os links que apontam para arquivos `.pdf` e, em seguida, baixa todos eles automaticamente para uma pasta de destino.

* **Como Usar:**<br>
      1- Instale as bibliotecas: `pip install requests beautifulsoup4`<br>
      2- No script, altere a variável `url_da_pagina` para o site que você deseja varrer.<br>
      3- Altere a variável `pasta_destino` para o nome da pasta onde os PDFs devem ser salvos (o script a criará se não existir).<br>
      4- Execute o script (`python crawler_pdf.py`) e observe os arquivos sendo baixados.
