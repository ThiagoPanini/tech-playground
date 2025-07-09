using MediatR;
using Microsoft.AspNetCore.Mvc;

namespace VerticalSliceArchitecture.Features.Users.GetUser;

[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase
{
    private readonly IMediator _mediator;

    public UsersController(IMediator mediator)
    {
        _mediator = mediator;
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<GetUserResponse>> GetUser(int id)
    {
        var query = new GetUserQuery { Id = id };
        var result = await _mediator.Send(query);
        
        if (result == null)
            return NotFound();
            
        return Ok(result);
    }
}

public class GetUserQuery : IRequest<GetUserResponse>
{
    public int Id { get; set; }
}

public class GetUserResponse
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public DateTime CreatedAt { get; set; }
    public int TotalOrders { get; set; }
}