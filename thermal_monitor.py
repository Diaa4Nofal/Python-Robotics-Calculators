# Robotics Thermal Monitoring System
# Part of AI & Robotics Engineering Training

current_temperature = 85  # الحرارة الحالية للمحرك بالسيلسيوس

print(f"Checking system status... Current Temp: {current_temperature}°C")

if current_temperature > 80:
    print("⚠️ ALERT: Temperature too high! Stopping motors...")
    print("Action: Engage Cooling System.")
elif current_temperature > 60:
    print("ℹ️ WARNING: Temperature rising. Reducing speed...")
else:
    print("✅ System OK: Temperature within safe limits.")
