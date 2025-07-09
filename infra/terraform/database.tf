# RDS module for database
module "database" {
  source = "./modules/rds"
  
  # Database configuration
  db_instance_class = var.db_instance_class
  db_name          = var.db_name
  db_username      = var.db_username
  db_password      = var.db_password
  
  # Network configuration
  subnet_ids         = var.private_subnet_ids
  security_group_ids = [aws_security_group.db_sg.id]
  
  # Default tags
  tags = local.common_tags
}

# Security group for the database
resource "aws_security_group" "db_sg" {
  name        = "${var.project_name}-db-sg"
  description = "Security group for PostgreSQL database"
  
  # Allow MySQL/PostgreSQL connections from application
  ingress {
    description     = "Database connection"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.app_sg.id]
  }
  
  tags = merge(local.common_tags, {
    Name = "${var.project_name}-db-sg"
  })
}

# Database-specific variables
variable "db_instance_class" {
  description = "RDS instance class (example: db.t3.micro)"
  type        = string
  default     = "db.t3.micro"
}

variable "db_name" {
  description = "Initial database name"
  type        = string
  default     = "verticalslicedb"
}

variable "db_username" {
  description = "Database administrator username"
  type        = string
  default     = "admin"
}

variable "db_password" {
  description = "Administrator user password (should be provided via environment variables)"
  type        = string
  sensitive   = true
}

variable "private_subnet_ids" {
  description = "Private subnet IDs where the database will be created"
  type        = list(string)
  default     = []
}