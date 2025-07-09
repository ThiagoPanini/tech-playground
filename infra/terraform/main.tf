# Main Terraform configuration for vertical slice architecture
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# AWS Provider - region configuration
provider "aws" {
  region = var.aws_region
}

# Local data to define common tags
locals {
  common_tags = {
    Environment = var.environment
    Project     = "vertical-slice-architecture"
    Owner       = "DevOps Team"
    # Created by Terraform
    ManagedBy   = "Terraform"
  }
}

# Configuration variables
variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "Project name for resource identification"
  type        = string
  default     = "vertical-slice-app"
}

# Security Group for the application
resource "aws_security_group" "app_sg" {
  name        = "${var.project_name}-app-sg"
  description = "Security group for vertical slice architecture application"
  
  # Ingress rules - allows HTTP and HTTPS traffic
  ingress {
    description = "HTTP traffic"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    description = "HTTPS traffic"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # Egress rules - allows all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = merge(local.common_tags, {
    Name = "${var.project_name}-app-sg"
  })
}

# Important outputs
output "security_group_id" {
  description = "Application security group ID"
  value       = aws_security_group.app_sg.id
}

output "environment" {
  description = "Current environment"
  value       = var.environment
}