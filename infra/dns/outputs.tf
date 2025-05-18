output "apex_dns_record" {
  value = aws_route53_record.apex.fqdn
}

output "www_dns_record" {
  value = aws_route53_record.www.fqdn
}
