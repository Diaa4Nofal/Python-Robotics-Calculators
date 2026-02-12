# Robotics Engineering Tool: Motor Efficiency Calculator
# Developed by: Diaa Nofal

def calculate_efficiency(input_power, output_power):
    """
    Calculates the efficiency of a robotic motor.
    Formula: (Output Power / Input Power) * 100
    """
    if input_power <= 0:
        return "Error: Input power must be greater than zero."
    
    efficiency = (output_power / input_power) * 100
    return f"Motor Efficiency: {efficiency:.2f}%"

# Input values (Example for a robot joint motor)
in_p = 150  # Power in Watts
out_p = 120 # Power in Watts

print("--- Robotics Engineering Diagnostic ---")
print(calculate_efficiency(in_p, out_p))
