# SysOps Portfolio

## 概要

このリポジトリは、SysOps（システム運用）に関連するスクリプトやドキュメントを管理するためのポートフォリオです。AWS、Azure、その他クラウドプラットフォームに関連するスクリプトや設定ファイル、テストドキュメントなどが含まれています。

## ディレクトリ構成
```
.
├── AWS-SysOps-Portfolio
│   └── Lambda_Functions
│       ├── Alarm-Mail
│       │   ├── Alarm-Mail_Code
│       │   │   └── index.py
│       │   ├── Alarm-Mail_Config.md
│       │   ├── Alarm-Mail_Testing.md
│       │   └── Alarm-Mail_Usage.md
│       ├── EC2-Alarm-Status-Monitor
│       │   ├── EC2-Alarm-Status-Monitor_Code
│       │   │   └── index.py
│       │   └── EC2-Alarm-Status-Monitor_Config.md
│       ├── EC2-Auto-Start-Stop
│       │   ├── EC2-Auto-Start-Stop_Code
│       │   │   └── index.py
│       │   ├── EC2-Auto-Start-Stop_Config.md
│       │   ├── EC2-Auto-Start-Stop_Testing.md
│       │   └── EC2-Auto-Start-Stop_Usage.md
│       └── EC2-Proc-Reboot
│           ├── EC2-Proc-Reboot_Code
│           │   └── index.py
│           ├── EC2-Proc-Reboot_Config.md
│           ├── EC2-Proc-Reboot_Testing.md
│           ├── EC2-Proc-Reboot_Usage.md
│           └── ProcChk.sh
├── Common
│   ├── clean_Out
│   │   ├── clean_Out.sh
│   │   ├── clean_Out_Config.md
│   │   ├── clean_Out_Testing.md
│   │   └── clean_Out_Usage.md
│   └── file_Archive
│       ├── file_Archive.sh
│       ├── file_Archive_Config.md
│       ├── file_Archive_Testing.md
│       └── file_Archive_Usage.md
└── README.md
```

## ディレクトリ構成の説明

- **AWS-SysOps-Portfolio**: AWS関連のスクリプトや設定ファイルが含まれています。Lambda関数やEC2関連のスクリプトがあります。
  - **Lambda_Functions**: Lambda関数のコードや設定ファイルが含まれています。
    1. **Alarm-Mail**
        - コード: [Alarm-Mail_Code/index.py](AWS-SysOps-Portfolio/Lambda_Functions/Alarm-Mail/Alarm-Mail_Code/index.py)
        - 設定: [Alarm-Mail_Config.md](AWS-SysOps-Portfolio/Lambda_Functions/Alarm-Mail/Alarm-Mail_Config.md)
        - テスト: [Alarm-Mail_Testing.md](AWS-SysOps-Portfolio/Lambda_Functions/Alarm-Mail/Alarm-Mail_Testing.md)
        - 使用法: [Alarm-Mail_Usage.md](AWS-SysOps-Portfolio/Lambda_Functions/Alarm-Mail/Alarm-Mail_Usage.md)

    2. **EC2-Alarm-Status-Monitor**
        - コード: [EC2-Alarm-Status-Monitor_Code/index.py](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Alarm-Status-Monitor/EC2-Alarm-Status-Monitor_Code/index.py)
        - 設定: [EC2-Alarm-Status-Monitor_Config.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Alarm-Status-Monitor/EC2-Alarm-Status-Monitor_Config.md)

    3. **EC2-Auto-Start-Stop**
        - コード: [EC2-Auto-Start-Stop_Code/index.py](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Auto-Start-Stop/EC2-Auto-Start-Stop_Code/index.py)
        - 設定: [EC2-Auto-Start-Stop_Config.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Auto-Start-Stop/EC2-Auto-Start-Stop_Config.md)
        - テスト: [EC2-Auto-Start-Stop_Testing.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Auto-Start-Stop/EC2-Auto-Start-Stop_Testing.md)
        - 使用法: [EC2-Auto-Start-Stop_Usage.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Auto-Start-Stop/EC2-Auto-Start-Stop_Usage.md)

    4. **EC2-Proc-Reboot**
        - コード: [EC2-Proc-Reboot_Code/index.py](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Proc-Reboot/EC2-Proc-Reboot_Code/index.py)
        - 設定: [EC2-Proc-Reboot_Config.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Proc-Reboot/EC2-Proc-Reboot_Config.md)
        - テスト: [EC2-Proc-Reboot_Testing.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Proc-Reboot/EC2-Proc-Reboot_Testing.md)
        - 使用法: [EC2-Proc-Reboot_Usage.md](AWS-SysOps-Portfolio/Lambda_Functions/EC2-Proc-Reboot/EC2-Proc-Reboot_Usage.md)

- **Common**: 共通のスクリプトやツールが含まれています。
    1. **clean_Out**
        - スクリプト: [clean_Out.sh](Common/clean_Out/clean_Out.sh)
        - 設定: [clean_Out_Config.md](Common/clean_Out/clean_Out_Config.md)
        - テスト: [clean_Out_Testing.md](Common/clean_Out/clean_Out_Testing.md)
        - 使用法: [clean_Out_Usage.md](Common/clean_Out/clean_Out_Usage.md)

    2. **file_Archive**
        - スクリプト: [file_Archive.sh](Common/file_Archive/file_Archive.sh)
        - 設定: [file_Archive_Config.md](Common/file_Archive/file_Archive_Config.md)
        - テスト: [file_Archive_Testing.md](Common/file_Archive/file_Archive_Testing.md)
        - 使用法: [file_Archive_Usage.md](Common/file_Archive/file_Archive_Usage.md)

## 更新履歴

- 2024-05-02: 初版リリース
- 2024-05-09: 第二版リリース
