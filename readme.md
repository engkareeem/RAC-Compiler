# RAC (Robotic Arm Compiler)

RAC (Robotic Arm Compiler) is a custom compiler built in Python designed specifically for controlling robotic arms using a high-level language. The compiler takes high-level code, parses it, and converts it into an Abstract Syntax Tree (AST), which is then transformed into a JSON representation for further use. RAC supports custom robotic arm commands such as `__setArm` and handles control flow constructs like loops and conditionals.

## Features
- **High-Level Syntax**: Write robotic arm control programs in an easy-to-read, high-level language.
- **Custom Commands**: Includes specific commands like `__setArm` and `__delay` for robotic arm operations.
- **JSON Output**: Transforms the parsed AST into JSON for easy integration with other systems.
- **Control Flow Support**: Includes support for constructs like `if`, `while`, and variable declarations.

# Dependencies

- Python 3.x
- rply
- `pyperclip` (optional, for clipboard functionality)
- Custom modules:
  - `lexer`
  - `parser`
  - `codegen`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/engkareeem/RAC-Compiler.git
   cd rac
   ```

2. Install dependencies:
   ```bash
   pip install pyperclip
   pip install rply
   ```

3. Run the sample code:
   ```bash
   python compiler.py
   ```

## Usage

- Write your robotic arm program in the custom high-level syntax.
- Use RAC to compile the program into a JSON representation.
- Integrate the JSON with your robotic arm control system.


## Example Code

Below is an example of the high-level code RAC can compile:

```
function test() {
    __setArm(1, 2, 3, 4, 5);
}
number x = 0;
bool flag = 1;

while (true) {
    test();
    if (flag) {
        x = x + 1;
    } else {
        x = x - 1;
    }
    if (flag >= 10) {
        flag = false;
    }
    __set_arm(x, 10, 0);
    __delay(100);
}
```

## How It Works

1. **Lexical Analysis**: The `Lexer` tokenizes the input code into a stream of tokens.
2. **Parsing**: The `Parser` generates an AST from the tokenized code.
3. **Code Generation**: The AST is converted into a JSON representation using `ast_to_json`.
4. **Output**: The resulting JSON can be used to drive the robotic arm or as an intermediate step in a larger pipeline.

## Supported Commands

### **1. digitalWrite(pin, state)**
- **Description:** Sets the specified digital pin to either `HIGH` or `LOW`.
- **Parameters:**
  - `pin`: The pin number to which you want to write (e.g., 2, 3, 13).
  - `state`: The state to set the pin to; use `true` for `HIGH` and `false` for `LOW`.
- **Example Usage:**
  ```
  digitalWrite(13, true);  // Set pin 13 to HIGH
  digitalWrite(13, false); // Set pin 13 to LOW
  ```

### **2. digitalRead(pin)**
- **Description:** Reads the current state of a specified digital pin.
- **Parameters:**
  - `pin`: The pin number to read (e.g., 2, 3, 13).
- **Returns:** `true` if the pin is `HIGH`, `false` if the pin is `LOW`.
- **Example Usage:**
  ```
  bool state = digitalRead(13); // Read state of pin 13
  ```

### **3. analogWrite(pin, value)**
- **Description:** Writes an analog value (PWM wave) to a specified pin.
- **Parameters:**
  - `pin`: The pin number to which you want to write.
  - `value`: The duty cycle of the PWM signal (0-255).
- **Example Usage:**
  ```
  analogWrite(9, 128);  // Set PWM value of pin 9 to 128
  ```

### **4. analogRead(pin)**
- **Description:** Reads the value from the specified analog pin.
- **Parameters:**
  - `pin`: The analog pin number to read.
- **Returns:** A number between 0 and 1023.
- **Example Usage:**
  ```
  int sensorValue = analogRead(A0); // Read analog value from pin A0
  ```

### **5. delay(milliseconds)**
- **Description:** Pauses the program for the specified number of milliseconds.
- **Parameters:**
  - `milliseconds`: The number of milliseconds to delay.
- **Example Usage:**
  ```
  delay(1000);  // Pause for 1 second
  ```

### **6. print(number)**
- **Description:** Prints a number to the serial monitor (string output is not supported).
- **Parameters:**
  - `number`: The number to print.
- **Example Usage:**
  ```
  print(42); // Prints the number 42 to the serial monitor
  ```

### **7. setArm(x, y, z)**
- **Description:** Sets the robotic arm’s position in 3D space.
- **Parameters:**
  - `x`: X-coordinate.
  - `y`: Y-coordinate.
  - `z`: Z-coordinate.
- **Example Usage:**
  ```
  setArm(10, 20, 30); // Move arm to (10, 20, 30)
  ```

### **8. setArmSpeed(speed)**
- **Description:** Changes the arm speed (0-255).
- **Parameters:**
  - `speed`: Speed (0-255).
- **Example Usage:**
  ```
  setArmSpeed(100);  // Changing arm speed to 100
  ```

### **9. setWrist(angle[, speed])**
- **Description:** Sets the wrist's angle and speed.
- **Parameters:**
  - `angle`: The angle to set the wrist.
  - `speed`: Wrist speed (0-255), optional.
- **Example Usage:**
  ```
  setWrist(45, 10);  // Set wrist to 45 degrees at speed 10
  ```

### **10. autoWrist()**
- **Description:** Automatically adjusts the wrist angle relative to the shoulder and elbow positions.
- **Example Usage:**
  ```
  autoWrist(); // Adjust wrist based on shoulder and elbow
  ```

### **11. rotateWrist(angle[, speed])**
- **Description:** Rotates the wrist to the specified angle.
- **Parameters:**
  - `angle`: The angle to rotate the wrist to.
  - `speed`: Rotating speed (0-255), optional.
- **Example Usage:**
  ```
  rotateWrist(90);  // Rotate wrist to 90 degrees
  ```

### **12. openGripper()**
- **Description:** Opens the robotic gripper.
- **Example Usage:**
  ```
  openGripper();  // Open the gripper
  ```

### **13. closeGripper()**
- **Description:** Closes the robotic gripper.
- **Example Usage:**
  ```
  closeGripper();  // Close the gripper
  ```

### **14. forceCloseGripper(speed)**
- **Description:** Closes the robotic gripper without considering the gripper strength.
- **Parameters:**
  - `speed`: Closing speed (0-255).
- **Example Usage:**
  ```
  forceCloseGripper(100);  // Close the gripper with speed 100
  ```

### **15. forceOpenGripper(speed)**
- **Description:** Opens the robotic gripper without considering the gripper strength.
- **Parameters:**
  - `speed`: Opening speed (0-255).
- **Example Usage:**
  ```
  forceOpenGripper(100);  // Open the gripper with speed 100
  ```

### **16. wait()**
- **Description:** Waits for the arm to stop moving.

---

Happy coding with RAC! 🚀
