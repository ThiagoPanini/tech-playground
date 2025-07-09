using MediatR;
using Microsoft.EntityFrameworkCore;
using VerticalSliceArchitecture.Infrastructure.Data;

namespace VerticalSliceArchitecture.Features.Orders.GetOrder;

public class GetOrderQuery : IRequest<GetOrderResponse>
{
    public int Id { get; set; }
}

public class GetOrderResponse
{
    public int Id { get; set; }
    public int UserId { get; set; }
    public string UserName { get; set; } = string.Empty;
    public DateTime OrderDate { get; set; }
    public decimal TotalAmount { get; set; }
    public string Status { get; set; } = string.Empty;
    public List<OrderItemResponse> Items { get; set; } = new();
}

public class OrderItemResponse
{
    public int ProductId { get; set; }
    public string ProductName { get; set; } = string.Empty;
    public int Quantity { get; set; }
    public decimal UnitPrice { get; set; }
    public decimal TotalPrice { get; set; }
}

public class GetOrderHandler : IRequestHandler<GetOrderQuery, GetOrderResponse?>
{
    private readonly ApplicationDbContext _context;

    public GetOrderHandler(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<GetOrderResponse?> Handle(GetOrderQuery request, CancellationToken cancellationToken)
    {
        var order = await _context.Orders
            .AsNoTracking()
            .Include(o => o.User)
            .Include(o => o.OrderItems)
            .ThenInclude(oi => oi.Product)
            .FirstOrDefaultAsync(o => o.Id == request.Id, cancellationToken);

        if (order == null)
            return null;

        return new GetOrderResponse
        {
            Id = order.Id,
            UserId = order.UserId,
            UserName = order.User.Name,
            OrderDate = order.OrderDate,
            TotalAmount = order.TotalAmount,
            Status = order.Status,
            Items = order.OrderItems.Select(oi => new OrderItemResponse
            {
                ProductId = oi.ProductId,
                ProductName = oi.Product.Name,
                Quantity = oi.Quantity,
                UnitPrice = oi.UnitPrice,
                TotalPrice = oi.TotalPrice
            }).ToList()
        };
    }
}