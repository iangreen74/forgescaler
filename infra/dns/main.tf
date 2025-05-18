# Route53 DNS Record for Forgemind

resource "aws_route53_record" "forgemind_dns" {
  zone_id = var.zone_id
  name    = var.domain_name
  type    = "A"

  alias {
    name                   = var.alias_name
    zone_id                = var.alias_zone_id
    evaluate_target_health = true
  }
}
