import json

ARQUIVOS_CADASTRADOS = "cadastros.json  "

def exibir_menu():
    print ("\n======== MENU CADASTRO ========")
    print ("1. Cadastrar pessoa")
    print ("2. Ver cadastros")
    print ("3. Sair")
    print ("==================================")
    
def salvar_cadastros (cadastros):
    with open (ARQUIVOS_CADASTRADOS, "w", encoding="utf-8") as arquivo:
        json.dump (cadastros, arquivo, indent=4, ensure_ascii=False)
        
def carregar_cadastros ():
    try:
        with open(ARQUIVOS_CADASTRADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def cadastrar_pessoas (cadastros):
    nome = input("nome: ")
    idade = input("idade: ")
    turma = input("turma: ")        
    curso = input("curso: ")

    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma,
"Curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro Realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("\nNenhum cadastro realizado.")
    else:
        print("\n===== Lista de Cadastros =====")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. Nome: {pessoa ['nome']}, Idade: {pessoa['idade']}, Turma: {pessoa['turma']}, Curso: {pessoa['curso']}")
            input("\nPressione enter para voltar ao menu...")