'''
Alunos: João Victor de Oliveira Gomes Ribeiro - 106 GES
        Júlia da Silva Villela - 1799 GEC
'''

from training_measure import classifier
from inputs import X_input

def main():
    print("AG002 - Avaliacao de credito do usuario")
    
    #PREDICAO COM BASE NOS VALORES INSERIDOS
    if classifier.predict(X_input) == 1:
        print('\nRisco de credito ruim')
    if classifier.predict(X_input) == 0:
        print('\nRisco de credito bom')

if __name__ == "__main__":
    main()