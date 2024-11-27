# DISTANCE-DETECTION
# **Distance Detection System** 

## **Objective**  
The **DISTANCE EYE** project focuses on measuring the distance between an object and an ultrasonic sensor (e.g., HC-SR04). It uses a Raspberry Pi as the central processing unit to detect and measure distance accurately. This system can trigger alerts or initiate predefined actions based on the detected distance, making it ideal for obstacle detection, automated parking systems, and proximity-based alerts.

---

## **Problem Statement**  
With increasing automation in industries, smart homes, and vehicles, precise distance measurement plays a crucial role in improving safety and efficiency. However, existing solutions often face challenges such as:  

- **High implementation costs.**  
- **Accuracy issues due to environmental interference.**  
- **Lack of customization for specific use cases.**  

This project provides a cost-effective and reliable distance detection system using an ultrasonic sensor and Raspberry Pi to overcome these challenges.

---

## **Hardware Components**  

### **1. Raspberry Pi 3/4**  
**Features:** Quad-core ARM CPU, 1GB+ RAM, Wi-Fi, Bluetooth, and GPIO pins.  
**Purpose:** Serves as the processing unit for reading data from the ultrasonic sensor and executing distance measurement logic.  

### **2. Ultrasonic Sensor (e.g., HC-SR04)**  
**Function:** Measures the distance of an object by transmitting and receiving ultrasonic waves.  
**Integration:** Connected to Raspberry Pi GPIO pins for real-time data input.  

### **3. LED/Buzzer Indicators**  
**Purpose:** Provide visual or audible feedback upon detecting objects within a predefined distance threshold.  

---

## **Software**  

**Programming Language:** Python  

### **Libraries Used:**  
- **RPi.GPIO:** For controlling Raspberry Pi GPIO pins.  
- **time:** For time-related operations like delays.  
- **os:** For executing system-level commands.  
- **smtplib:** For sending email notifications (optional).  

---

## **Circuit Design**  
- **Raspberry Pi GPIO pins** connected to the **ultrasonic sensor (HC-SR04)** for distance measurement.  
- **LED or buzzer** connected to an output GPIO pin for visual or audible alerts.  

---

## **Features**  
1. **Real-time Distance Measurement:**  
   - Uses the ultrasonic sensor to measure the distance of nearby objects.  
   
2. **Visual/Audible Alerts:**  
   - Triggers an LED or buzzer when an object is detected within a specified range.  

3. **Customizable Threshold:**  
   - Users can set a custom distance threshold for triggering alerts.  

4. **Notification System (Optional):**  
   - Sends alerts to the user's email or device if the object is within a critical distance.  

---

## **Setup Instructions**  
1. **Assemble the components** according to the provided circuit diagram.  
2. **Flash the Raspberry Pi** with a compatible OS (e.g., Raspbian).  
3. **Install necessary Python libraries:**  
   ```bash
   sudo apt-get install python3-rpi.gpio
   sudo apt-get install python3-smtplib
   ```  
4. **Clone the project repository:**  
   ```bash
   git clone <repository-url>
   cd DISTANCE-EYE
   ```  
5. **Run the script:**  
   ```bash
   python3 distance_detection.py
   ```  

---

## **Code Overview**  

### **Main Logic:**  
- Set up GPIO pins for the **ultrasonic sensor (input)** and **LED/Buzzer (output)**.  
- Continuously monitor the ultrasonic sensor for distance measurements.  
- If the measured distance falls below the threshold:  
  - Trigger the LED or buzzer.  
  - Optionally, send an email notification.  

---

## **Applications**  
- **Obstacle Detection for Autonomous Vehicles:** Prevents collisions by measuring distances to nearby objects.  
- **Parking Assistance:** Guides drivers by detecting nearby obstacles during parking.  
- **Industrial Safety:** Alerts operators about objects in restricted zones.  
- **Smart Homes:** Proximity-based automation, such as opening doors or turning on lights.  

---

## **Future Enhancements**  
1. **AI-powered Predictions:**  
   - Use machine learning to predict object trajectories based on distance and time data.  
   
2. **Integration with IoT Platforms:**  
   - Send distance data to cloud platforms for advanced monitoring and analytics.  
   
3. **Advanced Alerts:**  
   - Customize alerts using push notifications or SMS.  

---

## **Acknowledgments**  
This project leverages the power of **Raspberry Pi** and **ultrasonic sensors** to create a reliable, affordable distance detection system suitable for multiple applications.

---

## **Contributors**  
1) Siddhima Singh : [GitHub](https://github.com/siddhima-singh)
2) Aastha Kothari : [GitHub](https://github.com/AASTHAKOTHAR)
3) Lakshya Sharma : [GitHub](https://github.com/lakshya603)
