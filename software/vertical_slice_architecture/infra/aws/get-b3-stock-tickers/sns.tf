/* -----------------------------------------------------------------------------
  FILE: sns.tf
  MODULE: aws/get-b3-stock-tickers

  DESCRIPTION:
    This Terraform file uses a module to provision an AWS SNS topic for the
    "get-b3-stock-tickers" Lambda function.

  RESOURCES:
    
----------------------------------------------------------------------------- */

resource "aws_sns_topic" "tickers_topic" {
  name         = "techplay-b3-stock-tickers-topic"
  fifo_topic   = false
  display_name = "B3 Stock Tickers Topic"
}
