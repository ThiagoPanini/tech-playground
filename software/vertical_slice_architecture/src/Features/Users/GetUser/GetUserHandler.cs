using MediatR;
using Microsoft.EntityFrameworkCore;
using VerticalSliceArchitecture.Infrastructure.Data;

namespace VerticalSliceArchitecture.Features.Users.GetUser;

public class GetUserHandler : IRequestHandler<GetUserQuery, GetUserResponse?>
{
    private readonly ApplicationDbContext _context;

    public GetUserHandler(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<GetUserResponse?> Handle(GetUserQuery request, CancellationToken cancellationToken)
    {
        var user = await _context.Users
            .AsNoTracking()
            .Select(u => new GetUserResponse
            {
                Id = u.Id,
                Name = u.Name,
                Email = u.Email,
                CreatedAt = u.CreatedAt,
                TotalOrders = u.Orders.Count()
            })
            .FirstOrDefaultAsync(u => u.Id == request.Id, cancellationToken);

        return user;
    }
}