"""
ContextFlow-AI: Carbon Footprint Awareness Platform
Focus: Smart tracking and personalized insights for sustainability.
"""

class CarbonFootprintAssistant:
    def __init__(self, user_name):
        self.user_name = user_name
        self.total_footprint = 0.0

    def calculate_impact(self, activity, duration_hours):
        """Logic: Simple impact calculation based on activity type."""
        # Mock carbon intensity factors (kg CO2 per hour)
        factors = {"driving": 2.5, "public_transit": 0.5, "remote_work": 0.1}
        intensity = factors.get(activity.lower(), 1.0)
        
        impact = intensity * duration_hours
        self.total_footprint += impact
        return f"Activity '{activity}' added. Added {impact}kg to your carbon footprint."

    def get_personalized_insight(self):
        """Logical decision-making for sustainability."""
        if self.total_footprint > 10:
            return "Your footprint is high. Try switching to public transit today!"
        return "Great job keeping your footprint low! Keep it up."

# Example Usage
if __name__ == "__main__":
    app = CarbonFootprintAssistant(user_name="User")
    print(app.calculate_impact("driving", 2))
    print(app.get_personalized_insight())
