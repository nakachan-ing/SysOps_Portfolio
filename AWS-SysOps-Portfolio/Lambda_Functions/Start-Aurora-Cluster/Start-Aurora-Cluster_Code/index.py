import boto3
import logging
import json
from datetime import datetime

# ログの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    client = boto3.client('rds')
    cluster_id = 'ecsite-db-cluster'
    
    try:
        # クラスターの状態を確認
        response = client.describe_db_clusters(DBClusterIdentifier=cluster_id)
        cluster_status = response['DBClusters'][0]['Status']
        
        if cluster_status in ['stopped', 'inaccessible-encryption-credentials-recoverable']:
            start_response = client.start_db_cluster(DBClusterIdentifier=cluster_id)
            logger.info("DB Cluster started successfully: %s", start_response)
            
            # JSONシリアライズ可能な形式に変換
            response_serializable = convert_to_serializable(start_response)
            return {
                'statusCode': 200,
                'body': json.dumps(response_serializable)
            }
        else:
            logger.info("DB Cluster is not in a stopped state. Current state: %s", cluster_status)
            return {
                'statusCode': 200,
                'body': json.dumps({'message': f"DB Cluster is not in a stopped state. Current state: {cluster_status}"})
            }
        
    except Exception as e:
        logger.error("Error starting DB Cluster: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def convert_to_serializable(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(i) for i in obj]
    else:
        return obj
