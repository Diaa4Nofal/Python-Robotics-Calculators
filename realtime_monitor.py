import time # مكتبة للتحكم في الوقت

def start_monitoring():
    print("🚀 Robot System Initialized...")
    print("Monitoring temperature in real-time (Press Ctrl+C to stop)")
    
    # محاكاة لبيانات المستشعر
    dummy_sensor_data = [50, 55, 65, 75, 85, 90] 
    
    for temp in dummy_sensor_data:
        print(f"\nChecking Sensor... Current Temp: {temp}°C")
        
        if temp > 80:
            print("❌ CRITICAL: Overheating detected! Shutdown initiated.")
            break # توقف تماماً عند الخطر
        elif temp > 60:
            print("⚠️ WARNING: High temperature. Cooling fan started.")
        else:
            print("✅ Status: Normal")
        
        time.sleep(1) # انتظر ثانية واحدة قبل القراءة التالية

start_monitoring()
