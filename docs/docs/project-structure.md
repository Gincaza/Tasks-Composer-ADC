---
id: project-structure
title: Estrutura do Projeto
sidebar_position: 2
---

# Estrutura do Projeto

O projeto Tasks Composer está organizado da seguinte forma:

## Diretórios Principais

- **`core/`**: Contém a lógica principal da aplicação, incluindo:
  - **`models.py`**: Define os modelos de dados, como `Task` e `CustomUser`.
  - **`views.py`**: Contém as funções de visualização para lidar com as requisições HTTP.
  - **`templates/`**: Armazena os templates HTML para renderização das páginas.
  - **`static/`**: Contém arquivos estáticos como CSS, JavaScript e imagens.

- **`config/`**: Configurações do projeto Django, incluindo:
  - **`settings.py`**: Configurações globais do projeto.
  - **`urls.py`**: Define as rotas do projeto.
  - **`wsgi.py`** e **`asgi.py`**: Arquivos para configuração de servidores WSGI e ASGI.

- **`docs/`**: Documentação do projeto gerada com Docusaurus, incluindo:
  - **`docusaurus.config.js`**: Configurações do Docusaurus.
  - **`docs/`**: Contém os arquivos de documentação em Markdown.
  - **`src/`**: Arquivos de personalização e componentes React para o site de documentação.

## Arquivos Importantes

- **`manage.py`**: Script de gerenciamento do Django.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Informações gerais sobre o projeto.
- **`LICENSE`**: Licença do projeto.

Essa estrutura foi projetada para manter o código organizado e facilitar a colaboração entre desenvolvedores.