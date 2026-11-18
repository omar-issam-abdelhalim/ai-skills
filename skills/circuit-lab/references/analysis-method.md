# Analysis Method

Use this for Phase 1, and whenever a measured value needs explaining.

## Contents
1. Models
2. Assume → Solve → Verify
3. Choosing the supply
4. Design checks (run all of them)
5. Worked patterns (diode logic)
6. How sources disagree
7. Writing calculations.md

## 1. Models

| Part | ON model | OFF model |
|---|---|---|
| Si diode (1N400x) | 0.7 V source (real: 0.65–0.75 V, rising with current) | open circuit |
| LED | Vf source | open circuit |
| Push button / switch | wire (pressed) | open (released) |
| Resistor | V = I·R | — |

LED Vf by color (typical at 5–20 mA):

| Color | Vf |
|---|---|
| Red | 1.8–2.0 V |
| Yellow | 2.0–2.1 V |
| Green (GaP, older type) | 2.0–2.2 V |
| Green (InGaN, true green) | 2.7–3.1 V |
| Blue / White | 2.8–3.2 V |

Proteus LED models use about 2.2 V and display ON/OFF only. Tinkercad shows graded brightness. Real LEDs glow visibly at 1 mA.

## 2. Assume → Solve → Verify

For each input state:
1. Assume ON/OFF for every diode and LED.
2. Replace each part with its model.
3. Write KCL at each unknown node (current in = current out) and solve.
4. Verify:
   - every ON diode has positive forward current
   - every OFF diode has V_anode − V_cathode < its threshold
   If a check fails, flip that assumption and re-solve.
5. Record:
   - the node voltage
   - every branch current
   - the LED state, and its current if it is ON

Floating input node (open switch, no pull-down): no current can flow through it, so its diode is OFF.

## 3. Choosing the supply (when the PDF doesn't state it)

Check, at the candidate voltage:
- worst-case LED current
- pull-down power when a button is pressed: P = V²/R. For 1/4 W parts, keep it ≤ 0.25 W.

Example: 9 V with 100 Ω pull-downs gives 0.81 W, which burns the resistor. 5 V gives 0.25 W, which is OK if the button is only pressed momentarily.

## 4. Design checks (run all of them, report each as PASS / RISK)

1. **LED current:** 5–20 mA when ON. Above 20 mA is a RISK, and the fix is a larger series resistor.
2. **Resistor power:** P = I²R or V²/R must be below the rating, in the worst state.
3. **Pull ratio (diode-AND / NAND):**
   V_low ≈ 0.7 + (Vcc − 0.7)·R_pd/(R_pd + R_pu).
   V_low must stay below the LED Vf with a margin of at least 0.3 V. Otherwise the LED glows faintly in an "OFF" state.
4. **OFF-state margin:** for every OFF LED, the voltage across the LED (plus its series resistor) must be at least 0.3 V below Vf. Within 0.3 V is a RISK: a faint glow on real hardware even if Proteus shows OFF.
5. **ON-state margin:** for every ON LED, the current must be at least 3 mA for every plausible Vf. Recompute with a high-Vf part, for example InGaN green or blue, and solve self-consistently: the node voltage shifts when the LED current shifts.
6. **Divider traps:** a pull-up plus pull-down on the same node fixes that node at the divider voltage when the diodes are off. Check that this voltage doesn't land in a margin zone. Example: in a diode-logic NAND project, R11 and R13 (1 k each) held Y2 at about 2.8 V, so the LED glowed. Removing R13 gave 5.00 V.
7. **Default values:** every resistor in Proteus/Tinkercad must be set explicitly, because the defaults are wrong (Proteus RES = 10 k).

## 5. Worked patterns (diode logic, Vcc = 5 V)

**Diode-OR** (diodes from the inputs to node X, R_pd from X to GND):
- X = max(inputs) − 0.7
- One input HIGH: X ≈ 4.3 V.
- Two inputs HIGH: X is slightly higher, because the current is shared between the diodes and each one drops less.

**Diode-AND** (R_pu from Vcc to Y; the diodes' cathodes face the inputs; each input has a pull-down):
- All LOW: (5 − Y)/R_pu = n·(Y − 0.7)/R_pd
- One LOW: (5 − Y)/R_pu = (Y − 0.7)/R_pd
- All HIGH: the diodes are OFF, and Y = the LED Vf if an LED goes from Y to GND (the LED clamps it).

**"Inverting" with an LED** (LED anode at Vcc, cathode at the node):
- The LED shows NOT(node), but the node itself still computes OR/AND.
- Diode logic cannot invert: a real NOT needs a transistor.
- Explain this in the learning pack, because it is a classic viva question.

**Measured reference** (diode-logic gates project, Vcc = 5 V, Proteus 8.13):

| Gate | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| OR | 0.00 | 4.26 | 4.26 | 4.29 |
| AND | 1.49 | 2.04 | 2.04 | 2.24 |
| NOR | 2.76 | 4.27 | 4.27 | 4.30 |
| NAND v1 (with R13) | 1.45 | 1.81 | 1.81 | 2.78 |
| NAND v2 (without R13) | — | — | — | 5.00 |

## 6. When sources disagree

Hand analysis, Proteus, Tinkercad and real hardware use different models:
- Proteus LED: ON/OFF threshold.
- Tinkercad: graded brightness, with one Vf per color.
- Real parts: different Vf from part to part.

When they disagree:
- go back to KCL with the actual numbers
- decide by worst case
- write the disagreement into the learning pack as a lesson

## 7. calculations.md format

For each block:
1. a short description of the topology
2. per state:
   - the assumptions
   - the KCL equation
   - the solution
   - the verification line
   - the LED current
3. a summary table: state → node V → LED
4. a "Risks" section with the design-check results

Show the algebra. The user must be able to redo it on paper.
