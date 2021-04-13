# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:45:55 2020

"""
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
import os

def send_mail(weak_file_name,result_body,Test_title):

    # 以下にGmailの設定を書き込む★ --- (*1)
    gmail_account = "????@gmail.com"
    gmail_password = "半角英数字でパスワード"
    # メールの送信先 --- (*2)
    mail_to = "送信先メールアドレス"
    
    #現在のフォルダの場所を取得
    cwd = os.getcwd()
    
    #分析結果の円グラフの画像のパスを取得
    image_file_path=os.path.join(cwd,weak_file_name)
    
    # 添付ファイルのパス(jpgファイルで指定) --- (*3)
    file_path=image_file_path
    
    username=os.getlogin()
    
    # メールデータ(MIME)の作成 --- (*4)
    subject = "間違えている単語の状況"
    body = username+"さんへ\n\n"+"こんにちは\n"+"現在の間違えている問題の状況をお知らせします\n"+"添付ファイルを開いてご確認ください。\n\n 今回のテスト結果もお知らせします。\n\n ＜テスト結果と間違えた問題＞\n"+result_body
    encoding = 'utf-8'
    msg = MIMEMultipart()
    msg["Subject"] = Header(subject, encoding)
    msg["To"] = mail_to
    msg["From"] = gmail_account
    msg.attach(MIMEText(body, 'plain', encoding))
    
    # 添付ファイル(ZIP)をメールに追加 --- (*5)
    attach = MIMEBase('application','txt')
    with open(file_path, "br") as f:
        attach.set_payload(f.read())
    encoders.encode_base64(attach)
    attach.add_header('Content-Disposition', 'attachment',
        filename=weak_file_name)
    msg.attach(attach)
    
    # Gmailに接続 --- (*6)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
        context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg) # メールの送信
    server.quit()
    print("\n →→→→→→→　メールが送信されました →→→→→→→→")
    print("メールの受信トレイをご確認ください")
