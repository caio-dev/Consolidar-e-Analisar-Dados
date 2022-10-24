import analises

print('Informe a opção que deseja visualizar digitando o número da opção:')
print('Informações básicas sobre a base')
print('2 - Faturamento por Ano')
print('3 - Faturamento por Produto')
print('4 - Faturamento por Região')

opcao = int(input())

if opcao == 1:
    analises.info_base()
elif opcao == 2:
    analises.valor_por_ano()
elif opcao == 3:
    analises.valor_por_produto()
elif opcao == 4:
    analises.valor_por_regiao()
else:
    print('Opção Inválida!')

