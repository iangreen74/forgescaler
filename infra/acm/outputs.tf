output "cert_arn" {
  description = "The ARN of the ACM certificate"
  value       = aws_acm_certificate.forgemind_cert.arn
}
