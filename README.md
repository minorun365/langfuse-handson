# langfuse-handson

Amazon Bedrock を呼び出す Python のコードに Langfuse を組み込み、トレース、プロンプト管理、評価、データセットを順に試すハンズオン用のコードです。番号順に、前のファイルへ数行ずつ追加していく構成です。

| ファイル | 内容 |
|---|---|
| 1_bedrock.py | Bedrock を呼び出すだけの出発点 |
| 2_trace.py | トレースを記録する |
| 3_prompt.py | プロンプトを取得する |
| 4_eval.py | 評価を行う |
| 5_dataset.py | データセットを登録する |

## 動かし方

Langfuse のキーを環境変数 LANGFUSE_PUBLIC_KEY、LANGFUSE_SECRET_KEY、LANGFUSE_HOST に設定してから、番号順に実行します。コードは Langfuse の Python SDK v2 向けの書き方です。AWS の認証には sandbox というプロファイルを使う前提なので、手元のプロファイル名に合わせて書き換えてください。

```bash
pip install boto3 "langfuse<3"
python 1_bedrock.py
```

## ライセンス

MIT License です。詳細は [LICENSE](./LICENSE) を参照してください。
