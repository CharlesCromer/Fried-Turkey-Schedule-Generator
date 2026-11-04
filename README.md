# Fried Turkey Schedule Generator 🦃

A simple, interactive Python program that works backward from your planned meal time to build a deep-fried turkey preparation and cooking schedule.

Enter **when you want to serve dinner** and **the weight of your turkey**, and the program calculates when to begin preparation, heat the oil, start frying, check the turkey's temperature, and carve. The schedule appears in the terminal and is saved to a printable text file.

Originally created by **Charles Cromer** in 2020.

## Features

- Calculates a preparation timeline based on your desired serving time.
- Accepts turkey weights from **5 to 30 pounds** (whole pounds only).
- Estimates a frying-time window of **3–3.5 minutes per pound**.
- Includes time for preparation, fryer setup, oil heating, and resting.
- Displays times in a familiar 12-hour AM/PM format.
- Saves the generated schedule to **`Turkey Timer.txt`** in the current working directory.
- Allows you to generate another schedule without restarting the program.
- Uses only Python's standard library; no external packages are required.

## Requirements

- Python 3
- A terminal or command prompt

## Getting started

Clone the repository:

```bash
git clone https://github.com/CharlesCromer/Fried-Turkey-Schedule-Generator.git
cd Fried-Turkey-Schedule-Generator
```

Run the script:

**Windows**

```powershell
py "Turkey Timer.py"
```

**macOS / Linux**

```bash
python3 "Turkey Timer.py"
```

Alternatively, download `Turkey Timer.py` and run it directly from a terminal. No installation beyond Python is necessary.

## How to use

1. Enter the time you plan to serve the turkey in `H:MMam` or `H:MMpm` format, such as `3:00pm`.
2. Enter the turkey's weight in whole pounds, such as `15`.
3. Read the schedule displayed in the terminal.
4. Open **`Turkey Timer.txt`** in the directory from which you ran the script to view or print the schedule.
5. At the prompt `Run Again? [y/n]:`, enter `y` to make another schedule or `n` to exit.

### Example

For a **15-pound turkey** with a **3:00pm** serving time, the code's scheduling formulas produce the following approximate timeline on a fresh run:

| Time | Activity |
| --- | --- |
| 11:48am | Remove turkey from refrigerator; begin preparation and seasoning |
| 12:18pm | Prepare fryer and oil |
| 12:33pm | Start heating oil |
| 1:33pm | Put turkey in oil |
| 2:18pm | Begin checking internal temperature (45-minute minimum estimate) |
| 2:25pm | Maximum estimated fry-time endpoint (52 minutes) |
| 2:45pm | Begin carving according to the program's schedule |

The program also prints additional instructions about checking doneness and resting the turkey. **These times are estimates, not a substitute for checking food temperature or following fryer safety instructions.**

## How the schedule is calculated

The original program uses these assumptions:

| Stage | Estimated duration |
| --- | ---: |
| Initial preparation and seasoning | 30 minutes |
| Fryer and oil setup | 15 minutes |
| Oil heating | 60 minutes |
| Frying | 3–3.5 minutes per pound |
| Final scheduled resting period | 20 minutes |

It calculates the first task by subtracting **140 minutes plus the maximum estimated frying time** from your chosen serving time. The extra 15 minutes beyond the listed preparation, heating, and resting stages acts as a scheduling buffer.

For example, a 15-pound turkey has an estimated frying window of **45–52 minutes** because the program truncates fractional minutes to whole numbers.

## Important safety information

> **Food safety:** The original 2020 script tells users to remove the turkey at 160°F and assumes carryover cooking will raise it by 10°F. Do **not** rely on that assumption. Current USDA guidance recommends that poultry reach a safe internal temperature of **165°F (74°C)**, verified with a food thermometer in the thickest parts. Cooking time varies with bird size, temperature, equipment, and conditions.

Deep-frying a turkey can cause serious burns or fires. Use a fryer according to the manufacturer's instructions, **never fry a frozen or wet turkey**, keep the fryer outdoors and away from structures, avoid overfilling with oil, and never leave hot oil unattended. Consult current food-safety and fire-safety guidance before cooking.

This project is a **planning aid**, not an automated safety monitor or validated cooking guide.

## Known limitations

The README documents the original script as provided; the following issues have **not** been fixed in the source code:

- **Repeat runs:** The accumulated preparation time is initialized before the repeat loop, so generating a second schedule in the same session can produce incorrect times. Restart the script for each new schedule until this is fixed.
- **Invalid weight input:** Although the script attempts to validate weight, some nonnumeric input can still cause a `ValueError` instead of prompting again.
- **Midnight crossover:** The time-formatting logic does not reliably handle schedules that cross midnight.
- **Fixed assumptions:** Heating, preparation, frying, and rest periods are hard-coded and do not account for fryer design or actual cooking conditions.
- **Outdated temperature messages:** The script prints older temperature guidance. Follow the updated food-safety guidance above rather than those messages.
- **File overwrite:** Each run overwrites the existing `Turkey Timer.txt` output.

## Project structure

```text
Fried-Turkey-Schedule-Generator/
├── Turkey Timer.py       # Interactive schedule generator
├── README.md             # Project documentation
├── .gitignore
├── .gitattributes
└── Turkey Timer.txt      # Generated after running the script
```

## License

The source code header states that this project was released under the **GNU General Public License (GPL)**. The specific GPL version is not stated in the provided source. Before redistributing or accepting contributions, add a `LICENSE` file identifying the intended GPL version.

## Author

**Charles Cromer**  
Panama City, Florida, USA  
Email: [charles.cromer@gmail.com](mailto:charles.cromer@gmail.com)  
GitHub: [CharlesCromer](https://github.com/CharlesCromer)

Feedback and suggestions are welcome.
