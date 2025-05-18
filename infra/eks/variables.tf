variable "cluster_name" {
  description = "The name of the EKS cluster"
  type        = string
  default     = "forgemind-cluster"
}

variable "subnet_ids" {
  description = "The subnet IDs for the EKS cluster"
  type        = list(string)
}

variable "vpc_id" {
  description = "The VPC ID where the EKS cluster will be deployed"
  type        = string
}
