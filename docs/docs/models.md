---
id: models
title: Models e seu Comportamento
sidebar_position: 3
---

# Models e seu Comportamento

Os **models** no Django são responsáveis por definir a estrutura dos dados e como eles se comportam no banco de dados. No projeto `Tasks Composer`, os principais models são:

## Task

O model `Task` representa uma tarefa no sistema. Ele contém os seguintes campos:

- `title`: O título da tarefa.
- `description`: Uma descrição opcional da tarefa.
- `due_date`: A data de vencimento da tarefa.
- `completed`: Um booleano que indica se a tarefa foi concluída.
- `user`: Uma relação com o usuário (`CustomUser`) que criou a tarefa.

## CustomUser

O model `CustomUser` estende o modelo padrão de usuário do Django para incluir:

- `name`: O nome completo do usuário.

> **Nota:** O campo `avatar` foi removido do modelo `CustomUser` em uma migração posterior para simplificar o gerenciamento de dados do usuário.

Esses models são usados em várias partes do sistema, como nas [views](./views.md) e templates, para gerenciar e exibir os dados.