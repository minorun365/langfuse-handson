# langfuse-handson

Amazon Bedrock を呼ぶ Python のコードに Langfuse を足して、トレース・プロンプト管理・評価・データセットを順に試すハンズオン用のコードです。番号の順に、前のファイルへ数行ずつ足していく形になっています。

| ファイル | 内容 |
|---|---|
| 1_bedrock.py | Bedrock を呼ぶだけの出発点 |
| 2_trace.py | トレースを記録する |
| 3_prompt.py | プロンプトを取得する |
| 4_eval.py | 評価を行う |
| 5_dataset.py | データセットを登録する |

## 動かし方

Langfuse のキーを環境変数（LANGFUSE_PUBLIC_KEY・LANGFUSE_SECRET_KEY・LANGFUSE_HOST）に入れてから、番号の順に実行します。コードは Langfuse の Python SDK v2 の書き方です。AWS の認証は sandbox という名前のプロファイルを使う前提なので、手元のプロファイル名に合わせて書き換えてください。

```bash
pip install boto3 "langfuse<3"
python 1_bedrock.py
```

## ライセンス

MIT Licenseです。詳細は [LICENSE](./LICENSE) を参照してください。
