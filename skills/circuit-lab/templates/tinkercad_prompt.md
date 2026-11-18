You are in Tinkercad Circuits (an empty circuit editor is open). Work ONLY in this tab. Do not open other sites and do not type any passwords.

GOAL
Build <project / part> on one full-size breadboard. I will copy it onto a physical breadboard, so hole positions must be exact.

SETUP
Rename the circuit "<name>". Place one full-size breadboard and use the PRINTED column numbers (1–62). Place a "Power Supply" set to <V> (current limit 1A). Red wire from + to the top + rail, black wire from − to the top − rail.

RULES
- Use the top half (rows a–e) and the top rails. Wire colors: red for +V, black for GND, orange to extend a node to another column.
- Diodes: BAND = cathode. LEDs: set the color in the Inspector; anode = the bent leg.
- Diodes and resistors have fixed leads exactly 4 columns apart. The layout below already respects this.
- Pushbuttons straddle the center gap, with their top legs in row e at the given columns.
- Set every resistor value in the Inspector right after placing it, then re-check it.
- If a rail column has no hole, jumper diagonally to the nearest rail hole.

LAYOUT (column: contents)
<block by block>

EXECUTION
Build <block 1> first. Start the simulation and test: <expected>. If it fails, STOP and tell me what you see. Then build each remaining block and test it:
<tests per block>
To test two buttons at once: put a temporary jumper across button A's two columns, press B, then delete the jumper.
If the same step fails 3 times, STOP and report.

FINAL REPORT (in this chat), exactly this format:
1. Circuit URL
2. Deviations from the layout (table, with exact holes)
3. Test results (block × state, with LED brightness %)
4. Build list: POWER first, then block by block, in this format:
   Part | value/color | leg 1 hole | leg 2 hole | note
   - Mark (BAND) on the diode leg that has the band, and (ANODE) on the LED anode.
   - For pushbuttons, give only the 2 top-leg holes in row e.
   - Write rail holes as "+rail col X" / "−rail col X".
5. Totals of every part type
6. What was hard
