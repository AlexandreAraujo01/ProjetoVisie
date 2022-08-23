from re import L
import pymysql
import bson.json_util as json_util
import json

class DbVisie:
    def __init__(self):
        self.conection = pymysql.connect(host="jobs.visie.com.br", database='alexandreroberto', user='alexandreroberto', password='YWxleGFuZHJl')
        self.db = self.conection.cursor()
    
    
    def get_all_people(self):
        "pega todas as linhas do banco."
        query = "SELECT nome,data_admissao FROM `pessoas`;"
        self.db.execute(query)
        res = self.db.fetchall()
        return json.dumps(res,default=str)

    def specific_search(self,key,value):
        "pesquisa com filtra baseado em um campo"
        query = f'SELECT nome,data_admissao FROM `pessoas` WHERE `{key}` = "{value}"'
        self.db.execute(query)
        res = self.db.fetchone()
        return res
    
    def update_people(self,column,value,id):
        "atualiza uma linha baseado numa coluna escolhida"
        query = f'UPDATE `pessoas` set {column} = "{value}" where id_pessoa = {id}'
        print(query)
        self.db.execute(query)
        res = self.db.fetchone()
        self.conection.commit()
        return res
    
    def insert_people(self,obj):
        "insere uma nova linha na banco"
        lst = []
        lst.extend(obj.values())
        if len(lst) == 5:
            self.db.execute(f'INSERT INTO `pessoas` (nome,rg,cpf,data_nascimento,data_admissao) values {lst[0],lst[1],lst[2],lst[3],lst[4]}')
        self.conection.commit()

    def delete_people(self,id_people):
        query = f'DELETE FROM `pessoas` WHERE `id_pessoa` = {id_people}'
        print(query)
        self.db.execute("DELETE FROM `pessoas` WHERE `pessoas`.`id_pessoa` = 19")
        self.conection.commit()

        



if __name__ == "__main__":
    x = DbVisie()
    #x.get_all_people()
    # x.specific_search("nome","Alexandre Teixeira")
    #x.update_people("nome","Alexandre Araujo",2)
    # x.specific_search("nome","teste")
    # x.insert_people({"nome": "teste","rg": "54.398.006-1","cpf":"491.005.359.39","data_nascimento":"2000-07-05","data_admissão": "2022-08-23"})
    #x.delete_people(19)
    # nome,rg,cpf,data_nascimento,data_admissao