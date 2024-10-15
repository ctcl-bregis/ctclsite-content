MonitorCow is a series of external monitors that was originally part of [MediaCow Touch 2](/projects/mct2/).

The idea for me to build custom monitors is not new; I have been planning to do something like this since 2017. 

## Naming
Names for MonitorCow devices are in the following scheme: `MonitorCow-<Panel Name>`

For the initial prototypes described below, the name of those units would be MonitorCow-N156KME-GNA.

## Features
MonitorCow is intended to be easily to disassemble in order to swap parts such as the LCD panel. The internal connection for the LCD panel would be Embedded DisplayPort (eDP) which most modern laptops use.

### Connectivity
Like many external monitors, the main interface is a USB Type-C port with DisplayPort alternate mode.

A feature unique to MonitorCow is that it has a connector for HDMI for connecting devices that do not have DisplayPort over USB Type-C.
 
## Hardware
The hardware for MonitorCow is meant to be more simple to design and assemble, requiring no custom PCBs.

### PCB
Instead of having the complex task of designing another PCB for use in the monitor, an off-the-shelf controller board may be used. Boards using the Realtek RTD2775QT/YT are to be used with the N156KME-GNA panels described in the section below. These boards are not common, many controller boards seen online are for 1366x768 or 1920x1080 and frame rates up to 60 Hz where they find use in DIY hobby projects using a Raspberry Pi, not a desktop/gaming monitor setup.

These boards came from Shenzhen, China where the package presumably shipped by sea.

### Display
The inital prototypes may use Innolux N156KME-GNA, the specific display was chosen due to its very close DPI value to the 11.6" display being used in MediaCow Touch 2 itself while having a 2K resolution (2560x1440). An interesting feature is that the panel supports refresh rates up to 165Hz while having a 4-lane eDP1.3 connector.

### Case
The initial units using 15.6" panels would likely be made from wood with mounting brackets made from 3D printed PETG.

MonitorCow may have support VESA mounts. This feature was added for the ability to use a stand or mount with MonitorCow. 

## History
Two N156KME-GNA were received on October 7, 2024 while as of October 10, 2024, I await the two display eDP controller boards. Though designed for use with MediaCow Touch 2, they may be used with a [desktop PC](/projects/pc_pbt/).