variable "domain_name" {
  description = "The domain name to create a TLS certificate for"
  type        = string
}

# modules/acm/variables.tf
variable "zone_id" {
  description = "The Route53 hosted zone ID"
  type        = string
}
