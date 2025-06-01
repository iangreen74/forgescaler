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
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.region
}

#module "network" {
#source             = "./network"
#name               = "forgemind-vpc"
#cidr_block         = var.cidr_block
#availability_zones = var.availability_zones
#private_subnets    = var.private_subnets
#public_subnets     = var.public_subnets
#}

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
  source                 = "./dns"
  zone_id                = var.zone_id
  alias_zone_id          = var.alias_zone_id
  cloudfront_domain_name = var.cloudfront_domain_name
  domain_name            = var.domain_name
}

module "network_v2" {
  source = "./network"

  vpc_cidr_block       = var.vpc_cidr_block
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
}

module "eks" {
  source             = "./eks"
  cluster_name       = "forgescaler-cluster"
  subnet_ids         = module.network_v2.private_subnet_ids
  vpc_id             = module.network_v2.vpc_id
  availability_zones = var.availability_zones
}



