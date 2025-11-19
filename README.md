# ============================================================
# SISTEMA DE GERENCIAMENTO DE ESTOQUE E CADASTRO DE USUÁRIOS
# ============================================================
#
# -----------------------
# REQUISITOS DO SISTEMA
# -----------------------
# - Permitir cadastrar colaboradores com usuário e senha.
# - Armazenar itens de estoque contendo: ID, nome, categoria,
#   quantidade, preço e data de cadastro.
# - Identificar automaticamente itens com estoque baixo (<= 5).
# - Permitir remover itens para a lixeira (exclusão temporária).
# - Permitir restaurar itens da lixeira para o estoque.
# - Permitir excluir definitivamente todos os itens da lixeira.
# - Exibir gráficos de barras com quantidades dos itens.
# - Exibir itens com estoque baixo.
# - Exigir login antes de acessar o menu principal.
# - Manter interface em linha de comando (terminal).
#
#
# -----------------------
# FUNCIONALIDADES GERAIS
# -----------------------
#
# 1. Limpeza de Tela
#    - Limpa o terminal (Windows e Linux).
#
# 2. Pausa no Sistema
#    - Aguarda alguns segundos antes de continuar.
#
# 3. Aguardo de Enter
#    - Espera o usuário pressionar Enter para avançar.
#
#
# -------------------------------
# FUNCIONALIDADES DE COLABORADOR
# -------------------------------
#
# 4. Cadastrar Colaborador
#    - Solicita nome e sobrenome para gerar o usuário
#      automaticamente (ex: joao.silva).
#    - Verifica se o usuário já existe.
#    - Solicita senha numérica de 6 dígitos.
#    - Exige confirmação da senha.
#    - Registra data e hora do cadastro.
#
# 5. Login do Colaborador
#    - Compara usuário e senha com os cadastrados.
#    - Permite acesso ao menu principal caso estejam corretos.
#
# 6. Recuperação de Senha
#    - Exibe mensagem orientando contatar o administrador.
#
#
# -------------------------------
# FUNCIONALIDADES DO ESTOQUE
# -------------------------------
#
# 7. Adicionar Item ao Estoque
#    - Solicita nome, categoria, quantidade e preço.
#    - Valida campos vazios.
#    - Valida quantidade como número inteiro.
#    - Valida preço como número decimal.
#    - Gera ID automaticamente.
#    - Marca item como "estoque baixo" se quantidade <= 5.
#    - Registra data e hora do cadastro.
#
# 8. Listar Itens do Estoque
#    - Exibe todos os itens com formatação completa.
#
# 9. Mover Item para Lixeira
#    - Exclui item do estoque e move para a lixeira.
#    - Registra data e hora da exclusão.
#
# 10. Ver Itens da Lixeira
#    - Exibe itens removidos temporariamente.
#
# 11. Restaurar Item da Lixeira
#    - Retorna um item da lixeira para o estoque.
#
# 12. Esvaziar Lixeira
#    - Apaga permanentemente todos os itens da lixeira.
#
# 13. Gráfico de Itens do Estoque
#    - Cria um gráfico de barras com os nomes e quantidades.
#
# 14. Itens com Estoque Baixo
#    - Exibe apenas itens com quantidade <= 5.
#
#
# -------------------------------
# FUNCIONALIDADES DOS MENUS
# -------------------------------
#
# 15. Menu Inicial
#    - Permite cadastrar colaborador.
#    - Permite login.
#    - Opção de esqueci minha senha.
#    - Opção de sair do programa.
#
# 16. Menu Principal (Após Login)
#    - Adicionar item.
#    - Listar itens.
#    - Mover para lixeira.
#    - Ver lixeira.
#    - Restaurar item.
#    - Esvaziar lixeira.
#    - Gerar gráfico.
#    - Ver itens com estoque baixo.
#    - Voltar ao menu inicial.
#    - Sair.
#
#
# -------------------------------
# REQUISITOS DE EXECUÇÃO
# -------------------------------
#
# - Python instalado.
# - Biblioteca matplotlib instalada.
# - Execução via terminal (cmd, PowerShell ou Linux).
# - Não há uso de banco de dados; dados ficam em memória.
# - Ao fechar o programa, tudo é apagado (não persiste dados).
#
#
# =============================================
# FIM DOS COMENTÁRIOS / DOCUMENTAÇÃO DO SISTEMA
# =============================================
