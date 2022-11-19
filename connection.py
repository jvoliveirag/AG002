import mysql.connector
import pandas as pd

#Conexão com o Banco de Dados
conector = mysql.connector.connect(host='localhost', database='statlog',
                                    user='root',
                                    password='R!bero123')

if conector.is_connected():
    db_info = conector.get_server_info()
    print("Conectado ao servidor do MySQL na versao: ", db_info)

    try:
        cursor = conector.cursor()
        cursor.execute("""select database();""")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados", linha[0])
    finally:       
        #Leitura dos dados do banco
        dtFrame = pd.read_sql("SELECT * FROM germancredit", conector)
        pd.set_option('display.expand_frame_repr', False)
        cursor.close()
        conector.close()