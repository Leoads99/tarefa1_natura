# -*- coding: utf-8 -*-

import os, shutil


class Diretorio:
    # atributos
    def __init__(self, nome_dir, endereco_dir):
        self.nome_dir = nome_dir
        self.endereco_dir = endereco_dir
        
    
    # Métodos
    def cria_dir(self,nome_dir):
        dir = os.mkdir(nome_dir)
        return dir

    
    def criar_arquivo(self,nome_arquivo, metodo):
        arquivo = open(nome_arquivo, metodo)
        arquivo.writelines('Só sei que nada sei ')
        return arquivo

    def copiar_arquivo(self,dir_origem, dir_destino):
        copia = shutil.copy2(dir_origem, dir_destino)
        return copia


   # def dir_atual(self):
   #     print(f'O diretório atual é: {os.getcwd()}')
       

    def mudar_dir(self,endereco_dir):
        return os.chdir(endereco_dir)


    def renomeia(self, nome_antigo, novo_nome):
        new = os.rename(nome_antigo, novo_nome)
        return new


    def mover(self, nome_arquivo, dir_destino):
        return shutil.move(nome_arquivo, dir_destino)


endereco = "/home/kira/"
nome = 'pasta'
dir = Diretorio(nome, endereco)
dir.cria_dir('natura')
dir.cria_dir('avon')
endereco = "/home/kira/Documentos/natura"  

cont = 00
for cont in range(101):
    dir.mudar_dir(endereco)
    dir.criar_arquivo(f"natura_{cont}.txt","a")
    dir.mudar_dir("/home/kira/Documentos/avon")
    dir.copiar_arquivo(f"/home/kira/Documentos/natura/natura_{cont}.txt", f"/home/kira/Documentos/avon/avon_{cont}.txt")
    cont +=0.1
else:
    print('Tarefa finaliza')
