# S3 Bucket for Forgemind Memory Logs

resource "aws_s3_bucket" "memory_logs" {
  bucket = var.bucket_name
  force_destroy = true

  tags = {
    Environment = "forgemind"
  }
}

resource "aws_s3_bucket_versioning" "memory_logs_versioning" {
  bucket = aws_s3_bucket.memory_logs.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "memory_logs_encryption" {
  bucket = aws_s3_bucket.memory_logs.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
