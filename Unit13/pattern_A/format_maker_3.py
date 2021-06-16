#問題や解答の入力用テンプレートを作成するプログラム

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:33:15 2020

@author: Tomoki Ikegami
"""

#Ans:より後の答えを取り出す処理に使用
import re

#問題、解答の入力用テンプレート作成関数
def question_format(total,file_type,file_name):
    #ファイルを作成
    fileobj = open(file_name, "w", encoding = "utf_8")
    counter=1
    while counter < int(total)+1:
        
        print(file_type+str(counter)+":",file=fileobj)
        counter += 1

    #ファイルを閉じる    
    fileobj.close()


def insert_format(file_type,file_name,not_converted):
    #出力ファイルを作成
    fileobj = open(file_name, "w", encoding = "utf_8")
    #counter=1
    #2つのリストをまとめてfor文に渡す
    for i,original in enumerate(not_converted):
        #:が含まれていないとき、条件文はTrueになる。
        condition=(':' not in original)
        if condition:
            
            #new=file_type+str(i+1)+':'+original
            print('{0}{1}:{2}'.format(file_type,i+1,original),file=fileobj)
            #counter += 1
        else:
            print('{0}'.format(original),file=fileobj)
            print('{0}{1} == 番号挿入済 =='.format(file_type,i+1))
            
    print("\n")
    #ファイルを閉じる    
    fileobj.close()



def delete_format(file_name,inserted):
    #出力ファイルを作成
    fileobj = open(file_name, "w", encoding = "utf_8")
    #counter=1
    #2つのリストをまとめてfor文に渡す
    for i,original in enumerate(inserted):

    
        #print("Definitions → "+d_ques.group(2))
        condition=(':' in original)
        if condition:
        #:が含まれていないとき、条件文はTrueになる。
            #問題番号を削除して問題文のみを表示
            regdate_ques =original
            pattern = "(.*):(.*)"
            d_ques = re.search(pattern, regdate_ques)
            #new=file_type+str(i+1)+':'+original
            print('{0}'.format(d_ques.group(2)),file=fileobj)
            #counter += 1
        else:
            print('{0}'.format(original),file=fileobj)
            print('{0} == 番号削除済 =='.format(i+1))
            
    print("\n")
    #ファイルを閉じる    
    fileobj.close()

def initiaize_format(total,file_type,file_name,init):
    #ファイルを作成
    fileobj = open(file_name, "w", encoding = "utf_8")
    counter=1
    while counter < int(total)+1:
        
        print(file_type+str(counter)+":"+init,file=fileobj)
        counter += 1

    #ファイルを閉じる    
    fileobj.close()


#メインとなる処理部分（始点） =========================================================================================

print("\n==== 問題、解答のテキストファイルの入力テンプレートを作成します ====\n\n")

while True:
    print('q:作業終了')
    a=input("ファイルの新規作成:n 既存のファイルに番号を挿入:i 挿入済みの番号を削除：d 特定の文字で初期化してファイルを新規作成:ni >>")
    print("\n")
    
    if a=='q':
        break
    
    
    if a=='n':
        print("ファイル名を入力してください")
        file_name=input("ファイル名(拡張子も含めて)>>")
        print("\n")
        
        print("種類を入力してください：本文>>B  問題>>Q  解答>>A")
        file_type=input("ファイルの種類>>")
        print("\n")
        
        print("問題数を入力してください")
        total=input("問題数>>")
        print("\n")
        
        question_format(total,file_type,file_name)
        
        print("+++++++++++++++++++++")
        print(file_name+" が作成されました"+"\n")
        
    elif a=='i':
    
        print("ファイル名を入力してください")
        file_name=input("ファイル名(拡張子も含めて)>>")
        f1=open(file_name,encoding="utf-8_sig")
        print("\n")
    
    
        print("種類を入力してください：本文>>B  問題>>Q  解答>>A")
        file_type=input("ファイルの種類>>")
    
        #ファイル読み込み
        not_converted_0=f1.read()
        #改行コードで区切る
        not_converted=not_converted_0.splitlines()
    
        #ファイルを閉じる
        f1.close()
    
        print("\n")
    
        insert_format(file_type,file_name,not_converted)
    
        
        print("======================")
        print(file_name+" に番号が挿入されました "+"\n")

    elif a=='d':
        
        print("ファイル名を入力してください")
        file_name=input("ファイル名(拡張子も含めて)>>")    
        print("\n")
        f1=open(file_name,encoding="utf-8_sig")
        
    
        '''
        print("種類を入力してください：本文>>B  問題>>Q  解答>>A")
        file_type=input("ファイルの種類>>")
        '''
    
        #ファイル読み込み
        inserted_0=f1.read()
        #改行コードで区切る
        inserted=inserted_0.splitlines()
    
        #ファイルを閉じる
        f1.close()
    
        delete_format(file_name,inserted)
    
        
        print("======================")
        print(file_name+" の番号が削除されました "+"\n") 
        
    else:
        print("ファイル名を入力してください")
        file_name=input("ファイル名(拡張子も含めて)>>")
        print("\n")
        
        print("種類を入力してください： 問題ごとのミス数>>W ")
        file_type=input("ファイルの種類>>")
        print("\n")
        
        print("初期化する文字または、数字を入力してください: 例)0 ")
        init=input("初期化文字または数字>>")
        
        print("問題数を入力してください")
        total=input("問題数>>")
        print("\n")
        
        
        
        initiaize_format(total,file_type,file_name,init)
        
        print("+++++++++++++++++++++")
        print(file_name+" が作成されました"+"\n")        

    print("\n")


#メインとなる処理部分（終点） =========================================================================================

