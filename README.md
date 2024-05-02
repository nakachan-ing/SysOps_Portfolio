# SysOps Portfolio

## 概要

このリポジトリは、SysOps（システム運用）に関連するスクリプトやドキュメントを管理するためのポートフォリオです。AWS、Azure、その他クラウドプラットフォームに関連するスクリプトや設定ファイル、テストドキュメントなどが含まれています。

## ディレクトリ構成
```
└── SysOps_Portfolio
├── AWS-SysOps-Portfolio
│ └── Lambda_Functions
│ ├── EC2-Alarm-Status-Monitor
│ │ ├── EC2-Alarm-Status-Monitor_Code
│ │ │ └── index.py
│ │ └── EC2-Alarm-Status-Monitor_Config.md
│ ├── EC2-Auto-Start-Stop
│ │ ├── EC2-Auto-Start-Stop_Code
│ │ │ └── index.py
│ │ ├── EC2-Auto-Start-Stop_Config.md
│ │ ├── EC2-Auto-Start-Stop_Testing.md
│ │ └── EC2-Auto-Start-Stop_Usage.md
│ └── EC2-Proc-Reboot
│ ├── EC2-Proc-Reboot_Code
│ │ └── index.py
│ ├── EC2-Proc-Reboot_Config.md
│ ├── EC2-Proc-Reboot_Testing.md
│ ├── EC2-Proc-Reboot_Usage.md
│ └── ProcChk.sh
└── Common
├── clean_Out.sh
└── file_Archive.sh
```

## ディレクトリ構成の説明

- **AWS-SysOps-Portfolio**: AWS関連のスクリプトや設定ファイルが含まれています。Lambda関数やEC2関連のスクリプトがあります。
  - **Lambda_Functions**: Lambda関数のコードや設定ファイルが含まれています。
    - **EC2-Alarm-Status-Monitor**: EC2のアラーム状態を監視するLambda関数のコードや設定が含まれています。
      - **EC2-Alarm-Status-Monitor_Code**: EC2アラーム監視のためのPythonコードがここにあります。
      - **EC2-Alarm-Status-Monitor_Config.md**: EC2アラーム監視Lambda関数の設定に関するドキュメントです。
    - 他のLambda関数のディレクトリも同様に構成されています。
  - 他のAWS関連スクリプトや設定ファイルも同様の階層構造で管理されています。

- **Common**: 共通のスクリプトやツールが含まれています。
  - **clean_Out.sh**: ディスク容量を確保するためのディレクトリクリーンアップスクリプトです。
  - **file_Archive.sh**: ファイルをアーカイブするためのスクリプトです。

## 更新履歴

- 2024-05-02: 初版リリース
