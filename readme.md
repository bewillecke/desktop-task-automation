# Automatização do Setup Para Trabalho

Este projeto utiliza a biblioteca PyAutoGUI para automatizar a montagem do meu setup em um dia de trabalho. Entre essas tarefas, estão inclusas: abrir navegadores, acessar sites, realizar login em plataformas e reproduzir músicas no Spotify. 

## Funcionalidades

- Abrir o Google Chrome em modo anônimo.
- Acessar o Google, Gmail, Google Calendar, Notion e Globo.com.
- Realizar login automático em contas do Google e Notion.
- Reproduzir a playlist "lofi" no Spotify e ajustar o volume.
- Abrir o Visual Studio Code automaticamente.

## Estrutura do Projeto

```
.
├── main.py                # Script principal
├── search_image_function.py  # Função utilitária para localizar e clicar em imagens na tela
├── imgs/                 # Diretório contendo as imagens necessárias para localizar os elementos na tela
├── .env.example          # Exemplo de configuração de variáveis de ambiente
├── requirements.txt      # Lista de dependências do projeto
```

## Pré-requisitos

- Python 3.7 ou superior
- Pip instalado

### Dependências do projeto

Instale as dependências listadas no arquivo `requirements.txt` executando:

```bash
pip install -r requirements.txt
```

## Configuração do Ambiente

1. **Configuração das Variáveis de Ambiente:**
   - Crie um arquivo `.env` na raiz do projeto.
   - Copie o conteúdo do arquivo `.env.example`:

     ```
     EMAIL_GOOGLE = 'seu_email@gmail.com'
     SENHA_GOOGLE = 'sua_senha'
     EMAIL_NOTION = 'seu_email_notion@gmail.com'
     SENHA_NOTION = 'sua_senha_notion'
     ```
   - Substitua os valores fictícios pelas suas credenciais reais.

2. **Diretório de Imagens:**
   - Certifique-se de que o diretório `imgs/` contém todas as imagens necessárias para localizar os elementos na tela (por exemplo, ícones do Chrome, Notion, etc.).
   - As imagens devem ser capturadas com a mesma resolução e escala da tela onde o script será executado.

## Como Executar

1. Configure o ambiente conforme as instruções acima.
2. Execute o script principal:

   ```bash
   python main.py
   ```

## Pontos Importantes

- **Resolução da Tela:** Certifique-se de que a resolução da tela é a mesma usada para capturar as imagens no diretório `imgs/` (1920x1080). 
- **Atributo Confidence:**
  - Caso o script falhe ao localizar algum elemento, ajuste o valor de `confidence` no arquivo `search_image_function.py`. O valor padrão é `0.9`. Tente reduzir para `0.8` ou `0.7` se necessário.

  ```python
  img_location = pag.locateOnScreen(image, confidence=0.8)
  ```

- **Permissões no SO:** No Windows ou macOS, pode ser necessário conceder permissões ao PyAutoGUI para controlar o teclado e o mouse.

## Solução de Problemas

- **Erro ao localizar imagens:** Verifique se:
  - O diretório `imgs/` contém as imagens corretas.
  - A resolução e escala da tela correspondem às imagens usadas.

- **Erro de Importação:** Certifique-se de que todos os arquivos estão no mesmo diretório ou configure corretamente o ambiente Python.

## Licença

Este projeto é de uso pessoal e educacional. Sinta-se à vontade para modificar e utilizar conforme necessário.

---

### Contato
Caso tenha dúvidas ou sugestões, entre em contato através do meu GitHub ou e-mail.
- **[Bernardo Willecke Martins da Rocha]**
- **Celular:** (21) 98715-0359
- **E-mail:** [bewillecke@gmail.com](mailto:bewillecke@gmail.com)
- **LinkedIn:** [https://www.linkedin.com/in/bernardo-rocha-778607231/](https://www.linkedin.com/in/bernardo-rocha-778607231/)

