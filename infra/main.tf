terraform {
  backend "s3" {
    bucket         = "forgescaler-terraform-state"
    key            = "state/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "forgescaler-terraform-locks"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

module "network" {
  source               = "./modules/network"
  vpc_cidr_block       = var.vpc_cidr_block
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
}

module "eks" {
  source = "./modules/eks"

  cluster_name       = var.cluster_name
  vpc_id             = module.network.vpc_id
  subnet_ids         = module.network.private_subnet_ids
  availability_zones = var.availability_zones
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = var.s3_bucket_name
}

module "iam" {
  source = "./modules/iam"
}

module "acm" {
  source      = "./modules/acm"
  domain_name = var.domain_name
  zone_id     = var.zone_id
}

module "dns" {
  source      = "./modules/dns"
  domain_name = var.domain_name
  zone_id     = var.zone_id
}
