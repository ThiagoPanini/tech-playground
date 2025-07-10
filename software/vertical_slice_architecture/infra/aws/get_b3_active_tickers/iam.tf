/* --------------------------------------------------------
FILE: iam.tf @ get-b3-active-tickers module

Creation of IAM policies and roles necessary for granting 
privileges and access to resources instantiated in AWS 
environment for the purpose of collecting information 
about financial assets listed on B3.
-------------------------------------------------------- */

module "aws_iam_role" {
  source = "git::https://github.com/ThiagoPanini/tf-modules-showcase.git?ref=aws/iam-role/v0.1.0"

  role_name                   = "tech_playground_get_b3_active_tickers_lambda_role"
  trust_policy_filepath       = "${path.module}/assets/iam/trust_policies/trust-lambda.json"
  policy_templates_source_dir = "${path.module}/assets/iam/policy_templates"

  policy_templates_vars = {
    "region_name" = local.region_name,
    "account_id"  = local.account_id,
    "table_name"  = var.dynamodb_b3_active_tickers_table_name
  }

}
