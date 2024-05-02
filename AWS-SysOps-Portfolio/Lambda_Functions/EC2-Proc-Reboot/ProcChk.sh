#!/bin/bash
################################################################################
# シェル名      ：ProcChk.sh
# シェル説明    ：プロセス監視及び再起動(httpd)
# 戻り値        ： 0＝正常終了
#                  1＝異常終了
# Cron式       : #00 * * * * root bash /opt/shell/ProcChk.sh 2>&1
################################################################################
# チェックするプロセスリスト
process_list=(
    "httpd systemctl start httpd"
    # 他のプロセスも必要に応じて追加
)

# 関数定義
function FcLOG {
    if [ $RC -ne 0 ]; then
        logger -p local1.warn "ProcCheck : [Warning] ${message}"
    else
        logger -p local1.info "ProcCheck : [info] ${message}"
    fi
}

function FcProcCheck {
    local proc_name=$1
    local proc_cmd=$2

    # プロセスのチェック
    pid=$(pgrep "$proc_name")
    if [ -n "$pid" ]; then
        logger -p local1.info "$proc_name process is running with PID: $pid"
    else
        logger -p local1.warn "$proc_name process is not running"
        # プロセスが起動していない場合の処理を記述
        if [ -n "$proc_cmd" ]; then
            $proc_cmd
            if [ $? -ne 0 ]; then
                RC=1 ; message="${proc_name} restart error" ; FcLOG
            else
                RC=0 ; message="${proc_name} restart success" ; FcLOG
            fi
        fi
    fi
}

# メイン処理
for proc_info in "${process_list[@]}"; do
    proc_name=$(echo "$proc_info" | cut -d' ' -f1)
    proc_cmd=$(echo "$proc_info" | cut -d' ' -f2-)

    FcProcCheck "$proc_name" "$proc_cmd"
done

exit