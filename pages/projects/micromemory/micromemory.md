MicroMemory is a series of memory modules for embedded devices with memory bus widths less than 64 bits.

## Versions

### HyperRAM
Intended applications for SDRAM MicroMemory are microcontrollers and FPGAs.

#### EEPROM
HyperRAM MicroMemory modules contain a 1Kbit I2C EEPROM for 128 Bytes of configuration data. 

### SPI PSRAM
Intended applications for SDRAM MicroMemory are microcontrollers.

#### EEPROM
SPI PSRAM MicroMemory modules contain a 1Kbit I2C EEPROM for 128 Bytes of configuration data. 

### SDRAM
SDRAM is the first memory standard that a MicroMemory module was designed for. 

Intended applications for SDRAM MicroMemory are microcontrollers, FPGAs, microprocessors and DSPs.

#### EEPROM
SDRAM MicroMemory modules contain a 1Kbit I2C EEPROM for 128 Bytes of configuration data. 

### DDR
Intended applications for DDR MicroMemory are FPGAs, microprocessors and DSPs.

#### EEPROM
DDR MicroMemory modules contain a 1Kbit I2C EEPROM for 128 Bytes of configuration data. 

### DDR2
Intended applications for DDR2 MicroMemory are FPGAs, microprocessors, SoCs and DSPs.

#### EEPROM
DDR2 MicroMemory modules contain a 1Kbit I2C EEPROM for 128 Bytes of configuration data. 

### DDR3
Intended applications for DDR3 MicroMemory are FPGAs, microprocessors and SoCs.

#### EEPROM
DDR3 MicroMemory modules contain a 2Kbit I2C EEPROM for 256 Bytes of configuration data. 

### DDR4
Intended applications for DDR4 MicroMemory are FPGAs, microprocessors and SoCs.

#### EEPROM
DDR4 MicroMemory modules contain a 4Kbit I2C EEPROM for 512 Bytes of configuration data. 

## Naming Scheme

AABCCDDEEFGHH-IIIJKKKKLLMN

- AA - Always "MM" for MicroMemory
- B - Memory type
  - E - EDO DRAM
  - F - FPM DRAM
  - H - HyperRAM
  - S - SPI PSRAM
  - 0 - SDRAM
  - 1 - DDR
  - 2 - DDR2
  - 3 - DDR3
  - 4 - DDR4
  - 5 - DDR5
- CC - Bus width
  - 01 - 1-bit
  - 02 - 2-bit
  - 04 - 4-bit
  - 08 - 8-bit 
  - 16 - 16-bit
  - 32 - 32-bit
  - 40 - 40-bit (32-bit + 8-bit ECC)
- DD - Device bit width
  - 01 - 1-bit
  - 02 - 2-bit
  - 04 - 4-bit
  - 08 - 8-bit 
  - 16 - 16-bit
- E - Rank count
- FFFF - Device package type
  - BGAX - BGA
  - NSOC - SOIC (0.150 Inch)
  - SSON - SON
  - TSSP - TSSOP
  - TTSP - TSOP
  - USON - USON
  - WSOC - SOIC-Wide (0.300 Inch)
- GG - Device package pin count
- H - Signaling
  - S - Single Data Rate (SDR)
  - D - Double Data Rate (DDR)
  - Q - Quadruple Data Rate (QDR)
  - 4 - PAM4
- I - Module format
  - C - Mezzanine connector
  - M - M.2
  - S - Standard SODIMM 
- Separator
- JJJ - Total Capacity 
  - 001
  - 002
  - 004
  - 008
  - 012
  - 016
  - 024
  - 032
  - 048
  - 064
  - 128
  - 256
  - 384
  - 512
- K - Total Capacity Multiplier
  - B - Byte (1)
  - K - Kilobyte (1024)
  - M - Megabyte (1048576)
  - G - Gigabyte (1073741824)
- LLLL - Maximum frequency, in MHz
  - 0001 - 1 MHz
  - 1600 - 1600 MHz (for example: DDR4-3200)
- MM - Device Vendor
  - AM - AMD
  - CY - Cypress
  - CX - CXMT
  - EE - Elpida
  - HX - Hyundai/Hynix/SK hynix
  - IM - Intelligent Memory
  - IS - ISSI
  - IT - Intel
  - IQ - Qimonda
  - IX - Infineon
  - LG - LG/GoldStar
  - MI - Mitsubishi
  - MP - Mosel Vitelic/ProMOS
  - MT - Micron Technology
  - NT - Nanya Technology
  - PS - Powerchip
  - SE - Samsung
  - WB - Winbond
- N - Vendor DRAM die revision
  - A - A-die/Rev. A
  - ...
  - Z - Z-die/Rev. Z
- O - Special feature
  - X - None
  - E - On-die ECC

-JJJKLLLLMMNO is assigned to specific units. It is omitted in PCB design.

As MicroMemory covers legacy memory formats and may reuse parts from existing hardware, former DRAM vendors are included. 