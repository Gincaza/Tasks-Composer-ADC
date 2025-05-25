---
id: views
title: Views e Funcionalidades
sidebar_position: 4
---

# Views e Funcionalidades

As **views** no Django são responsáveis por lidar com as requisições e retornar respostas apropriadas. No projeto `Tasks Composer`.

## Dashboard

- **Descrição**: Exibe o painel principal com contagem de tarefas pendentes, concluídas e atrasadas.
- **Caminho**: `/dashboard/`

## Tasks

- **Descrição**: Gerencia a criação, edição e listagem de tarefas do usuário.
- **Caminho**: `/tasks/`

## Delete Task

- **Descrição**: Permite a exclusão de uma tarefa específica.
- **Caminho**: `/tasks/<int:task_id>/delete/`

## Mark Task Completed

- **Descrição**: Marca uma tarefa como concluída ou não concluída.
- **Caminho**: `/tasks/<int:task_id>/mark_completed/`

## Settings

- **Descrição**: Exibe a página de configurações do usuário.
- **Caminho**: `/settings/`

## Update User Info

- **Descrição**: Permite que o usuário atualize suas informações, como nome e avatar.
- **Caminho**: `/settings/update_user_info/`

## Home

- **Descrição**: Exibe a página inicial para visitantes.
- **Caminho**: `/`

## Register

- **Descrição**: Permite que novos usuários se registrem no sistema.
- **Caminho**: `/register/`