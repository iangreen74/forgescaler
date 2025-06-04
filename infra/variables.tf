variable "aws_region" {
  description = "AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

variable "name" {
  description = "Base name for resources"
  type        = string
}

# NETWORK

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "List of public subnet CIDR blocks"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "List of private subnet CIDR blocks"
  type        = list(string)
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

# DNS + ACM

variable "domain_name" {
  description = "The root domain name"
  type        = string
}

variable "zone_id" {
  description = "Route 53 zone ID for the domain"
  type        = string
}

variable "cloudfront_domain_name" {
  description = "Domain name for CloudFront distribution"
  type        = string
}

variable "alias_zone_id" {
  description = "Route53 alias zone ID"
  type        = string
}
