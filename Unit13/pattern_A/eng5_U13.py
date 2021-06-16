#英語ⅣB_Unit 13_単語テスト

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:56:34 2020

@author: Tomoki Ikegami
"""

from difflib import SequenceMatcher

# PYTHON_NUMPY_STRUCTURE_01-1

#シャッフル用

import random

#Ans:より後の答えを取り出す処理に使用
import re

#日時の取得
import datetime

#解答時間の記録
import time

#メールの送信に使用
import send_attach


### 使うテキストファイルによって変わるパラメータ ###

Test_title=" Unit 13 Quiz [pattern A] "
Title_per_unit="**** Unit 13-{0} Quiz ****"

TOTAL_UNIT=4 #総合問題も含めたユニット数

ques_template="eng5_words_U13-{0}_question.txt"                  #問題文を保存するファイル
ans_template="eng5_words_U13-{0}_answer.txt"                     #問題の解答を保存するファイル
wrong_template="eng5_words_U13-{0}_wrong_total.txt"              #間違えた問題数の累積を記録するファイル

result_file_name="eng5_words_U13_result.txt"                     #全てのテスト結果が保存されるファイル
current_result_file_name="eng5_words_U13_current_result.txt"     #問題を解いたそのときの結果
weak_file_name="eng5_words_U13_weak_point.txt"                   #☆の入ったテキストファイル

How_to_ask="Definitions → "
input_style="English word >>"

star='(;_;) '

## 各種関数

def get_separated(list_X,n):
    list_A=[]
    list_B=[]
    
    for i in range(n):    
        regdate_ques =list_X[i]
        pattern = "(.*):(.*)"
        d_ques = re.search(pattern, regdate_ques)
        list_A.append(d_ques.group(1))
        list_B.append(d_ques.group(2))
    
        
    return list_A,list_B



def simple_sort(list_A,list_B,n):
    
    list_C=[0]*n
    
    for i in range(n-1):
        
        #print("単純ソート")
        
        
        #左端をとりあえず最小値に
        mini=list_A[i]
        mini_2=list_B[i]
        
        #左からi番目をとりあえず最小値にしているので、その添え字を最小値としておく。
        index=i
        
        #添え字jを使って右に向かって最小値を探しに行く
        for j in range(i+1,n):
        
            #もし、j番目に最小値があれば
            if list_A[j]<mini:
                
            #最小値をj番目のものに更新する
                mini=list_A[j]
                mini_2=list_B[j]
            #最小値のあった場所(添え字j)に、添え字を更新する
                index=j
        
        ###リストの順番を入れ替える
        #i番目の要素を一時的に保存
        temp=list_A[i]
        temp_2=list_B[i]
        
        #見つけた最小値をi番目に置く
        list_A[i]=list_A[index]
        list_B[i]=list_B[index]
        
        
        #最小値のあった場所には、i番目の要素を入れておく。
        list_A[index]=temp
        list_B[index]=temp_2        
        
        #print('i=',i,'j=',j)
        #print(list_A)  
 
    for i in range(n):
        list_C[i]=str(list_A[i])+":"+str(list_B[i])
    
    return list_C

     
def simple_sort2(list_A,list_B,n):
    
    list_C=[0]*n
    
    for i in range(n-1):
        
        #print("単純ソート")
        
        
        #左端をとりあえず最小値に
        mini=list_A[i]
        mini_2=list_B[i]
        
        #左からi番目をとりあえず最小値にしているので、その添え字を最小値としておく。
        index=i
        
        #添え字jを使って右に向かって最小値を探しに行く
        for j in range(i+1,n):
        
            #もし、j番目に最小値があれば
            if list_A[j]<mini:
                
            #最小値をj番目のものに更新する
                mini=list_A[j]
                mini_2=list_B[j]
            #最小値のあった場所(添え字j)に、添え字を更新する
                index=j
        
        ###リストの順番を入れ替える
        #i番目の要素を一時的に保存
        temp=list_A[i]
        temp_2=list_B[i]
        
        #見つけた最小値をi番目に置く
        list_A[i]=list_A[index]
        list_B[i]=list_B[index]
        
        
        #最小値のあった場所には、i番目の要素を入れておく。
        list_A[index]=temp
        list_B[index]=temp_2        
        
        #print('i=',i,'j=',j)
        #print(list_A)  
      
    
    #star='(;_;) '
    
    for i in range(n):
        list_C[i]=list_B[i]+"  "+star*list_A[i]
    
    return list_C

    
   

def compile_wrong_data():
    
    #wrong_template="eng5_words_U13-{0}_wrong_total.txt"
    #template="eng5_words_U13-{0}_wrong_total.txt"
    
    file2=wrong_template.format(TOTAL_UNIT)
    
    
    fileobj2=open(file2, "a", encoding = "utf_8")
    
    
    for i in range(TOTAL_UNIT-1):
        file=wrong_template.format(i+1)
        fileobj = open(file, "r", encoding = "utf_8")
        
        #ファイルを文字列として読み込む
        wrong_n0=fileobj.read()
        #それぞれの行データをリストの一要素にする
        wrong_n=wrong_n0.splitlines()
        
        for j in range(len(wrong_n)):

            #全体の間違えた問題数の累計に書き込み
            fileobj2.write(wrong_n[j]+'\n')


    fileobj.close()
    fileobj2.close()


def make_result_now():
    
    f1=open(current_result_file_name,"r",encoding="utf-8_sig")
    
    #ファイル全体を文字列として読み込む
    result_now=f1.read()
    
    f1.close()
    
    return result_now



# 処理前の時刻
t1 = time.time() 
 
print("\n")
print(Test_title+"\n")

unit= input("学習する単元の数字を入力してください(1~{0},{1})".format(TOTAL_UNIT-1,TOTAL_UNIT)+">>")
test_mode=input("テストモードを使用しますか？(y/n)>>")
print("\n")


#問題文と解答のテキストファイルを読み込む     
f1=open(ques_template.format(unit),encoding="utf-8_sig")
f2=open(ans_template.format(unit),encoding="utf-8_sig")

fm=wrong_template.format(unit)
file=result_file_name
file_cr=current_result_file_name


fmr = open(fm, "r", encoding = "utf_8")

#問題文と解答を文字列として読み込む

question_0=f1.read()
answer_0=f2.read()


f3=open(ans_template.format(TOTAL_UNIT),encoding="utf-8_sig")
answer_for_show_0=f3.read()

#間違えた問題数記録も同時に読み込む
wrong_total_0=fmr.read()

#body_0=f3.read()

#間違えた問題数が保存されたファイルも同時に読み込む


#テスト結果保存用のファイルを開く
fileobj = open(file, "a", encoding = "utf_8")
fileobj_cr=open(file_cr, "w", encoding = "utf_8")

#問題文、答え、間違えた問題数累計を改行コードごとに分割

question=question_0.splitlines()
answer=answer_0.splitlines()
answer_for_show=answer_for_show_0.splitlines()

wrong_total=wrong_total_0.splitlines()

#body=body_0.splitlines()

#改行コード削除
#question[0]=question[0].strip()
#answer[0]=answer[0].stlip

#ファイルを閉じる
f1.close()
f2.close()
fmr.close()

#問題数をカウント
total=len(question)

    
# 解答結果
result=[0]*total

#間違えた解答を記憶する配列(リスト)
wrong_ans=[0]*total

#更新後の間違えたを記憶する配列(リスト)
new_wrong_total=[0]*total

#問題のタイトルを表示
print(Title_per_unit.format(unit)+"\n")
print("合計問題数",total)
print('\n')



# 現在のタイムスタンプを取得
now = datetime.datetime.now()



# シャッフル


p = list(zip(question,answer,wrong_total))
random.shuffle(p)
question, answer,wrong_total = zip(*p)


#2つのリストをまとめてfor文に渡す
for i,(key,value,w_value) in enumerate(zip(question,answer,wrong_total)):
    
    print("({0}問目)".format(i+1))
 
    #問題番号を削除して問題文のみを表示
    regdate_ques =key
    pattern = "(.*):(.*)"
    d_ques = re.search(pattern, regdate_ques)
    
    #間違えた問題の問題数のみを取りだす
    regdate_w_tot =w_value
    pattern = "(.*):(.*)"
    d_w_tot = re.search(pattern, regdate_w_tot)
    
    print(How_to_ask+d_ques.group(2))
    #print(key)
    a= input(input_style)
    
    
    #終了したいときの処理
    if a=='q':
        break
    
    #解答をコロン(：) で分割   
    regdate_ans =value
    pattern = "(.*):(.*)"
    d_ans = re.search(pattern, regdate_ans)
    
    
    
    #問題の種類を判定
    #ques_type:書き問題→True,選択問題→False
    #大文字のAが含まれると書き問題判定になるバグを改善
    ques_type=('_wr' in d_ans.group(1))

    #解答の比較
    
    r = SequenceMatcher(None, a,d_ans.group(2)).ratio()
    
    #メモ：if文のところを、ques_type==Trueのように記述するとif文が反応しなくなる
    #書き問題の時の処理
    
    if test_mode=='y':
    
        if ques_type:
        
            if 0.6<=r<=1.0:
                print('')
                new_wrong_total[i]=w_value
            else:
                print('')
                result[i]=1
                wrong_ans[i]=a
                
                #間違えた問題の累計問題数を1つ増やす
                wrong_num=int(d_w_tot.group(2))+1
                new_wrong_total[i]=d_w_tot.group(1)+':'+str(wrong_num)
                
      
    
        else:
            #T/F,選択式問題の処理
            if r==1.0:
                print("")
                new_wrong_total[i]=w_value
            else:
                print("")
                result[i]=1
                wrong_ans[i]=a
                
                #間違えた問題の累計問題数を1つ増やす
                wrong_num=int(d_w_tot.group(2))+1
                new_wrong_total[i]=d_w_tot.group(1)+':'+str(wrong_num)
                
    else:
        
        if ques_type:
        
            if 0.6<=r<=1.0:
                print("あなたの解答は正解です(一致率:{0}%)".format(r*100))
                new_wrong_total[i]=w_value
            else:
                print("不正解...正しい答えは「{0}」です。(一致率:{1}%)" .format(d_ans.group(2),r*100))
                result[i]=1
                wrong_ans[i]=a

                #間違えた問題の累計問題数を1つ増やす
                wrong_num=int(d_w_tot.group(2))+1
                new_wrong_total[i]=d_w_tot.group(1)+':'+str(wrong_num)      
    
        else:
            #T/F,選択式問題の処理
            if r==1.0:
                print("あなたの答えは正解です")
                new_wrong_total[i]=w_value
            else:
                print("不正解...正しい答えは「{0}」です" .format(d_ans.group(2)))
                result[i]=1
                wrong_ans[i]=a

                #間違えた問題の累計問題数を1つ増やす
                wrong_num=int(d_w_tot.group(2))+1
                new_wrong_total[i]=d_w_tot.group(1)+':'+str(wrong_num)
   
    print('\n')
    


#間違えた問題数を数える
wrong=result.count(1)

# 現在のタイムスタンプをそのまま出力
print("日時：{0}".format(now),file=fileobj)
print("日時：{0}".format(now),file=fileobj_cr)

# 処理後の時刻
t2 = time.time()
 
# 経過時間を計算
elapsed_time = t2-t1
total_time=elapsed_time/60

#f文字列は、formatと同じようなもの
print(f"解答時間：{total_time:.1f}分\n",file=fileobj)
print(f"解答時間：{total_time:.1f}分\n",file=fileobj_cr)

#print(now,file=fileobj)
#print("\n",file=fileobj)

#間違えた問題数更新のためにファイルを上書き
fmw = open(fm, "w", encoding = "utf_8")

list_A0,list_B0=get_separated(new_wrong_total,total)


#累計問題数の順番がバラバラなので、昇順に並べる

#問題番号と間違えた問題の累計を、文字列から数値に変換
list_Ai=[int(s) for s in list_A0]
list_Bi=[int(s) for s in list_B0]

#問題番号を基準に並べ替え(昇順)
final_wrong_total=simple_sort(list_Ai,list_Bi,total)


print("☆☆☆ 問題文と模範解答　☆☆☆")
print("\n")



for count,(item1,item2,item3) in enumerate(zip(question,answer,final_wrong_total)):
    
    print("問題文: "+ item1)
    print("正しい回答 :"+item2+"\n")
    fmw.write(item3+'\n')
    
    
    #表示するとエラーになる↓
    #print("あなたの答え:"+item3)
    #print("\n")

print("\n")

if a!='q':
    print("*****　テスト結果　*****\n")
    print('{0}問中 {1}問正解'.format(total,total-wrong))
    print(f"解答時間：{total_time:.1f}分\n")
    print("\n")
    print("×××××　間違えた問題　×××××")
    print("\n")
    
    #外部ファイルにも同じ内容を保存
    
    fileobj.write(" 単元番号：{0} \n".format(unit))
    fileobj.write("*****　テスト結果　*****\n")
    fileobj.write('{0}問中 {1}問正解'.format(total,total-wrong))
    fileobj.write("\n\n")
    fileobj.write("×××××　間違えた問題　×××××")


    fileobj_cr.write(" 単元番号：{0} \n".format(unit))
    fileobj_cr.write("*****　テスト結果　*****\n")
    fileobj_cr.write('{0}問中 {1}問正解'.format(total,total-wrong))
    fileobj_cr.write("\n\n")
    fileobj_cr.write("×××××　間違えた問題　×××××")  
    
    
    for count,(item1,item2,item3) in enumerate(zip(question,answer,wrong_ans)):
        if result[count]==1:
            #print("該当する本文は → "+item0)
            print("問題文は "+ item1) 
            print("正しい回答は "+item2+", あなたの答えは　"+item3+"\n")
            
            #外部ファイルにも同じ内容を保存
            fileobj.write("\n")
            #fileobj.write("該当する本文 → "+item0+"\n")
            fileobj.write("問題文は "+ item1+"\n") 
            fileobj.write("正しい回答は "+item2+", あなたの答えは　"+item3+"\n")

            fileobj_cr.write("\n")
            #fileobj.write("該当する本文 → "+item0+"\n")
            fileobj_cr.write("問題文は "+ item1+"\n") 
            fileobj_cr.write("正しい回答は "+item2+", あなたの答えは　"+item3+"\n")


     
    print("\n")
    print('↑↑↑ 全問題の解答を見る場合は、「テスト結果」 より上に移動　↑↑↑')
        
    
else:
    print("\n")
    print("テスト結果は表示できません")


print("\n\n",file=fileobj)

##それぞれの単元の間違えた問題数累計を全体に反映

#間違えた問題の記録も閉じる
fmw.close()


if fm!=wrong_template.format(TOTAL_UNIT):
    #元のファイルを削除

    file2=wrong_template.format(TOTAL_UNIT)
    fileobj2=open(file2, "w", encoding = "utf_8")
    fileobj2.close()

    compile_wrong_data()

##テスト結果保存用のファイルを閉じる    
fileobj.close()
fileobj_cr.close()

###ファイル間違えた問題数を視覚的に見れるようにする
#テスト結果保存用のファイルを開く
# fileobj_show = open('eng5_words_U13-5_wrong_total.txt', "r", encoding = "utf_8")

# #問題数の累計ファイル（全体の）を開く
# show_wrong_0=fileobj_show.read()

# #行ごとにファイルを読み込み
# show_wrong=show_wrong_0.splitlines()

# all_ques_total=len(show_wrong)
# list_SL,list_SR=get_separated(show_wrong,all_ques_total)

# list_SR_i=[int(s) for s in list_SR]

# visualize_weak=simple_sort2(list_SR_i,answer_for_show,all_ques_total)

# print("\n\n")

# print("あなたの間違えやすい単語です")

# for i in visualize_weak:
#     print(i)
    

#fileobj_show.close()



##ファイル間違えた問題数を視覚的に見れるようにする
#テスト結果保存用のファイルを開く
fileobj_show = open(wrong_template.format(TOTAL_UNIT), "r", encoding = "utf_8")

#問題数の累計ファイル（全体の）を開く
show_wrong_0=fileobj_show.read()


fileobj_show.close()


#行ごとにファイルを読み込み
show_wrong=show_wrong_0.splitlines()

all_ques_total=len(show_wrong)

list_SL,list_SR=get_separated(show_wrong,all_ques_total)
list_SR_i=[int(s) for s in list_SR]


fw1=open(weak_file_name,'w',encoding="utf-8")

# print("\n\n")
# print("あなたの間違えやすい単語です (☆の数は間違えた回数を示しています)")



# for i in range(all_ques_total):
#     star='☆'
#     print(answer_for_show[i]+"  "+star*list_SR_i[i])


for i in range(all_ques_total):
    #star='(;_;) '
    print(answer_for_show[i]+"  "+star*list_SR_i[i],file=fw1)


fw1.close()

print("\n\n")
print("間違えている問題の状況を、メールに送信しますか?(y/n)")
b=input(">>")

if b=="y":
    #メールを送信
    result_body=make_result_now()
    send_attach.send_mail(weak_file_name,result_body,Test_title)
