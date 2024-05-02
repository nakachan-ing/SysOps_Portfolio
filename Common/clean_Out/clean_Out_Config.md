# clean_Out.shの設定

## 設定内容
- シェル名: clean_Out.sh
- シェル説明: ディレクトリ内の与えられた期間を超えた処理対象を削除する

## 引数一覧
1. 処理ディレクトリ: 必須
2. 削除対象日数（数値）: 必須
3. 処理対象種別: 必須（「all」「dir」「file」のいずれか）

## Cron式
00 08 * * * root bash /path/to/clean_Out.sh /path/to/処理ディレクトリ "90" "all" 2>&1