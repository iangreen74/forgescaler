variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "cidr_block" {
  default = "10.0.0.0/16"
}

variable "availability_zones" {
  default = ["us-west-2a", "us-west-2b", "us-west-2c"]
}

variable "private_subnets" {
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "public_subnets" {
  default = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}

variable "role_name" {
  default = "forgemind-agents-role"
}

variable "bucket_name" {
  default = "forgemind-memory-logs"
}

variable "domain_name" {
  default = "forgemind.io"
}

variable "zone_id" {
  description = "Route53 Hosted Zone ID"
  type        = string
}

variable "alias_zone_id" {
  description = "Zone ID of the ALB or CloudFront for aliasing"
  type        = string
}

variable "cluster_name" {
  default = "forgemind-cluster"
}
