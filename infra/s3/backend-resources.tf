# S3 bucket for Terraform state backend
resource "aws_s3_bucket" "tf_state" {
  bucket = "forgemind-terraform-state"
  force_destroy = true

  tags = {
    Purpose = "Terraform backend"
    Environment = "forgemind"
  }
}

resource "aws_s3_bucket_versioning" "tf_state_versioning" {
  bucket = aws_s3_bucket.tf_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_dynamodb_table" "tf_locks" {
  name         = "forgemind-terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Purpose = "Terraform lock"
    Environment = "forgemind"
  }
}
