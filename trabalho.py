def is_leap_year(year):
    """
    Função para determinar se um ano é bissexto ou não.

    Argumentos:
    year: int - O ano a ser verificado.

    Retorna:
    bool - True se o ano for bissexto, False caso contrário.
    """
    # Um ano é bissexto se for divisível por 4
    # Exceto quando também for divisível por 100
    # A menos que seja divisível por 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    # Solicitar ao usuário que insira o ano desejado
    year = int(input("Digite o ano que deseja verificar: "))

    # Verificar se o ano é bissexto
    if is_leap_year(year):
        print(f"O ano {year} é bissexto e possui 366 dias.")
        print("Isso ocorre porque ele é divisível por 4, mas não por 100, ou é divisível por 400.")
    else:
        print(f"O ano {year} não é bissexto e possui 365 dias.")
        print("Isso ocorre porque ele não atende às condições para ser bissexto.")

if __name__ == "__main__":
    main()