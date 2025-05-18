variable "zone_id" {
  description = "Route53 public hosted zone ID"
  type        = string
}

variable "alias_zone_id" {
  description = "CloudFront or ALB alias zone ID"
  type        = string
  default     = "Z2FDTNDATAQYW2" # CloudFront global zone ID
}

variable "cloudfront_domain_name" {
  description = "Domain name of CloudFront distribution"
  type        = string
}

variable "domain_name" {
  description = "The root domain name"
  type        = string
  default     = "forgescaler.com"
}
