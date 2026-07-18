🤖 Arduino 4-Servo Sweep & Hold System
This repository contains an implementation of an automated multi-servo control system using an Arduino Uno. The project was developed as a technical task for the Smart Methods training program.

📋 Project Objective
The goal is to program 4 micro servo motors to execute two sequential movement phases:

Sweep Phase (First 2 Seconds): All 4 servo motors continuously rotate back and forth (Sweep mode) simultaneously.
Hold Phase (Post 2 Seconds): Immediately after the 2-second mark, all motors stop swinging and lock firmly at a 90-degree angle.
🛠️ Hardware & Wiring Layout
The circuit is fully simulated on Tinkercad Circuits with an optimized layout using shared power rails for standard logic verification.

Pin Mapping Table
Component	Servo Pin	Arduino Pin	Wire Color
Servo 1	Signal / Power / GND	Pin 3 (PWM) / 5V / GND	Orange / Red / Brown
Servo 2	Signal / Power / GND	Pin 5 (PWM) / 5V / GND	Orange / Red / Brown
Servo 3	Signal / Power / GND	Pin 6 (PWM) / 5V / GND	Orange / Red / Brown
Servo 4	Signal / Power / GND	Pin 9 (PWM) / 5V / GND	Orange / Red / Brown
⚠️ Hardware Note: In physical deployments, an external 5V power supply must be used to power the 4 servos to prevent overcurrent resets on the Arduino regulator, ensuring a common ground layout is maintained.

🚀 Simulation Demo
Here is the automated execution behavior of the system:
https://github.com/Mona-CS90/SmartMethods_SummerTraining_Tasks/blob/main/03-Electronics-and-Electrical/Design_4%20Servo_Motors/simulation.gif


💻 Source Code
The firmware is written in C++ utilizing the standard Servo.h library and non-blocking time delta tracking through millis() to handle the strict 2-second phase transitions.

#include <Servo.h>

// Instantiating 4 servo controller objects
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

unsigned long startTime;
const unsigned long sweepDuration = 2000; // Phase 1 duration in milliseconds (2 seconds)

int angle = 0; 
int direction = 1; // 1 for incrementing, -1 for decrementing angle

void setup() {
  // Attach servos to selected PWM-capable pins
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);
  
  // Cache simulation start time
  startTime = millis();
}

void loop() {
  // Compute elapsed delta time
  unsigned long currentTime = millis() - startTime;

  if (currentTime < sweepDuration) {
    // Phase 1: Synchronized Sweep Action
    servo1.write(angle);
    servo2.write(angle);
    servo3.write(angle);
    servo4.write(angle);
    
    angle += direction * 5; 
    
    // Reverse movement bounds
    if (angle >= 180 || angle <= 0) {
      direction = -direction;
    }
    delay(15); // Smooth step transition delay
  } 
  else {
    // Phase 2: Immediate Lock at 90 Degrees
    servo1.write(90);
    servo2.write(90);
    servo3.write(90);
    servo4.write(90);
    
    // Halt further processing loop execution
    while(true) {
      // Infinite safe state loop
    }
  }
}
📥 Submission Artifacts
Simulation Environment: Tinkercad Circuits
Deliverables: High-fidelity implementation source code & explicit simulation video.
