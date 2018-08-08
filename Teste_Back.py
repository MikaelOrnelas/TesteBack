import pyodbc           #>Driver python para SQL
                                                                 
conexao = pyodbc.connect("Driver={SQL Server Native Client 11.0};"   #>Configuração p/ conexão
                        "Server=localhost;"                       #com o driver pyodbc
                        "Database=Trabalhos;"
                        "Trusted_Connection=yes;")
                                
mycursor = conexao.cursor()    #>Cursor para percorrer os objetos do banco
                                                                
#Insert
def insert():                                                  
    dados =[(1800, 123456789-00, 'clienteA', 1, 1970),          
            (1600, 987654321-11, 'clienteB', 1, 800),
            (1210, 456987123-22, 'clienteC', 1, 99),        #>Dados para inserção e
            (2000, 852369741-33, 'clienteD', 1, 170),       #cálculo
            (1111, 741369852-44, 'clienteE', 0, 565),
            (1755, 987654789-55, 'clienteF', 1, 30),
            (2470, 124236852-66, 'clienteG', 1, 774),
            (2800, 582528174-77, 'clienteH', 1, 119)
            ]

    valores = ', '.join(map(str,dados))                      #>Converte dados para string
    inserir = "insert into tb_customer_account(id_customer, cpf_cnpj, nm_customer, is_active, vl_total) values{}".format(valores)    #>Insere os dados 
    mycursor.execute(inserir)                                                                                                       #após convertidos
                                                            
#Select
def select():                                               
    print("Média do calculo \n")                            
    mycursor.execute("select avg(vl_total) from tb_customer_account where vl_total>='560' and id_customer between 1500 and 2700")   #>Condição para média

    for x in mycursor:      #>Percorre os objetos e 
        print(x, "\n")      #imprime a média

    print("Clientes que participaram do cálculo \n")
    mycursor.execute("select nm_customer from tb_customer_account where vl_total>='560' and id_customer between 1500 and 2700 order by vl_total desc") #>Condição para
                                                                                                                                                       #participar da pesquisa 
    for x in mycursor:      #>Percorre os objetos e
        print(x)            #imprime os clientes que participaram da pesquisa

if __name__ == '__main__':
    insert()
    select()
