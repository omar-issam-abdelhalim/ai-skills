# Proteus Playbook (Proteus 8.13 Professional, Windows, desktop control)

Everything here was learned from a real run. Follow it literally.

## Environment facts

- Install path: `C:\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\BIN\PDS.EXE`
- Reference display: 2560×1600 at 150% scaling, single monitor (adjust click strategy to your own display). Proteus uses Qt 4.8.7, so it may render slightly blurry. Zoom in before precise clicks.
- `.pdsprj` is a ZIP containing a proprietary binary `ROOT.DSN`. NEVER try to generate or edit project files directly. Build only through the GUI.
- Desktop control must run in a **local** session on this machine. Cloud or remote sessions cannot see or click the Proteus window.

## Procedure

1. **New Project:**
   - name and path inside the project folder's `proteus\`
   - schematic from the DEFAULT template
   - No PCB
   - No Firmware
2. **Pick Devices:** press `P` in Component Mode and search by keyword. Verified names: `1N4001`, `RES`, `LED-RED`, `LED-GREEN`, `LED-YELLOW`, `LED-BLUE`, `SWITCH`. If a name doesn't match, pick the closest one and report it.
3. **Inputs:** use `SWITCH` (latching), NOT `BUTTON` (momentary). With SWITCH, a state can be held while you read values or take screenshots.
4. **Power:** Terminals Mode → POWER with the label `+5V`, and GROUND. Proteus parses the label as the rail voltage. Place a separate terminal next to each part instead of running long wires. All terminals with the same label are connected.
5. **Wiring:** click a pin end, then the other pin end. A junction dot means the wires are connected. Zoom in before every wire.
6. **Values:** double-click a part → Resistance. **RES defaults to 10k.** Set every value right after placing the part, and re-verify every resistor before each test. In the first run, AND pull-downs were left at 10k, which would have made AND behave as OR.
7. **Measurement:** Virtual Instruments Mode → DC VOLTMETER, with + on the block's main node and − on ground. It shows `+88.8` before the simulation runs; that is a placeholder, not a reading.
8. **Labels:** add a text label per block, using 2D graphics text.
9. **Run:** ▶ at the bottom-left starts the simulation, ■ stops it. Click a SWITCH while running to toggle it.
10. **Save:** Ctrl+S after every block.

## Known failure modes and workarounds

- **Dead screen region:** Proteus ignored mouse moves in the upper-right area of the screen, so wire endpoints landed in stale positions. Pan the view and keep the work in the center.
- **"Edit Wire Style" dialog:** opens if you click twice on a wire, or on a wire lying over a pin. Cancel without changes, delete the wire, and re-draw it.
- **"Part reference already in use":** caused by renaming in the wrong order. Use a temporary name, then rename.
- **"Height not valid":** a typo in a text label's size field. Fix the value.
- **Leftover wire stubs** inside symbols: harmless if they touch only one pin. Mention them in the log.
- **Screenshots:** if the screenshot tool doesn't return a file, capture the screen with PowerShell:
  ```powershell
  Add-Type -AssemblyName System.Windows.Forms,System.Drawing
  $b=[System.Windows.Forms.Screen]::PrimaryScreen.Bounds
  $bmp=New-Object System.Drawing.Bitmap $b.Width,$b.Height
  $g=[System.Drawing.Graphics]::FromImage($bmp); $g.CopyFromScreen($b.Location,[System.Drawing.Point]::Empty,$b.Size)
  $bmp.Save("<folder>\state_XX.png"); $g.Dispose(); $bmp.Dispose()
  ```
- **Anything else unexpected:** STOP and describe it to the user.

## Test matrix

- Set all blocks' inputs to the same state, then read every voltmeter and every LED. Repeat for each state.
- Log a table in `proteus_log.md`: block × state → measured V, LED, calculated V, Δ.
- Take one screenshot per state (`state_00.png` …).

## Modifying an existing project (Phase 4)

1. In PowerShell, copy: `Copy-Item "<x>.pdsprj" "<x>_v2.pdsprj"`
2. Open the COPY only.
3. Delete the part, then delete the wires it left dangling.
4. Verify that every voltmeter is still on the right node and on ground.
5. Rerun the full matrix, and add a v1-vs-v2 table to the log.

## Display caveats to explain to the user

- LED colors in Proteus don't change the simulated Vf in a meaningful way. The final LED colors come from the physical design.
- Proteus LEDs are ON/OFF only, so a faint glow never shows. Cross-check every marginal state with the analysis.
