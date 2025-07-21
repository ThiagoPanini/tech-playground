/* -----------------------------------------------------------------------------
  FILE: sqs.tf
  MODULE: aws/get-b3-stock-tickers

  DESCRIPTION:
    This Terraform file uses a module to provision an AWS SQS queue for the
    "get-b3-stock-tickers" Lambda function. The queue's configuration is loaded
    from an external JSON file, and attributes are generated from templates
    with variable substitution.

  RESOURCES:
    - module.aws_sqs_queue:
        Provisions an SQS queue with the specified configuration and attributes
        generated from templates. The module supports variable substitution for
        queue attributes and uses external files for configuration.
----------------------------------------------------------------------------- */

module "sqs_queue" {
  source = "git::https://github.com/ThiagoPanini/tfbox.git?ref=aws/sqs-queue/v0.1.0"

  name                              = var.sqs_queue_name
  visibility_timeout_seconds        = var.sqs_queue_visibility_timeout_seconds
  message_retention_seconds         = var.sqs_queue_message_retention_seconds
  delay_seconds                     = var.sqs_queue_delay_seconds
  max_message_size                  = var.sqs_queue_max_message_size
  receive_wait_time_seconds         = var.sqs_queue_receive_wait_time_seconds
  create_dead_letter_queue          = true
  copy_dlq_config_from_source_queue = true

}
