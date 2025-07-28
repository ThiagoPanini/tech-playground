/* -----------------------------------------------------------------------------
FILE: dynamodb.tf @ get-b3-active-tickers module

DESCRIPTION:
  This Terraform configuration uses a remote module to provision an AWS DynamoDB
  table for storing B3 active tickers. The table's name, hash key, range key,
  and attribute definitions are parameterized via input variables for flexible
  deployments.

RESOURCES:
  - module.aws_dynamodb_table:
    Deploys a DynamoDB table using the tfbox module with configurable properties
    such as name, hash key, range key, and attributes.
----------------------------------------------------------------------------- */


module "aws_dynamodb_table" {
  source = "git::https://github.com/ThiagoPanini/tfbox.git?ref=aws/dynamodb-table/v0.1.2"

  name      = var.dynamodb_table_name
  hash_key  = var.dynamodb_table_hash_key
  range_key = var.dynamodb_table_range_key

  attributes = var.dynamodb_table_attributes
}
