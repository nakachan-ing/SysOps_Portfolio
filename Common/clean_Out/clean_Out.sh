#!/bin/bash
umask 007
## 入力引数
iDir=${1:-"NULL"}           # 処理ディレクトリ
iDays=${2:-"NULL"}          # 削除対象日数（数値）
iTarget=${3:-"NULL"}        # 処理対象種別（「all」「dir」「file」のいずれか）

rc=0

###############################################
# １．引数チェック
###############################################

# 1)NULL値チェック
i=0
set ${iDir} ${iDays} ${iTarget}
while [ "$1" ]; do
    i=$((i+1))
    if [ "${1}" = "NULL" ]; then
        rc=9
        break
    else
        shift
    fi
done

# コメント変数の設定
if [[ $rc -ne 0 ]]; then
    case ${i} in
        1 )
            comVAL="引数１：処理ディレクトリ"
        ;;
        2 )
            comVAL="引数２：削除対象日数（数値）"
        ;;
        3 )
            comVAL="引数３：処理対象種別（「all」「dir」「file」のいずれか）"
        ;;
    esac
fi

# 終了ステータス判定
if [ $rc -ne 0 ]; then
    # 処理を終了する
    echo "引数が正しく指定されていません。"
    echo ${comVAL}"がnull。"
    exit 9
fi

###############################################
# ２．想定外値入力チェック
###############################################

#１）規定値でない値が設定されているかチェックする

if [ ! -d "${iDir}" ]; then #ディレクトリ存在チェック
    echo "引数１：処理ディレクトリは存在しません。"
    echo "設定値："${iDir}
    exit 9
elif [[ ! "$iDays" =~ ^[0-9]+$ ]]; then # 削除期間の数値チェック
    echo "引数２：削除対象日数（数値）に数値以外が設定されています。"
    echo "設定値："${iDays}
    exit 9
elif [ "${iTarget}" != "all" ] && [ "${iTarget}" != "dir" ] && [ "${iTarget}" != "file" ]; then #処理種別
    echo "設定値："${iTarget}
    echo "想定値：「all」「dir」「file」"
    echo "引数３：処理対象種別に想定外な値が設定されています。"
    exit 9
fi

###############################################
# ３．削除実行
###############################################

#１）削除コマンド生成
case ${iTarget} in
    "all" )
        cmdStr="find ${iDir} -maxdepth 1 -mindepth 1 -mtime +${iDays} | xargs rm -rf"
    ;;
    "dir" )
        cmdStr="find ${iDir} -maxdepth 1 -mindepth 1 -mtime +${iDays} -type d | xargs rm -rf"
    ;;
    "file" )
        cmdStr="find ${iDir} -maxdepth 1 -mindepth 1 -mtime +${iDays} -type f | xargs rm -f"
    ;;

esac

#２）コマンド実行
eval ${cmdStr}
rc=$?

# 終了ステータス判定
if [ $rc -ne 0 ]; then
    # 処理を終了する
    echo "削除が異常終了しました。"
    echo "コマンド："${cmdStr}

    exit 9
fi

################################################
## N．後処理
################################################

# exit 0して終わる

exit 0