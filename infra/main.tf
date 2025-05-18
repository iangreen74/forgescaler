terraform {
  required_version = ">= 1.4.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "forgescaler-terraform-state"
    key    = "global/terraform.tfstate"
    region = "us-west-2"
  }
}

provider "aws" {
  region = var.region
}

module "network" {
  source             = "./network"
  name               = "forgemind-vpc"
  cidr_block         = var.cidr_block
  availability_zones = var.availability_zones
  private_subnets    = var.private_subnets
  public_subnets     = var.public_subnets
}

module "iam" {
  source    = "./iam"
  role_name = var.role_name
}

module "s3" {
  source      = "./s3"
  bucket_name = var.bucket_name
}

module "acm" {
  source      = "./acm"
  domain_name = var.domain_name
}

module "dns" {
  source        = "./dns"
  zone_id       = var.zone_id
  domain_name   = var.domain_name
  alias_name    = module.eks.cluster_endpoint
  alias_zone_id = var.alias_zone_id
}

module "eks" {
  source       = "./eks"
  cluster_name = var.cluster_name
  subnet_ids   = module.network.private_subnets
  vpc_id       = module.network.vpc_id
}
