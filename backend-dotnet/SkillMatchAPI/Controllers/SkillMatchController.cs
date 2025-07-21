using Microsoft.AspNetCore.Mvc;
using SkillMatchAPI.Models;



namespace SkillMatchAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class SkillMatchController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public SkillMatchController(IHttpClientFactory httpClientFactory)
        {
            _httpClient = httpClientFactory.CreateClient();
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] SkillInput request)
        {
            Console.WriteLine("Received request with skills: " + request.skills);
            try
            {
                var response = await _httpClient.PostAsJsonAsync("http://127.0.0.1:8000/predict", request);
                Console.WriteLine("Sent request to Python server");

                var result = await response.Content.ReadFromJsonAsync<PredictionResponse>();
                Console.WriteLine("Received from Python: " + result?.role);

                return Ok(result);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
                return StatusCode(500, "Internal Server Error");
            }
        }
    }
}