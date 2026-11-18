# Tinkercad Playbook (built by a browser agent, verified by you)

## Who does what

- **The browser agent** (an AI agent running inside the user's browser) builds the circuit in Tinkercad. Assume it cannot read or write local files, so it reports everything in its chat.
- **You** (the local agent running this skill):
  - write the prompt
  - copy it to the clipboard
  - receive the report the user pastes back
  - verify it
  - produce `build_list.md`

## Tinkercad facts (verified)

- **Full breadboard:** 62 numbered columns (1–62), plus 2 unlabeled columns left of column 1. Always use the PRINTED numbers, and leave the unlabeled columns empty. Physical 830-point boards print 1–63, so a layout within 1–62 fits both.
- **Rails:** the outer top rail is −, the inner top rail is +. Rail holes come in groups of 5, and some columns have no rail hole above them (for example 18, 31, 61–62). Jumpers to the rail then go diagonally to the nearest rail hole. The rails are continuous, so no mid-board bridge is needed.
- **Fixed leads:** diodes and resistors have legs exactly **4 columns apart** and cannot be bent. Design the layout around 4-column spans, or plan orange jumpers that extend a node to another column. Put real spans in the layout, so the agent doesn't have to improvise.
- **Pushbutton:** has 4 legs and straddles the center gap. The two top legs sit in row e at columns N and N+2. The bottom legs (row f) connect to nothing. A physical 2-pin button goes in the same two row-e holes.
- **Resistor rows:** a resistor standing vertically from row a reaches the − rail. Reaching the + rail needs row b, because of the fixed lead spacing.
- **Inspector quirks:** the unit (Ω/kΩ) and LED color drop-downs sometimes ignore clicks. Re-check every value after setting it. A misclick can exit to the dashboard; the work autosaves, so reopen the circuit.
- **Snapping:** LEDs may land one row off, or in the center gap. Verify every leg's hole by hovering: the whole column highlights green.
- **Testing two buttons at once:** the mouse can hold only one button. Add a temporary jumper across button A's two columns (this is exactly what pressing it does), press B, then delete the jumper.
- **Power:** use the "Power Supply" component set to 5 V, with a 1 A current limit. The total current shows on its display.
- **Brightness:** Tinkercad shows graded LED brightness and flags LEDs above 20 mA. It reveals faint glows that Proteus hides. It uses one Vf per color, so it will NOT reveal problems that depend on a specific part's Vf (for example InGaN green).

## Writing tinkercad_prompt.md

Start from templates/tinkercad_prompt.md. Always include:
1. "Work ONLY in this tab, do not open other sites, do not type passwords."
2. Setup: rename the circuit, place a full breadboard, confirm the 62 columns, and wire the power supply.
3. Rules:
   - wire colors (red = +5V, black = GND, orange = node extension)
   - BAND marks the cathode
   - anode = the bent leg
   - button placement
   - set and re-check every resistor value
4. The layout per block, as `column: contents`, with real 4-column spans.
5. Execution: build block 1 → test → STOP if it fails → the remaining blocks, each followed by its test.
6. The report format, exactly:
   - the URL
   - a deviations table
   - a test table
   - the build list as `Part | value/color | leg 1 hole | leg 2 hole | note`, power first, then block by block
   - the part totals

## Verifying the report (never skip)

For each block:
1. From the build list, collect every hole per column. Columns joined by an orange jumper count as one node.
2. Map each node to the spec node, for example "col 11+12 = X".
3. Check every spec connection:
   - right parts on the right node
   - diode bands on the cathode side
   - LED anodes correct
   - pull resistors to the correct rail
4. Check for shorts: both legs of one part must never be in the same node.
5. Check the totals against the spec BOM.

Output a verification table (block → nodes → PASS/FAIL), then `build_list.md`.

## Physical-transfer notes for build_list.md

- Follow the rail SIGNS printed on the physical board, not the rail position, because boards differ. "+rail col X" means the nearest + rail hole.
- A physical 2-pin button goes in the two row-e holes listed. If it doesn't fit, bend the legs; never change the node column.
- Measure every resistor with the multimeter before inserting it. 10 Ω (brown-black-black) and 100 Ω (brown-black-brown) are easy to confuse.
- Check high-Vf LEDs before inserting them: put the LED with 220 Ω on 5 V and measure the voltage across it. Green at 2.7 V or more is InGaN; if a dim ON state is a risk, swap it for yellow or red.
