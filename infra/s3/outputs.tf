output "memory_logs_bucket" {
  description = "S3 bucket used for memory logs"
  value       = aws_s3_bucket.memory_logs.id
}
