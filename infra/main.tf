terraform {
  backend "s3" {
    bucket         = "forgescaler-terraform-state"
    key            = "infra/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }

  required_version = ">= 1.5.0"
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

module "network" {
  source               = "./modules/network"
  name                 = var.name
  vpc_cidr_block       = var.vpc_cidr_block
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
}

module "iam" {
  source = "./iam"
}

module "s3" {
  source = "./s3"
}

module "acm" {
  source      = "./acm"
  domain_name = var.domain_name
  zone_id     = var.zone_id
}

module "dns" {
  source      = "./dns"
  domain_name = var.domain_name
  zone_id     = var.zone_id
}

module "eks" {
  source             = "./eks"
  cluster_name       = var.name
  vpc_id             = module.network.vpc_id
  subnet_ids         = module.network.private_subnet_ids
  availability_zones = var.availability_zones
}
