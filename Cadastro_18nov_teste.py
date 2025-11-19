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


import datetime, time, os
import matplotlib.pyplot as plt
estoque = []
lixeira = []
colaboradores =[]
proximo_id = 1

# ---------------- FUNÇÕES ÚTEIS ----------------
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def aguardar_enter():
    input("\nPressione Enter para continuar...")        
        
def pausa(segundos):
    time.sleep(segundos)
           
def senha_usuario():
    print("\n=== Cadastro de novo colaborador ===")
    
    nome = input("Digite o primeiro nome do colaborador: ").strip().lower()
    while nome == "":
        print("O nome não pode ficar em branco.")
        nome = input("Digite o primeiro nome do colaborador: ").strip().lower()
        
    sobrenome = input("Digite o sobrenome do colaborador: ").strip().lower()
    while sobrenome == "":
        print("O sobrenome não pode ficar em branco.")
        sobrenome = input("Digite o sobrenome do colaborador: ").strip().lower()
    usuario = f"{nome}.{sobrenome}"
    
    for colaborador in colaboradores:
        if colaborador["usuario"] == usuario:
            print(f"O login '{usuario}' já existe. Tente outro sobrenome.")
            pausa(2)
            limpar_tela()
            return
        
    senha = input("Digite uma senha numerica de 6 digitos: ")
    while not (senha.isdigit() and len(senha) == 6):
        print("Senha inválida. A senha deve ter exatamente 6 dígitos numericos.")
        senha = input("Digite uma senha numerica de 6 digitos: ")
        
    confirmacao = input("Confirme a senha: ")
    while confirmacao != senha:
        print("As senhas não coincidem. Tente novamente.")
        confirmacao = input("Confirme a senha: ")
    colaborador = {"usuario": usuario, "senha": senha,
                   'data_usuario': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    colaboradores.append(colaborador)
    print(f"\nCadastro de colaborador realizado com sucesso! Login: '{usuario}'.")    
    aguardar_enter()
    limpar_tela()
    return


def adicionar_item():
    global proximo_id
    
    nome = input(f"Digite o nome do item: ").strip().lower()
    categoria = input("Digite a categoria do item: ").strip().lower()
    quantidade_str = input("Digite a quantidade do item: ").strip()
    preco_str = input("Digite o preço do item: ").strip()
    
    # Verifica campos vazios
    if not nome or not categoria or not quantidade_str or not preco_str:
        print("\nErro: Nenhum campo pode ficar vazio!")
        pausa(2)
        limpar_tela()
        return

    # Validação de número
    if not quantidade_str.isdigit():
        print("\nErro: Quantidade inválida!")
        pausa(2)
        limpar_tela()
        return
    try:
        preco = float(preco_str)
    except:
        print("\nErro: Preço inválido!")
        pausa(2)
        limpar_tela()
        return

    quantidade = int(quantidade_str)
    
    item = {
        'id': proximo_id,
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco,
        "estoque_baixo" : quantidade <= 5,
        'data_cadastro': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
    
    estoque.append(item)
    proximo_id += 1
    print("\nItem adicionado com sucesso!")
    print("Cadastro: ", proximo_id-1)
    aguardar_enter()
    limpar_tela()
    
    
def listar_itens():
    if not estoque:
        print("Nenhum item cadastrado.")
        pausa(3)
        return
    limpar_tela()
    print("Itens do Estoque.")
    print("\nID       Nome         Categoria      Quantidade   Preço         Data/Hora Cadastro")
    print("-"*70)
    for item in estoque:
        print(f"{item['id']:<8} {item['nome']:<12} {item['categoria']:<14} {item['quantidade']:<12} R$ {item['preco']:<10.2f} {item['data_cadastro']}")
    aguardar_enter()
        
def lixeira_mover():
    if not estoque:
        print("Nenhum item cadastrado para mover para a Lixeira.")
        return
    try:
        id_lixeira = int(input("Digite o ID do item que deseja mover para a Lixeira: "))
    except ValueError:
        print("Id invalido. Tente novamente.")
        return
    for item in estoque:       
        if item["id"] == id_lixeira:
            item['data_exclusão'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            lixeira.append(item)
            estoque.remove(item)
            print("\nItem movido para a lixeira com sucesso!")
            pausa(3)
            limpar_tela()
            return
    print(f"O item id {id_lixeira} não cadastrado no estoque ou ja foi removido para a lixeira.")
    pausa(3)
    limpar_tela()
    
    
def ver_lixeira():
        if not lixeira:
            print("Lixeira vazia. Nada para mostrar.")
            pausa(3)
            limpar_tela()
            return
        else:
            limpar_tela()
            print("Itens na Lixeira:")
            print("\nID       Nome         Categoria      Quantidade   Preço         Data/Hora Exclusão")
            print("-"*70)
            for item in lixeira:
                print(f"{item['id']:<8} {item['nome']:<12} {item['categoria']:<14} {item['quantidade']:<12} R$ {item['preco']:<10.2f} {item['data_exclusão']}")
            aguardar_enter()
                
def restaurar_item():
    if not lixeira:
        print("Lixeira vazia. Nenhum item para restaurar.")
        return
    try:
        id_restaurar = int(input("Digite o ID do item que deseja restaurar: "))
    except ValueError:
        print("Id invalido. Tente novamente.")
        pausa(3)
        limpar_tela()
        return
    for item in lixeira:
        if item["id"] == id_restaurar:
            estoque.append(item)
            lixeira.remove(item)
            print("\nItem restaurado com sucesso!")
            pausa(3)
            limpar_tela()
            return
    print(f"O item id {id_restaurar} não encontrado na lixeira.")
    
    
def esvaziar_lixeira():
    if not lixeira:
        print("Lixeira vazia. Nenhum item para excluir.")
        pausa(3)
        limpar_tela()
        return
    else:
        lixeira.clear()
        print("Itens excluidos permanentemente!")
        pausa(3)
        limpar_tela()
        
def grafico_itens_estoque():
    if not estoque:
        print("Nenhum item no estoque para gerar o gráfico.")
        pausa(2)
        limpar_tela()
        return
   
    nomes = [item['nome'] for item in estoque]
    quantidades = [item['quantidade'] for item in estoque]
    
    plt.bar(nomes, quantidades, color='blue')
    plt.xlabel('Itens')
    plt.ylabel('Quantidades')
    plt.title('Itens no Estoque')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
def estoque_baixo():
    itens_baixo_estoque = [item for item in estoque if item['estoque_baixo']]
    if not itens_baixo_estoque:
        print("Nenhum item com estoque baixo.")
        pausa(2)
        limpar_tela()
        return
    limpar_tela()
    print("Itens com Estoque Baixo (menos de 5 unidades):")
    print("\nID       Nome         Categoria      Quantidade   Preço         Data/Hora Cadastro")
    print("-"*70)
    for item in itens_baixo_estoque:
        print(f"{item['id']:<8} {item['nome']:<12} {item['categoria']:<14} {item['quantidade']:<12} R$ {item['preco']:<10.2f} {item['data_cadastro']}")
    aguardar_enter()
        
               
def menu_inicial():
    while True:
        print("\nBem vindo ao sistema de gerenciamento de cadastro.")
        print("\n1. Cadastrar Colaborador")
        print("2. Fazer Login")
        print("3. Esqueçi minha senha")
        print("S. Sair")
        
        escolha = input("\nEscolha a opção desejada: ")
        
        if escolha == '1':
            senha_usuario()
        elif escolha == '2':
            usuario_input = input("Digite o usuário: ").strip().lower()
            senha_input = input("Digite a senha: ")
            for colaborador in colaboradores:
                if colaborador["usuario"] == usuario_input and colaborador["senha"] == senha_input:
                    print("Acesso concedido.")
                    pausa(2)
                    limpar_tela()
                    menu()
                    break
            else:
                print("Usuário ou senha incorretos.")
                pausa(2)
                limpar_tela()
        elif escolha == '3':
            print("Por favor, entre em contato com o administrador do sistema para recuperar sua senha.")
            pausa(2)
            limpar_tela()
        elif escolha.lower() == 's':
            print("Saindo do programa.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            pausa(2)
            limpar_tela()
            continue
            
                  
def menu():
    while True:
        print("\nMenu de Opções:")
        print("Escolha a opção desejada ou '9' para SAIR: ")
        print("\n1. Adicionar Item")
        print("2. Listar Itens")
        print("3. Mover Item para Lixeira")
        print("4. Ver Lixeira")
        print("5. Restaurar Item")
        print("6. Esvaziar Lixeira")
        print("7. Grafico de Itens no Estoque")
        print("8. Estoque Baixo Item")
        print("9. Voltar Menu anterior")
        print("S. Sair")
    
        escolha = input("\nOpção: ")
        if escolha == '1':           
            adicionar_item()                     
        elif escolha == '2':
            listar_itens()
        elif escolha == '3':
            lixeira_mover()
        elif escolha == '4':
            ver_lixeira()          
        elif escolha == '5':
            restaurar_item()                     
        elif escolha == '6':
            esvaziar_lixeira()
        elif escolha == '7':
            grafico_itens_estoque()
        elif escolha == '8':
            estoque_baixo()
        elif escolha == '9':
            limpar_tela()
            return               
        elif escolha.lower() == 's':
            print("Obrigado por usar o sistema de gerenciamento de cadastro.")
            print("\n")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            
#=========Execução do programa=========

if __name__ == "__main__":
    menu_inicial()
