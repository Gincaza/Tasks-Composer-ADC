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
- `user`: Uma relação com o usuário que criou a tarefa.

[Veja o código do model `Task`](../../core/models.py).

## CustomUser

O model `CustomUser` estende o modelo padrão de usuário do Django para incluir:

- `name`: O nome completo do usuário.
- `avatar`: Uma imagem de avatar para o perfil do usuário.

[Veja o código do model `CustomUser`](../../core/models.py).

Esses models são usados em várias partes do sistema, como nas views e templates, para gerenciar e exibir os dados.