#!/bin/bash
umask 007
## 入力引数
iFromDir=${1:-"NULL"}                   # アーカイブ元ディレクトリ
iToDir=${2:-"NULL"}                     # アーカイブ先ディレクトリ
iDays=${3:-"NULL"}                      # 処理対象経過日数（数値）
iFindCond=${4:-"NULL"}                  # 処理対象経ファイル名検索条件

rc=0

###############################################
# １．引数チェック
###############################################

# 1)NULL値チェック
i=0
set ${iFromDir} ${iToDir} ${iDays} ${iFindCond}
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
                        comVAL="引数１：アーカイブ元ディレクトリ"
                ;;
                2 )
                        comVAL="引数２：アーカイブ先ディレクトリ"
                ;;
                3 )
                        comVAL="引数３：処理対象経過日数（数値）"
                ;;
                4 )
                        comVAL="引数４：処理対象経ファイル名検索条件"
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

if [ ! -d "${iFromDir}" ]; then #ディレクトリ存在チェック
        echo "引数１：アーカイブ元ディレクトリは存在しません。"
        echo "設定値："${iFromDir}
        exit 9
elif [ ! -d "${iToDir}" ]; then #ディレクトリ存在チェック
        echo "引数２：アーカイブ先ディレクトリは存在しません。"
        echo "設定値："${iToDir}
        exit 9
elif [[ ! "$iDays" =~ ^[0-9]+$ ]]; then # 処理対象経過日数の数値チェック
        echo "引数３：処理対象経過日数（数値）に数値以外が設定されています。"
        echo "設定値："${iDays}
        exit 9
fi

###############################################
# ３．圧縮・移動実行
###############################################

#１）圧縮・移動
find ${iFromDir} -name "${iFindCond}" -mtime +${iDays} -type f | xargs -I {} sh -c 'gzip {} && mv -f {}.gz '"${iToDir}"
rc=$?

# 終了ステータス判定
if [ $rc -ne 0 ]; then
        # 処理を終了する
        echo "圧縮・移動が異常終了しました。"
        echo "コマンド：find ${iDir} -name "${serchConf}" -mtime +${iDays} -type f | xargs -I {} sh -c 'gzip {} && mv -f {}.gz "${iToDir}"'"

        exit 9
fi

################################################
## N．後処理
################################################

# exit 0して終わる

exit 0