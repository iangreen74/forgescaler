output "dns_record_name" {
  description = "The DNS record name for Forgemind"
  value       = aws_route53_record.forgemind_dns.name
}
