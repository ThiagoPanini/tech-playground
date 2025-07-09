using MediatR;
using Microsoft.EntityFrameworkCore;
using VerticalSliceArchitecture.Infrastructure.Data;

namespace VerticalSliceArchitecture.Features.Products.GetProduct;

public class GetProductHandler : IRequestHandler<GetProductQuery, GetProductResponse?>
{
    private readonly ApplicationDbContext _context;

    public GetProductHandler(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<GetProductResponse?> Handle(GetProductQuery request, CancellationToken cancellationToken)
    {
        var product = await _context.Products
            .AsNoTracking()
            .FirstOrDefaultAsync(p => p.Id == request.Id, cancellationToken);

        if (product == null)
            return null;

        return new GetProductResponse
        {
            Id = product.Id,
            Name = product.Name,
            Description = product.Description,
            Price = product.Price,
            Category = product.Category,
            CreatedAt = product.CreatedAt,
            UpdatedAt = product.UpdatedAt
        };
    }
}