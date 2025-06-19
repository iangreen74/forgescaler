variable "bucket_name" {
  description = "The name of the S3 bucket for dashboard"
  type        = string
}

variable "dashboard_domain" {
  description = "Subdomain for dashboard (e.g. dashboard.vaultscaler.com)"
  type        = string
}

variable "acm_certificate_arn" {
  description = "ACM cert for CloudFront"
  type        = string
}

variable "route53_zone_id" {
  description = "Hosted zone ID for vaultscaler.com"
  type        = string
}
