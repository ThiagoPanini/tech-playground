# Vertical Slice Architecture Example

This directory contains a complete implementation of Vertical Slice Architecture using .NET 8.

## Quick Start

1. Navigate to the src directory:
   ```bash
   cd software/vertical_slice_architecture/src
   ```

2. Restore packages:
   ```bash
   dotnet restore
   ```

3. Run the application:
   ```bash
   dotnet run
   ```

4. Open your browser and navigate to: `https://localhost:5001/swagger`

## Features Implemented

### Products
- Get Product by ID
- Create Product

### Orders  
- Get Order by ID (with related data)

### Users
- Get User by ID (with order count)

## Architecture Benefits Demonstrated

1. **Feature Independence**: Each feature folder contains all related code
2. **Clear Boundaries**: Minimal sharing between features
3. **Testability**: Each handler can be tested independently
4. **Maintainability**: Easy to locate and modify feature-specific code
5. **Scalability**: Features can be developed by different teams

## Next Steps

- Add validation using FluentValidation
- Implement remaining CRUD operations
- Add integration tests
- Implement cross-cutting concerns (logging, caching, etc.)
- Add authentication and authorization