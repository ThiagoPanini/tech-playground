# RDS module for PostgreSQL
# This module creates an RDS instance optimized for vertical slice architecture applications

# Subnet group for RDS
resource "aws_db_subnet_group" "main" {
  name       = "${var.project_name}-subnet-group"
  subnet_ids = var.subnet_ids
  
  tags = merge(var.tags, {
    Name = "${var.project_name}-subnet-group"
  })
}

# PostgreSQL RDS instance
resource "aws_db_instance" "main" {
  # Basic configuration
  identifier = "${var.project_name}-database"
  engine     = "postgres"
  engine_version = "15.4"
  
  # Instance specifications
  instance_class    = var.db_instance_class
  allocated_storage = 20
  storage_type      = "gp2"
  storage_encrypted = true
  
  # Database configuration
  db_name  = var.db_name
  username = var.db_username
  password = var.db_password
  
  # Network configuration
  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = var.security_group_ids
  
  # Backup and maintenance configuration
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  # Performance configuration
  performance_insights_enabled = true
  monitoring_interval         = 60
  
  # Security configuration
  deletion_protection = false  # Set to true in production
  skip_final_snapshot = true   # Set to false in production
  
  tags = merge(var.tags, {
    Name = "${var.project_name}-database"
  })
}

# Module variables
variable "project_name" {
  description = "Project name for resource identification"
  type        = string
}

variable "db_instance_class" {
  description = "RDS instance class"
  type        = string
  default     = "db.t3.micro"
}

variable "db_name" {
  description = "Initial database name"
  type        = string
}

variable "db_username" {
  description = "Administrator username"
  type        = string
}

variable "db_password" {
  description = "Administrator password"
  type        = string
  sensitive   = true
}

variable "subnet_ids" {
  description = "Subnet IDs where the instance will be created"
  type        = list(string)
}

variable "security_group_ids" {
  description = "Security group IDs"
  type        = list(string)
}

variable "tags" {
  description = "Common tags for all resources"
  type        = map(string)
  default     = {}
}

# Module outputs
output "db_instance_endpoint" {
  description = "RDS instance endpoint"
  value       = aws_db_instance.main.endpoint
}

output "db_instance_id" {
  description = "RDS instance ID"
  value       = aws_db_instance.main.id
}

output "db_instance_arn" {
  description = "RDS instance ARN"
  value       = aws_db_instance.main.arn
}