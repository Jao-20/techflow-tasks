"""
Sistema de Gerenciamento de Tarefas - TechFlow Solutions
CRUD completo para controle de tarefas de equipes ágeis
"""

import json
import os
from datetime import datetime

# Arquivo onde as tarefas são salvas
ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def criar_tarefa(titulo, descricao, prioridade="media"):
    """
    Cria uma nova tarefa (CREATE).
    Prioridade pode ser: baixa, media, alta
    """
    tarefas = carregar_tarefas()

    # Gera um ID único baseado no maior ID existente
    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "a_fazer",  # a_fazer | em_progresso | concluido
        "criado_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "atualizado_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"\n✅ Tarefa #{novo_id} criada com sucesso!")
    return nova_tarefa

def listar_tarefas(status=None):
    """
    Lista todas as tarefas (READ).
    Se informar status, filtra por ele.
    """
    tarefas = carregar_tarefas()

    if status:
        tarefas = [t for t in tarefas if t["status"] == status]

    if not tarefas:
        print("\n📋 Nenhuma tarefa encontrada.")
        return []

    print("\n" + "="*60)
    print(f"{'ID':<5} {'TÍTULO':<25} {'PRIORIDADE':<12} {'STATUS':<15}")
    print("="*60)

    for t in tarefas:
        print(f"#{t['id']:<4} {t['titulo']:<25} {t['prioridade']:<12} {t['status']}")

    print("="*60)
    print(f"Total: {len(tarefas)} tarefa(s)\n")
    return tarefas

def atualizar_tarefa(id_tarefa, titulo=None, descricao=None, prioridade=None, status=None):
    """
    Atualiza uma tarefa existente (UPDATE).
    Apenas os campos informados serão alterados.
    """
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            if titulo:
                tarefa["titulo"] = titulo
            if descricao:
                tarefa["descricao"] = descricao
            if prioridade:
                tarefa["prioridade"] = prioridade
            if status:
                tarefa["status"] = status
            tarefa["atualizado_em"] = datetime.now().strftime("%d/%m/%Y %H:%M")

            salvar_tarefas(tarefas)
            print(f"\n✅ Tarefa #{id_tarefa} atualizada com sucesso!")
            return tarefa

    print(f"\n❌ Tarefa #{id_tarefa} não encontrada.")
    return None

def deletar_tarefa(id_tarefa):
    """Remove uma tarefa pelo ID (DELETE)."""
    tarefas = carregar_tarefas()
    tarefas_novas = [t for t in tarefas if t["id"] != id_tarefa]

    if len(tarefas_novas) == len(tarefas):
        print(f"\n❌ Tarefa #{id_tarefa} não encontrada.")
        return False

    salvar_tarefas(tarefas_novas)
    print(f"\n✅ Tarefa #{id_tarefa} removida com sucesso!")
    return True

def detalhar_tarefa(id_tarefa):
    """Mostra todos os detalhes de uma tarefa específica."""
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            print("\n" + "="*40)
            print(f"  TAREFA #{tarefa['id']}")
            print("="*40)
            print(f"  Título:      {tarefa['titulo']}")
            print(f"  Descrição:   {tarefa['descricao']}")
            print(f"  Prioridade:  {tarefa['prioridade']}")
            print(f"  Status:      {tarefa['status']}")
            print(f"  Criada em:   {tarefa['criado_em']}")
            print(f"  Atualizada:  {tarefa['atualizado_em']}")
            print("="*40)
            return tarefa

    print(f"\n❌ Tarefa #{id_tarefa} não encontrada.")
    return None


def menu():
    """Menu interativo do sistema."""
    while True:
        print("\n" + "="*40)
        print("  TECHFLOW - GERENCIADOR DE TAREFAS")
        print("="*40)
        print("  1. Criar nova tarefa")
        print("  2. Listar todas as tarefas")
        print("  3. Ver detalhes de uma tarefa")
        print("  4. Atualizar tarefa")
        print("  5. Deletar tarefa")
        print("  6. Filtrar por status")
        print("  0. Sair")
        print("="*40)

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (baixa/media/alta) [media]: ") or "media"
            criar_tarefa(titulo, descricao, prioridade)

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            id_t = int(input("ID da tarefa: "))
            detalhar_tarefa(id_t)

        elif opcao == "4":
            id_t = int(input("ID da tarefa a atualizar: "))
            print("Deixe em branco para não alterar o campo.")
            titulo = input("Novo título: ") or None
            descricao = input("Nova descrição: ") or None
            prioridade = input("Nova prioridade (baixa/media/alta): ") or None
            status = input("Novo status (a_fazer/em_progresso/concluido): ") or None
            atualizar_tarefa(id_t, titulo, descricao, prioridade, status)

        elif opcao == "5":
            id_t = int(input("ID da tarefa a deletar: "))
            deletar_tarefa(id_t)

        elif opcao == "6":
            status = input("Status (a_fazer/em_progresso/concluido): ")
            listar_tarefas(status)

        elif opcao == "0":
            print("\nAté logo! 👋\n")
            break

        else:
            print("\n⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
    
