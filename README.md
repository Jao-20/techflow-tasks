# TechFlow Tasks

Sistema de gerenciamento de tarefas desenvolvido como projeto prático da disciplina de Engenharia de Software — UniFECAF.

## O que é isso?

A ideia é simular o desenvolvimento de um sistema real para uma startup de logística. O sistema permite criar, listar, atualizar e deletar tarefas, controlando prioridade e status de cada uma.

Tudo foi desenvolvido seguindo metodologias ágeis, com organização via Kanban, commits bem descritos e testes automatizados rodando via GitHub Actions.

## Como rodar

Você precisa ter o Python instalado (versão 3.8 ou superior).

```bash
# Clone o repositório
git clone https://github.com/Jao-20/techflow-tasks.git

# Entre na pasta
cd techflow-tasks

# Rode o sistema
python tasks.py
```

## Como rodar os testes

```bash
python -m pytest tests/ -v
```

## Estrutura do projeto

```
techflow-tasks/
 tasks.py               # sistema principal
 README.md              # este arquivo
 .gitignore
 tests/
 test_tasks.py      # testes automatizados
.github/
 workflows/
 ci.yml         # pipeline de CI com GitHub Actions
```

## Funcionalidades

- Criar tarefa com título, descrição e prioridade
- Listar todas as tarefas
- Ver detalhes de uma tarefa específica
- Atualizar título, descrição, prioridade ou status
- Deletar tarefa
- Filtrar tarefas por status (A Fazer / Em Progresso / Concluído)

## Mudança de escopo

No início o sistema não salvava nada — as tarefas sumiam ao fechar o programa. Durante o desenvolvimento, foi adicionada persistência em arquivo JSON, resolvendo esse problema e tornando o sistema mais útil na prática.

## Autor

João — [@Jao-20](https://github.com/Jao-20)  
Disciplina de Engenharia (ADS) UniFECAF




