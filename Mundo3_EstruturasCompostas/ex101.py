import datetime
ano= datetime.date.today().year
def voto(id):
    if id >= 18:
        return f'Com {id} anos: O voto é OBRIGATÓRIO!'
    elif 16 <= idade < 18 or id > 65:
        return f'Com {id} anos: O voto é OPCIONAL!'
    elif id < 18:
        return f'Com {id} anos: O voto é NEGADO!'


nascimento= int(input('ANO DE NASCIMENTO:'))
idade= ano - nascimento
print(voto(idade))