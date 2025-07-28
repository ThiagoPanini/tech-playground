/* -----------------------------------------------------------------------------
  FILE: variables.tf
  MODULE: aws/get-b3-stock-tickers

  DESCRIPTION:
    Variables for configuring all infrastructure resources related to the process
    of getting active stock tickers from B3 (the Brazilian Stock Exchange).
----------------------------------------------------------------------------- */


/* --------------------------------------------------------
   VARIABLES: DynamoDB
-------------------------------------------------------- */

variable "dynamodb_table_name" {
  description = "Name of the table to be created in DynamoDB to store basic information about tickers listed on B3"
  type        = string
  default     = "tbl_techplay_b3_stock_tickers"
}

variable "dynamodb_table_hash_key" {
  description = "Name of the variable associated as Hash Key of the table"
  type        = string
  default     = "code"
}

variable "dynamodb_table_range_key" {
  description = "Name of the variable associated as Range Key of the table"
  type        = string
  default     = "date_extracted"
}

variable "dynamodb_table_attributes" {
  description = "List of indexed attributes (hash or range key) associated with the table"
  type        = list(map(string))
  default = [
    {
      "name" : "code",
      "type" : "S"
    },
    {
      "name" : "date_extracted",
      "type" : "S"
    }
  ]
}


/* --------------------------------------------------------
   VARIABLES: SQS Queue
-------------------------------------------------------- */

variable "sqs_queue_name" {
  description = "Name of the SQS queue to be created for the get-b3-stock-tickers Lambda function"
  type        = string
  default     = "techplay_b3_stock_tickers_queue"
}

variable "sqs_queue_visibility_timeout_seconds" {
  description = "The visibility timeout for the queue (in seconds). Visibility timeout sets the length of time that a message received from a queue (by one consumer) will not be visible to the other message consumers."
  type        = number
  default     = 1080

  validation {
    condition     = var.sqs_queue_visibility_timeout_seconds >= 0 && var.sqs_queue_visibility_timeout_seconds <= 43200
    error_message = "Visibility timeout must be between 0 seconds and 43200 seconds (12 hours)."
  }
}

variable "sqs_queue_message_retention_seconds" {
  description = "The length of time, in seconds, that Amazon SQS retains a message that does not get deleted."
  type        = number
  default     = 3600

  validation {
    condition     = var.sqs_queue_message_retention_seconds >= 60 && var.sqs_queue_message_retention_seconds <= 1209600
    error_message = "Message retention must be between 60 seconds (1 minute) and 1209600 seconds (14 days)."
  }
}

variable "sqs_queue_delay_seconds" {
  description = "The time, in seconds, that the delivery of all messages in the queue will be delayed. Any messages sent to the queue remain invisible to consumers for the duration of the delay period"
  type        = number
  default     = 0

  validation {
    condition     = var.sqs_queue_delay_seconds >= 0 && var.sqs_queue_delay_seconds <= 900
    error_message = "Delay seconds must be between 0 and 900 seconds (15 minutes)."
  }
}

variable "sqs_queue_max_message_size" {
  description = "The limit of how many bytes a message can contain before Amazon SQS rejects it."
  type        = number
  default     = 262144

  validation {
    condition     = var.sqs_queue_max_message_size >= 1024 && var.sqs_queue_max_message_size <= 262144
    error_message = "Max message size must be between 1024 (1 KB) and 262144 bytes (256 KB)."
  }
}

variable "sqs_queue_receive_wait_time_seconds" {
  description = "The time for which a ReceiveMessage call will wait for a message to arrive. In other words, the maximum amount of time that polling will wait for messages to become available to receive."
  type        = number
  default     = 2

  validation {
    condition     = var.sqs_queue_receive_wait_time_seconds >= 0 && var.sqs_queue_receive_wait_time_seconds <= 20
    error_message = "Receive wait time must be between 0 and 20 seconds."
  }
}
