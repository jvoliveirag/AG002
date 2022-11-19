from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import hamming_loss
from connection import dtFrame


#Tratamento dos dados vindos do banco
cols = ['laufkont','laufzeit','moral','verw','hoehe','sparkont','beszeit','rate','famges','buerge',
        'wohnzeit','verm','alter','weitkred','wohn','bishkred','beruf','pers', 'telef','gastarb', 'kredit']
X = dtFrame.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]].values
y = dtFrame.iloc[:, [21]].values


#Separação da porcentagem de dados para teste e treinamento da rede
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)


#Classificação através da Árvore de Decisão
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

print('\n---------------------------------------[INICIO DAS METRICAS]--------------------------------------')
#Medindo a acurácia do modelo com base nas métricas de avaliação
y_predict = classifier.predict(X_test)
print('\nAcuracy:', metrics.accuracy_score(y_test, y_predict)*100,'%') #mostra a porcentagem de acerto
print('Acuracy:', metrics.accuracy_score(y_test, y_predict, normalize=False),'\n') #mostra quantas acertou

print(classification_report(y_test, y_predict)) #mostra as metricas principais da classificacao

concordancia = cohen_kappa_score(y_test, y_predict) 
print('Coeficiente Kappa de Cohen (Concordancia):', concordancia)
if(concordancia >= 0 and concordancia <= 0.2):
    print('Concordancia minima')
if(concordancia >= 0.21 and concordancia <= 0.4):
    print('Concordancia razoavel')
if(concordancia >= 0.41 and concordancia <= 0.6):
    print('Concordancia moderada')
if(concordancia >= 0.61 and concordancia <= 0.8):
    print('Concordancia substancial')
if(concordancia >= 0.81 and concordancia <= 1):
    print('Concordancia perfeita')

print('\nPercentual de Labels previstas incorretamente:', hamming_loss(y_test, y_predict)*100,'%')

print('\nMedia Harmonica Ponderada entre precisao e recall:', metrics.fbeta_score(y_test, y_predict, beta=0.5))
#valor ideal em 1 e seu pior valor em 0

print('\n---------------------------------------[FIM DAS METRICAS]--------------------------------------')