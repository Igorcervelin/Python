# -*- coding: utf-8 -*-

class Estado():   

    #Estado inicial
    def __init__(atual, mDir, mEsq, cDir, cEsq, lado):
        atual.lado = lado
        atual.no = None
        atual.possibilidades = []
        atual.mDir = mDir
        atual.mEsq = mEsq
        atual.cDir = cDir
        atual.cEsq = cEsq
 
    def validacao(atual):
        # Evitar negativos
        if ((atual.mDir < 0) 
            or (atual.cDir < 0)
            or (atual.mEsq < 0) 
            or (atual.cEsq < 0)):
            return False

        # Numero de missionarios nao pode ser menor que canibais
        if ((atual.mDir == 0 or atual.mDir >= atual.cDir)and
            (atual.mEsq == 0 or atual.mEsq >= atual.cEsq)):
            return True
       
    #Gera estados validos sem ser estado final
    def lista_possibilidades(atual):
        movimentacao = [[1,0],[1,1],[0,2],[2,0],[0,1]]
              
        # Gera os possíveis estados e armazena apenas os válidos no estado atual
        for mover in movimentacao:
            if atual.lado == 'esquerdo':

                mEsq = atual.mEsq - mover[0]
                mDir = atual.mDir + mover[0]
                cEsq = atual.cEsq - mover[1]
                cDir = atual.cDir + mover[1]

                #Criar possibilidades
                possibilidades = Estado(mDir, mEsq, cDir,cEsq, 'direita')
                
            else:

                mDir = atual.mDir - mover[0]
                mEsq = atual.mEsq + mover[0]
                cDir = atual.cDir - mover[1]
                cEsq = atual.cEsq + mover[1]
                
                possibilidades = Estado(mDir, mEsq, cDir,cEsq, 'esquerdo')

            #adiciona na lista de possibilidades
            possibilidades.no = atual

            #validar estado
            if possibilidades.validacao():
                atual.possibilidades.append(possibilidades)

        # Verifica se todos atravessaram o rio (3 e 3 / 0 e 0)
    def final(atual):
        if ((atual.mEsq and atual.cEsq) == 3 and 
           (atual.mDir and atual.cDir) == 0):
           return True
        else:
            return False


#Gera arvore de estados.
class Operacao():
    def __init__(atual):
    #insere raiz
        atual.selecionado = [Estado(3, 0, 3, 0, 'direita')]
        atual.solucao = None

    def concluir(atual):
        #Solucao em busca em largura
      
        for elemento in atual.selecionado:
            if elemento.final():
                # Se a solução foi encontrada, gera o caminho até a raiz da arvore e encerra
                atual.solucao = [elemento]
                while elemento.no:
                    atual.solucao.insert(0, elemento.no)
                    elemento = elemento.no
                break;
            #Se o elementoo nao solucionar, gera uma possibilidade
            elemento.lista_possibilidades()
            atual.selecionado.extend(elemento.possibilidades)


def main():
    problema = Operacao()
    problema.concluir()

    problema.solucao.reverse() 
    print('\t\t\t\t  Solucao:\n',50*'--')
    for estado in problema.solucao:
        print ('Missionarios:',estado.mEsq, '\t\t '  ,  'Missionarios:',estado.mDir,'\n'
            'Canibais:',estado.cEsq, '\t\t\t ' ,  'Canibais:',estado.cDir,'\n')

if __name__ == '__main__':
    main()