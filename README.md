# restAPI　for works
NECOの新人課題でRestAPIを使い課題を管理するRestAPIをまだ誰も使ってなかったPython+Djangoで実装しました。データベースはSQLiteを使ってます。


# 使い方
```bash
python manage.py runserver
```
ってやると仮想サーバーが起動するので、そのうえで
http://127.0.0.1:8000/api/v1/Works
をたたくとアクセスできます。
WorksにてWorksnameとTimelimitで構成されてます。各データにアクセスするときはhttp://127.0.0.1:8000/api/v1/Works/[id] でアクセスできます
もし上記URL以外のツールでアクセスした場合、TimelimitのほうはDateFieldで実装しましたので20XX/XX/XXの形で入力してください。(未検証)
あとは任意の方法で煮るなり焼くなりGETするなりDELETEするなりしてください。

Githubを始め、Web系全く触ってなくて何もわからなかったので許してほしいです。

つっきぃ(tsukky)