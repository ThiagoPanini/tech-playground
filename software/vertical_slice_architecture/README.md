
# Vertical Slice Architecture - B3 Stock Tickers

This project demonstrates a **Vertical Slice Architecture** for fetching and storing stock ticker information from the B3 (Brazilian Stock Exchange). It follows clean architecture principles, with clear separation of concerns and dependency inversion.


## Overview

The application scrapes stock ticker data from the Fundamentus website and processes it using a vertical slice approach. Each feature is self-contained and includes all layers from presentation to infrastructure.


## Architecture

The project implements vertical slice architecture with these layers:
- **Domain**: Core business entities and interfaces
- **Use Cases**: Application business logic
- **Infrastructure**: External adapters and repositories
- **Presentation**: Entry points and handlers


## Features

### Get B3 Stock Tickers
Retrieves active stock tickers from the B3 exchange via web scraping.

**Flow:**
1. HTTP request to Fundamentus portal
2. HTML parsing to extract ticker information
3. Data transformation to domain entities
4. Optional storage in DynamoDB


## Project Structure

```
app/
├── src/
│   └── features/
│       ├── cross/                          # Shared components
│       │   ├── domain/                     # Shared domain entities
│       │   ├── infra/                      # Shared infrastructure adapters
│       │   ├── utils/                      # Utilities and helpers
│       │   └── value_objects/              # Shared value objects
│       └── get_b3_stock_tickers/           # Feature slice
│           ├── domain/                     # Domain layer
│           │   ├── entities/               # Business entities
│           │   └── interfaces/             # Abstract interfaces
│           ├── infra/                      # Infrastructure layer
│           │   ├── adapters/               # External service adapters
│           │   └── repositories/           # Data persistence
│           ├── presentation/               # Presentation layer
│           ├── use_case/                   # Application use cases
└── tests/                                  # Test files
    └── local/                              # Local testing
infra/                                      # Infrastructure as Code
└── aws/                                    # AWS Terraform configurations
    └── get_b3_active_tickers/              # AWS resources for the feature
```


## Technologies

- **Python 3.12+**
- **BeautifulSoup4**: HTML parsing
- **Requests**: HTTP client
- **PynamoDB**: DynamoDB ORM
- **Boto3**: AWS SDK
- **Terraform**: Infrastructure as Code


## Getting Started

### Prerequisites

- Python 3.12 or higher
- AWS account (for DynamoDB storage)
- Terraform (for infrastructure deployment)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Infrastructure Deployment

Deploy AWS infrastructure using Terraform:
```bash
cd infra/aws/get_b3_active_tickers
terraform init
terraform plan
terraform apply
```

### Local Testing

Run the application locally:
```bash
python -m app.tests.local.run_local
```

## Key Components

### Domain Entities
- **B3StockTicker**: Core entity representing a stock ticker with company information

### Interfaces
- **IDatabaseRepository**: Contract for data persistence
- **IHTMLParserAdapter**: Contract for HTML parsing
- **IHTTPClientAdapter**: Contract for HTTP operations

### Adapters
- **FundamentusHTMLParserAdapter**: Parses HTML from Fundamentus website
- **RequestsHTTPClientAdapter**: HTTP client implementation using requests library
- **DynamoDBDatabaseRepository**: DynamoDB storage implementation

### Use Cases
- **GetB3StockTickersUseCase**: Orchestrates the ticker retrieval process


## Architecture Benefits

- **Feature Isolation**: Each feature is self-contained
- **Testability**: Clear boundaries for unit testing
- **Maintainability**: Changes are localized to specific features
- **Scalability**: Easy to add new features without affecting existing ones
- **Dependency Inversion**: High-level modules don't depend on low-level modules


## Contributing

When adding new features:
1. Create a new feature slice following the established structure
2. Implement required interfaces
3. Add appropriate tests
4. Update documentation

## License

This project is part of the tech-playground repository and follows the same MIT license.