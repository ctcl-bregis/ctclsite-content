MediaCow Touch 2 is a project pertaining to the design and assembly of a mobile tablet device.

**Disclaimer**: Anything on this page and other pages related to this project is preliminary data and may change at any moment.

## History
The project technically started in early March 2021.

In May 2024, I have found out about the [LattePanda Mu](https://www.lattepanda.com/lattepanda-mu) System on Module. This module uses an x86-64 processor instead of an ARM64 SoC. [According to Intel](https://ark.intel.com/content/www/us/en/ark/products/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz.html), the N100 is targeted towards use in mobile devices. Using an x86 processor has its benefits including better software support and laptop-like performance.

Ideas for MediaCow Touch 2 date back to March 2021 as mentioned before. The initial idea at the time surrounded the use of a soldered-down Rockchip RK3588 SoC with ten DDR4 DRAM ICs, specifically Nanya NT5AD1024M8A3, for 8GB of memory with ECC. This would have been almost impossible if not impossible for me to design at the time so I later decided to use a System on Module.

Halfway through March 2021 (March 12, 2021 according to emails), I decided to use the Graperain GR3399 System on Module that uses the Rockchip RK3399 and 2GB of DDR3 RAM (4x Samsung K4B4G1649E-BCMA). The development kit including the SoM was ordered in February 2022 but ended up never being used for the project. I preferred to use the MXM3.0 ("Gold Finger") format of the System on Module over the "Stamp hole" G3399 so during the assembly stage, I could just remove a couple screws to remove the module from the development kit and install the module into the prototype without having to desolder and risk damaging the module and/or development board.

Later in 2022, I found out about various System on Modules that became available from Banana Pi, who supplied the board for MediaCow Touch 1, that used the newer and more powerful Rockchip RK3588.

Throughout 2022 and 2023, I stopped working on hardware design projects due to their complexity and focused on software instead.

In May 2024, I signed up for the LattePanda Mu Free Trial Event to receive a LattePanda Mu System on Module along with its Lite Carrier Board. I did not expect the idea to be approved and for me to receive the development hardware. 

### Name
MediaCow Touch 2 is part of the MediaCow series, the history behind the name is covered in the [MediaCow page](/projects/mc/).

## Overview


### Security and Privacy Features
MediaCow Touch 2 provides hardware-level security features that are often not seen in devices of its class. 

#### Audio and Microphones
Audio signals to and from the integrated audio CODEC can be disconnected by onboard switches.

Speakers are to be connected to the carrier board through JST-style connectors instead of being soldered directly. 

#### Wireless
Wireless connectivity including Wi-Fi, Bluetooth and cellular is provided by M.2-format modules that can be removed to completely disable wireless connectivity or replaced for changing unique identifiers.

#### TPM
The carrier board has a TPM header for the option of a TPM module.

#### State
MediaCow Touch 2 follows the principles of the document titled ["State Considered Harmful"](https://blog.invisiblethings.org/papers/2015/state_harmful.pdf).

User storage is to be provided by an SSD connected to the carrier board's M.2 slot. The SPI flash memory IC used for BIOS is socketed on the carrier board and can be removed when the device is disassembled. 

By default, the LattePanda Mu contains an 64GB eMMC for user-accessible storage and an SPI flash for BIOS. It may be possible to remove these devices from the module or be provided a LattePanda Mu that does not have these devices populated.

This also applies to the embedded controller, SMEC, where its storage is provided by an eMMC module that plugs into the carrier board. It may be possible for the embedded controller to emulate an SPI flash device for the LattePanda Mu to read from. 

#### BIOS
The BIOS to be used is coreboot, an open source firmware. 

#### Ports
Power to USB ports can be disabled by the embedded controller. This can help prevent damage from devices such as USB Killer or Bad USB.
