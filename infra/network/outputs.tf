variable "vpc_cidr_block" {
  description = "CIDR block for the default/original VPC"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "Public subnet CIDRs for the original VPC"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "Private subnet CIDRs for the original VPC"
  type        = list(string)
}

variable "vpc_cidr_block_v2" {
  description = "CIDR block for the second (new) VPC"
  type        = string
}

variable "public_subnet_cidrs_v2" {
  description = "List of public subnet CIDRs for new VPC"
  type        = list(string)
}

variable "private_subnet_cidrs_v2" {
  description = "List of private subnet CIDRs for new VPC"
  type        = list(string)
}

variable "availability_zones" {
  description = "List of availability zones to deploy resources in"
  type        = list(string)
}
