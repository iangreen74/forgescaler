output "vpc_id" {
  value = module.network_v2.vpc_id
}

output "private_subnet_ids" {
  value = module.network_v2.private_subnet_ids
}

output "public_subnet_ids" {
  value = module.network_v2.public_subnet_ids
}

output "vpc_cidr_block" {
  value = module.network_v2.vpc_cidr_block
}
