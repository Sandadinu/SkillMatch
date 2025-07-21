// File: Models/SkillModels.cs
namespace SkillMatchAPI.Models
{
    public class SkillInput
    {
        public string? skills { get; set; }
    }

    public class PredictionResponse
    {
        public string? role { get; set; }
    }
}
