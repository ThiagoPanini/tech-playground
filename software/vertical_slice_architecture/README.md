# Vertical Slice Architecture

A comprehensive implementation of Vertical Slice Architecture pattern using .NET 8, demonstrating how to organize code by features rather than technical layers.

## Overview

Vertical Slice Architecture is a software architecture pattern that emphasizes organizing code around features instead of technical layers. Each feature contains all the code it needs to function independently, including data access, business logic, and presentation concerns.

## Core Principles

### 1. Feature-Based Organization
- Code is organized by business features (e.g., Products, Orders, Users)
- Each feature is self-contained and independent
- Reduces coupling between different parts of the system

### 2. Minimized Sharing
- Shared code is kept to a minimum
- Each feature can evolve independently
- Reduces the risk of breaking changes affecting multiple areas

### 3. Request/Response Focus
- Each feature typically handles a specific request
- Clear input and output contracts
- Easy to understand and test

### 4. CQRS Integration
- Natural fit with Command Query Responsibility Segregation
- Separate read and write operations
- Optimized data access patterns

## Benefits

### Development Benefits
- **Faster Development**: Developers can work on features independently
- **Easier Onboarding**: New team members can focus on one feature at a time
- **Reduced Merge Conflicts**: Features are isolated, reducing code conflicts
- **Better Testability**: Each feature can be tested in isolation

### Maintenance Benefits
- **Easier Debugging**: Issues are contained within specific features
- **Simplified Refactoring**: Changes to one feature don't affect others
- **Independent Deployment**: Features can potentially be deployed separately
- **Better Code Organization**: Clear structure makes code easier to navigate

### Business Benefits
- **Faster Time to Market**: Features can be developed and deployed independently
- **Better Scalability**: Individual features can be scaled based on demand
- **Improved Maintainability**: Easier to maintain and extend functionality

## Architecture Structure

```
src/
├── Features/
│   ├── Products/
│   │   ├── GetProduct/
│   │   │   ├── ProductsController.cs
│   │   │   ├── GetProductQuery.cs
│   │   │   └── GetProductHandler.cs
│   │   ├── CreateProduct/
│   │   │   ├── CreateProductCommand.cs
│   │   │   └── CreateProductHandler.cs
│   │   └── ...
│   ├── Orders/
│   │   ├── GetOrder/
│   │   ├── CreateOrder/
│   │   └── ...
│   └── Users/
│       ├── GetUser/
│       ├── CreateUser/
│       └── ...
├── Infrastructure/
│   └── Data/
│       └── ApplicationDbContext.cs
├── Shared/
│   └── Entities/
│       ├── Product.cs
│       ├── Order.cs
│       └── User.cs
└── Program.cs
```

## Key Components

### 1. Features Organization
Each feature is organized in its own folder containing:
- **Controller**: HTTP endpoints for the feature
- **Query/Command**: Request/response models
- **Handler**: Business logic implementation
- **Validator**: Input validation logic (when needed)

### 2. MediatR Integration
- Uses MediatR for request/response handling
- Provides clean separation between controllers and business logic
- Enables cross-cutting concerns through behaviors

### 3. Entity Framework Core
- Database access through Entity Framework Core
- Shared DbContext for all features
- Optimized queries per feature needs

## Implementation Examples

### Product Feature - Get Product

**Controller:**
```csharp
[HttpGet("{id}")]
public async Task<ActionResult<GetProductResponse>> GetProduct(int id)
{
    var query = new GetProductQuery { Id = id };
    var result = await _mediator.Send(query);
    
    if (result == null)
        return NotFound();
        
    return Ok(result);
}
```

**Query:**
```csharp
public class GetProductQuery : IRequest<GetProductResponse>
{
    public int Id { get; set; }
}
```

**Handler:**
```csharp
public async Task<GetProductResponse?> Handle(GetProductQuery request, CancellationToken cancellationToken)
{
    var product = await _context.Products
        .AsNoTracking()
        .FirstOrDefaultAsync(p => p.Id == request.Id, cancellationToken);

    return product == null ? null : new GetProductResponse
    {
        Id = product.Id,
        Name = product.Name,
        // ... other properties
    };
}
```

## Getting Started

### Prerequisites
- .NET 8 SDK
- SQL Server (or SQL Server LocalDB)
- Visual Studio or VS Code

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd software/vertical_slice_architecture/src
   ```

2. **Restore packages**
   ```bash
   dotnet restore
   ```

3. **Update database connection**
   Update the connection string in `appsettings.json`:
   ```json
   {
     "ConnectionStrings": {
       "DefaultConnection": "Your connection string here"
     }
   }
   ```

4. **Create and run migrations**
   ```bash
   dotnet ef migrations add InitialCreate
   dotnet ef database update
   ```

5. **Run the application**
   ```bash
   dotnet run
   ```

6. **Access Swagger UI**
   Navigate to `https://localhost:5001/swagger` to explore the API

## Testing Strategy

### Unit Testing
- Test handlers independently
- Mock external dependencies
- Focus on business logic validation

### Integration Testing
- Test complete feature flows
- Use in-memory database or test containers
- Validate API endpoints end-to-end

### Example Test Structure
```
tests/
├── Features/
│   ├── Products/
│   │   ├── GetProductHandlerTests.cs
│   │   └── CreateProductHandlerTests.cs
│   └── Orders/
│       └── GetOrderHandlerTests.cs
└── Integration/
    ├── ProductsControllerTests.cs
    └── OrdersControllerTests.cs
```

## Best Practices

### 1. Feature Independence
- Minimize dependencies between features
- Use shared entities sparingly
- Prefer duplication over coupling

### 2. Database Access
- Use specific projections for read operations
- Optimize queries for each feature's needs
- Consider separate read/write models

### 3. Validation
- Validate inputs at the command/query level
- Use FluentValidation for complex validation rules
- Fail fast with clear error messages

### 4. Error Handling
- Use consistent error response formats
- Handle exceptions at the feature level
- Provide meaningful error messages

### 5. Performance Considerations
- Use AsNoTracking() for read operations
- Implement caching where appropriate
- Monitor and optimize query performance

## Common Patterns

### 1. CQRS (Command Query Responsibility Segregation)
- Separate read and write operations
- Optimize each operation independently
- Use different models for commands and queries

### 2. Repository Pattern (Optional)
- Consider for complex data access scenarios
- Implement per feature if needed
- Keep repositories focused and lightweight

### 3. Domain Events
- Use for cross-feature communication
- Maintain feature independence
- Handle eventually consistent scenarios

## Migration from Layered Architecture

### Step-by-Step Approach
1. **Identify Features**: Map existing functionality to business features
2. **Create Feature Folders**: Organize code by features instead of layers
3. **Move Controllers**: Group controllers with their related logic
4. **Refactor Services**: Convert services to handlers
5. **Update Data Access**: Optimize queries per feature needs

### Common Challenges
- **Shared Code**: Decide what to share vs. duplicate
- **Cross-Feature Communication**: Use domain events or API calls
- **Database Design**: Balance normalization with feature independence
- **Team Organization**: Align team structure with feature boundaries

## Advanced Topics

### 1. Feature Flags
- Enable/disable features dynamically
- A/B testing capabilities
- Gradual feature rollouts

### 2. Microservices Evolution
- Features can evolve into microservices
- Clear boundaries already established
- Easier service extraction

### 3. Event-Driven Architecture
- Use domain events for cross-feature communication
- Maintain loose coupling between features
- Support eventual consistency patterns

## Resources

### Books
- "Building Evolutionary Architectures" by Neal Ford
- "Microservices Patterns" by Chris Richardson
- "Clean Architecture" by Robert C. Martin

### Articles
- [Vertical Slice Architecture by Jimmy Bogard](https://jimmybogard.com/vertical-slice-architecture/)
- [CQRS and MediatR in .NET](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/apply-simplified-microservice-cqrs-ddd)

### Tools
- [MediatR](https://github.com/jbogard/MediatR) - Simple mediator pattern implementation
- [FluentValidation](https://fluentvalidation.net/) - Validation library for .NET
- [Entity Framework Core](https://docs.microsoft.com/en-us/ef/core/) - Object-database mapper

## Contributing

When adding new features:
1. Create a new folder under `Features/`
2. Follow the established patterns
3. Include appropriate tests
4. Update documentation

## License

This project is licensed under the MIT License - see the [LICENSE](../../../LICENSE) file for details.