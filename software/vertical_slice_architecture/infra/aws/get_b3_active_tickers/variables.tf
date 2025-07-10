/* --------------------------------------------------------
ARQUIVO: variables.tf @ get-active-tickers module

Arquivo de variáveis definidas para configurar todas as
declarações de recursos necessárias para implantação das
peças de coleta e armazenamento de informações básicas de
ativos financeiros listados na B3.
-------------------------------------------------------- */


/* --------------------------------------------------------
   VARIÁVEIS: DynamoDB
-------------------------------------------------------- */

variable "dynamodb_b3_active_tickers_table_name" {
  description = "Nome da tabela a ser criada no DynamoDB para armazenar informações básicas de tickers listados na B3"
  type        = string
  default     = "tbl_b3_active_tickers"
}

variable "dynamodb_b3_active_tickers_table_hash_key" {
  description = "Nome da variável associada como Hash Key da tabela"
  type        = string
  default     = "code"
}

variable "dynamodb_b3_active_tickers_table_range_key" {
  description = "Nome da variável associada como Range Key da tabela"
  type        = string
  default     = "date_extracted"
}

variable "dynamodb_b3_active_tickers_table_attributes" {
  description = "Lista de atributos indexados (hash ou range key) associados à tabela"
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
   VARIÁVEIS: Policies e Role IAM
-------------------------------------------------------- */

