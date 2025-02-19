# 🤖 Mars-Rover-Solution

## ❓ Problem  

A squad of robotic rovers is to be landed by NASA on a plateau on Mars. This plateau, which is rectangular, must be navigated by the rovers so that their onboard cameras can capture a complete view of the surrounding terrain to send back to Earth.

A rover's position and location are represented by a combination of **x** and **y** coordinates and a letter representing one of the four cardinal compass points. The plateau is divided into a grid to simplify navigation. An example position might be `0 0 N`, meaning the rover is in the bottom-left corner facing **North**.

To control a rover, NASA sends a simple string of commands. The possible commands are:

- **`L`** (rotate 90° left)
- **`R`** (rotate 90° right)
- **`M`** (move forward one grid point in the current direction)

Assume that the square directly **North** of `(x, y)` is `(x, y+1)`.

## 🚀 Features  

- Simulates one or multiple rovers moving on a plateau.
- Prevents rovers from moving outside the plateau.
- Accepts both **uppercase and lowercase** movement commands (`L`, `R`, `M`).
- Allows the user to stop adding rovers by pressing **Enter**.

## 🔧 Installation  

1. Ensure you have **Python** installed.
2. Clone this repository:
   ```sh
   git clone https://github.com/Nataliaqg/Mars-Rover-Solution.git
   ```
3. Navigate to the project directory:
   ```sh
   cd mars-rover-solution
   ```
4. Run the program:
   ```sh
   python rovers.py
   ```

## 📌 Usage  

The program requires user input to define the **plateau size**, **rover positions**, and **movement commands**.

### Example Input
```sh
Enter the plateau dimensions: 5 5
Enter the rovers location: 1 2 N
Enter the movement commands: LMLMLMLMM
Enter the next rovers location or press Enter to display the result: 3 3 E
Enter the movement commands: MMRMMRMRRM
```
### Example Output
```sh
Final rover positions:
1 3 N
5 1 E
```

## 📞 Contact

If you have any questions or suggestions, feel free to reach out:

📧 **Email:** [nataliaquirogag@gmail.com](mailto:nataliaquirogag@gmail.com)

---

## 🙌 Acknowledgment

Thank you for taking the time to check out this project! I truly appreciate your interest and support.