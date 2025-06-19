terraform {
  required_version = ">= 1.5.0"
  backend "s3" {
    bucket         = "forgescaler-terraform-state"
    key            = "dashboard/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "dashboard_site" {
  source              = "./dashboard_site"
  bucket_name         = "vaultscaler-dashboard-site"
  dashboard_domain    = "dashboard.vaultscaler.com"
  acm_certificate_arn = var.acm_certificate_arn
  route53_zone_id     = var.route53_zone_id
}
