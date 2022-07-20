def notas(* n,sit=False):
    """
        Função que calcula as notas, podendo mostrar a situação da média ou não
    :param n: Notas do alunos
    :param sit: (OPCIONAL). Indica se deve ou não adicionar a situação
    :return: Dicionário com diversas informações sobre a turma
    """
    dic= {}
    dic['Total']= len(n)
    dic['Maior']= max(n)
    dic['Menor']= min(n)
    dic['Média']= sum(n) / len(n)
    if sit == True:
        if dic['Média'] > 7:
            dic['Situação']= 'BOA'
        elif dic['Média'] > 4:
            dic['Situação']='RAZOÁVEL'
        else:
            dic['Situação']='Ruim'
    return dic

resp= notas(1.4,1,9,8, sit=True)
print(resp)