#!/bin/bash

# Required inputs
CLUSTER_NAME=$1
CLUSTER_ENDPOINT=$2
CLUSTER_CA=$3
AWS_REGION=${4:-us-east-1}

# Output location
KUBECONFIG_FILE=${5:-"./kubeconfig"}

if [[ -z "$CLUSTER_NAME" || -z "$CLUSTER_ENDPOINT" || -z "$CLUSTER_CA" ]]; then
  echo "Usage: $0 <cluster_name> <cluster_endpoint> <cluster_ca> [aws_region] [output_path]"
  exit 1
fi

cat > "$KUBECONFIG_FILE" <<EOF
apiVersion: v1
clusters:
- cluster:
    server: ${CLUSTER_ENDPOINT}
    certificate-authority-data: ${CLUSTER_CA}
  name: ${CLUSTER_NAME}
contexts:
- context:
    cluster: ${CLUSTER_NAME}
    user: aws
  name: ${CLUSTER_NAME}
current-context: ${CLUSTER_NAME}
kind: Config
preferences: {}
users:
- name: aws
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      command: aws
      args:
        - "eks"
        - "get-token"
        - "--region"
        - "${AWS_REGION}"
        - "--cluster-name"
        - "${CLUSTER_NAME}"
EOF

echo "✅ Kubeconfig generated at: $KUBECONFIG_FILE"
