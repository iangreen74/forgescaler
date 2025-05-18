output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "vpc_id" {
  value = module.network.vpc_id
}

output "bucket_name" {
  value = module.s3.memory_logs_bucket
}

output "cert_arn" {
  value = module.acm.cert_arn
}
