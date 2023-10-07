## CONFIGURE PROVIDERS
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["./credentials"]
  default_tags {
    tags = {
      Name       = "coverlettergen"
      Automation = "Terraform"
    }
  }
}

#------------------------------------------------------------

## Configure a provider to build the Dockerfile from within terraform
data "aws_ecr_authorization_token" "ecr_token" {}

provider "docker" {
  registry_auth {
    address  = data.aws_ecr_authorization_token.ecr_token.proxy_endpoint
    username = data.aws_ecr_authorization_token.ecr_token.user_name
    password = data.aws_ecr_authorization_token.ecr_token.password
  }
}

#------------------------------------------------------------
# CONFIGURE LOCAL VARIABLES
data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

locals {
  server_image  = aws_ecr_repository.coverlettergen_server.repository_url
  worker_image  = aws_ecr_repository.coverlettergen_worker.repository_url
  redis_address = aws_elasticache_cluster.coverlettergen_redis.cache_nodes.0.address
  redis_port    = aws_elasticache_cluster.coverlettergen_redis.cache_nodes.0.port
  envs = { for tuple in regexall("(.*)=(.*)", file(".env")) : tuple[0] => sensitive(tuple[1]) }
}

data "aws_iam_role" "lab" {
  name = "LabRole"
}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

#------------------------------------------------------------
# CONFIGURE DEPLOYMENT URL OUTPUT AFTER BUILD
resource "local_file" "url" {
  content  = "http://${aws_lb.coverlettergen.dns_name}"
  filename = "./api.txt"
}

#------------------------------------------------------------
