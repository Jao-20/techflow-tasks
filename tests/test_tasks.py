"""
Testes automatizados para o Sistema de Gerenciamento de Tarefas
TechFlow Solutions - Controle de Qualidade
"""

import unittest
import os
import json
import sys

# Adiciona o diretório pai ao path para importar o módulo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tasks import (
    criar_tarefa,
    listar_tarefas,
    atualizar_tarefa,
    deletar_tarefa,
    detalhar_tarefa,
    carregar_tarefas,
    ARQUIVO_TAREFAS
)

class TestSistemaTarefas(unittest.TestCase):
    """Testes unitários para o CRUD de tarefas."""

    def setUp(self):
        """Limpa o arquivo de tarefas antes de cada teste."""
        if os.path.exists(ARQUIVO_TAREFAS):
            os.remove(ARQUIVO_TAREFAS)

    def tearDown(self):
        """Remove o arquivo de tarefas após cada teste."""
        if os.path.exists(ARQUIVO_TAREFAS):
            os.remove(ARQUIVO_TAREFAS)


    # TESTES DE CRIAÇÃO
    

    def test_criar_tarefa_basica(self):
        """Testa se uma tarefa é criada corretamente."""
        tarefa = criar_tarefa("Implementar login", "Criar tela de autenticação")
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa["titulo"], "Implementar login")
        self.assertEqual(tarefa["status"], "a_fazer")

    def test_criar_tarefa_com_prioridade(self):
        """Testa criação de tarefa com prioridade definida."""
        tarefa = criar_tarefa("Deploy produção", "Subir versão final", prioridade="alta")
        self.assertEqual(tarefa["prioridade"], "alta")

    def test_criar_multiplas_tarefas_ids_unicos(self):
        """Testa se IDs são únicos ao criar múltiplas tarefas."""
        t1 = criar_tarefa("Tarefa 1", "Desc 1")
        t2 = criar_tarefa("Tarefa 2", "Desc 2")
        t3 = criar_tarefa("Tarefa 3", "Desc 3")
        ids = [t1["id"], t2["id"], t3["id"]]
        self.assertEqual(len(ids), len(set(ids)))  # Todos diferentes


    # TESTES DE LEITURA
 

    def test_listar_tarefas_vazio(self):
        """Testa listagem quando não há tarefas."""
        resultado = listar_tarefas()
        self.assertEqual(resultado, [])

    def test_listar_tarefas_com_dados(self):
        """Testa se lista retorna todas as tarefas criadas."""
        criar_tarefa("Tarefa A", "Desc A")
        criar_tarefa("Tarefa B", "Desc B")
        resultado = listar_tarefas()
        self.assertEqual(len(resultado), 2)

    def test_listar_por_status(self):
        """Testa filtro por status."""
        criar_tarefa("Tarefa 1", "Desc 1")
        t2 = criar_tarefa("Tarefa 2", "Desc 2")
        atualizar_tarefa(t2["id"], status="concluido")

        concluidas = listar_tarefas(status="concluido")
        self.assertEqual(len(concluidas), 1)
        self.assertEqual(concluidas[0]["titulo"], "Tarefa 2")

    
    # TESTES DE ATUALIZAÇÃO
    

    def test_atualizar_titulo(self):
        """Testa atualização do título de uma tarefa."""
        tarefa = criar_tarefa("Título antigo", "Desc")
        atualizada = atualizar_tarefa(tarefa["id"], titulo="Título novo")
        self.assertEqual(atualizada["titulo"], "Título novo")

    def test_atualizar_status(self):
        """Testa mudança de status da tarefa."""
        tarefa = criar_tarefa("Tarefa teste", "Desc")
        atualizada = atualizar_tarefa(tarefa["id"], status="em_progresso")
        self.assertEqual(atualizada["status"], "em_progresso")

    def test_atualizar_tarefa_inexistente(self):
        """Testa atualização de ID que não existe."""
        resultado = atualizar_tarefa(9999, titulo="Não existe")
        self.assertIsNone(resultado)

    # -------------------------
    # TESTES DE EXCLUSÃO
    # -------------------------

    def test_deletar_tarefa(self):
        """Testa se a tarefa é removida corretamente."""
        tarefa = criar_tarefa("Para deletar", "Desc")
        resultado = deletar_tarefa(tarefa["id"])
        self.assertTrue(resultado)
        tarefas = carregar_tarefas()
        self.assertEqual(len(tarefas), 0)

    def test_deletar_tarefa_inexistente(self):
        """Testa deleção de tarefa que não existe."""
        resultado = deletar_tarefa(9999)
        self.assertFalse(resultado)

    def test_deletar_nao_afeta_outras(self):
        """Testa se deletar uma tarefa não afeta as outras."""
        t1 = criar_tarefa("Tarefa 1", "Desc")
        t2 = criar_tarefa("Tarefa 2", "Desc")
        deletar_tarefa(t1["id"])
        tarefas = carregar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["id"], t2["id"])


    # TESTES DE VALIDAÇÃO


    def test_tarefa_tem_campos_obrigatorios(self):
        """Verifica se a tarefa contém todos os campos necessários."""
        tarefa = criar_tarefa("Teste campos", "Descrição")
        campos = ["id", "titulo", "descricao", "prioridade", "status", "criado_em", "atualizado_em"]
        for campo in campos:
            self.assertIn(campo, tarefa, f"Campo '{campo}' está faltando!")

    def test_status_inicial_e_a_fazer(self):
        """Garante que o status inicial sempre é 'a_fazer'."""
        tarefa = criar_tarefa("Nova tarefa", "Desc")
        self.assertEqual(tarefa["status"], "a_fazer")


if __name__ == "__main__":
    unittest.main(verbosity=2)
