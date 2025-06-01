output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "bucket_name" {
  value = module.s3.memory_logs_bucket
}

output "cert_arn" {
  value = module.acm.cert_arn
}

output "vpc_id" {
  value = module.network_v2.vpc_id
}

output "public_subnet_ids" {
  value = module.network_v2.public_subnet_ids
}

output "private_subnet_ids" {
  value = module.network_v2.private_subnet_ids
}

