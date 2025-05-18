terraform {
  backend "s3" {
    bucket         = "forgemind-terraform-state"
    key            = "global/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "forgemind-terraform-locks"
    encrypt        = true
  }
}
