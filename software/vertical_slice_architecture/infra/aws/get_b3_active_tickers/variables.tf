/* --------------------------------------------------------
FILE: variables.tf @ get-active-tickers module

Variables file defined to configure all necessary resource 
declarations for deployment of collection and storage 
components for basic information about financial assets 
listed on B3.
-------------------------------------------------------- */


/* --------------------------------------------------------
   VARIABLES: DynamoDB
-------------------------------------------------------- */

variable "dynamodb_b3_active_tickers_table_name" {
  description = "Name of the table to be created in DynamoDB to store basic information about tickers listed on B3"
  type        = string
  default     = "tbl_b3_active_tickers"
}

variable "dynamodb_b3_active_tickers_table_hash_key" {
  description = "Name of the variable associated as Hash Key of the table"
  type        = string
  default     = "code"
}

variable "dynamodb_b3_active_tickers_table_range_key" {
  description = "Name of the variable associated as Range Key of the table"
  type        = string
  default     = "date_extracted"
}

variable "dynamodb_b3_active_tickers_table_attributes" {
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
   VARIABLES: IAM Policies and Role
-------------------------------------------------------- */

