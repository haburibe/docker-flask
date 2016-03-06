イメージを作成

```
$ docker build -t haburibe/flask .
```

コンテナを実行
コンテナの8080番ポートをホストの8080番ポートにつなげる

```
$ docker run -d -p 8080:8080 haburibe/flask
```
