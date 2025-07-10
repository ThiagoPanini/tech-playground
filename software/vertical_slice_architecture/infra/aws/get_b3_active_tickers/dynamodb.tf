/* --------------------------------------------------------
FILE: dynamodb.tf @ get-b3-active-tickers module

Creation of a DynamoDB table preconfigured as a storage 
resource for items obtained through interface for 
collecting information about financial assets listed on B3.
-------------------------------------------------------- */

module "aws_dynamodb_table" {
  source = "git::https://github.com/ThiagoPanini/tf-modules-showcase.git?ref=aws/dynamodb-table/v0.1.1"

  name      = var.dynamodb_b3_active_tickers_table_name
  hash_key  = var.dynamodb_b3_active_tickers_table_hash_key
  range_key = var.dynamodb_b3_active_tickers_table_range_key

  attributes = var.dynamodb_b3_active_tickers_table_attributes
}
