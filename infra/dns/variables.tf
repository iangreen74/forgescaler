variable "zone_id" {
  description = "Route53 Hosted Zone ID"
  type        = string
}

variable "domain_name" {
  description = "The domain name to use for Forgemind"
  type        = string
}

variable "alias_name" {
  description = "The ALB DNS name or CloudFront distribution name"
  type        = string
}

variable "alias_zone_id" {
  description = "The ALB or CloudFront zone ID"
  type        = string
}
