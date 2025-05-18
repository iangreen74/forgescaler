# ACM Certificate for HTTPS

resource "aws_acm_certificate" "forgemind_cert" {
  domain_name       = var.domain_name
  validation_method = "DNS"

  tags = {
    Environment = "forgemind"
  }

  lifecycle {
    create_before_destroy = true
  }
}
