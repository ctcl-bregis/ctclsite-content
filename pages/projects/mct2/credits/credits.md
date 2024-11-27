## Software Used
Open Source software has been used whenever possible. 

### CAD and EDA

#### KiCAD
KiCAD is used to draw electrical schematics and design the carrier board PCB.

#### LibreCAD
LibreCAD was used for the first time on August 6 to record measurements of the battery pack that is used in the device.

#### OpenSCAD and FreeCAD
OpenSCAD was used for the design of the case. The design was going to be done in FreeCAD but soon after I switched to OpenSCAD to complete the case design.

### Planning and Documentation

#### draw.io/diagrams.net
The desktop version of draw.io was used extensively for planning the physical layout of the device.

#### Git and GitHub
The MediaCow Touch 2 hardware design and software files are hosted on GitHub for anyone to see while having the ability to easily sync progress across devices in cases where I have to go somewhere.

#### ctclsite-rust
This website hosts this documentation while being a convenient method to showcase my ideas, progress and thought processes. 

#### Discord
Using a chat service in as a way to dump ideas into categories has returned from MediaCow Touch 1 where I used a self-hosted Rocket.Chat instance for that purpose. This time I used a private "server" on Discord to dump and brainstorm ideas. At the conclusion of the project, I would make a public release of the channel logs. 

#### MediaWiki
A self-hosted MediaWiki instance is used for personal documentation. It's role in MediaCow Touch 2, however, is very limited. 

#### STM32CubeMX
STM32CubeMX was used to select the microcontroller used as the embedded controller (SMEC) and plan its pinout until the switch to the SP7021 as the embedded controller.

#### CircuitJS
[CircuitJS](https://falstad.com/circuit/) has been used to test ideas such as using Schottky diodes on the power inputs of SPI flash memory and connecting the IS pin of the Infineon BTS7006 to a microcontroller.

### Software Development
This software was used to develop software for the project.

#### VSCodium
VSCodium is used as the main editor for any software project, including this website. Content like these pages are written using VSCodium.

The 'Open Remote - SSH' extension played a crucial role during development as it let me edit files on the desktop PC from anywhwere like I am using VSCodium on that system.

## Hardware Used
Hardware used for development since May 2024:

**Format: Codename - Motherboard**

### Development Hardware
"Cyclobutane" is the codename that refers to the system on module itself and is unrelated to the development carrier boards from LattePanda.

- "Cyclobutane" - LattePanda Mu
  - Experimentation
  - Communications
  - Used in the end product

### Workstations

- "Polybutylene Terephthalate" - ASRock B550M Pro4
  - Circuit and device design
  - Documentation
  - Software development
  - Research
  - Communications
- "Polymethylmethacrylate" - HP ZBook Studio G3 15 (Xeon)
  - Circuit and device design
  - Documentation
  - Software development
  - Research
  - Communications
- "Chlorofluoroethane" ("R151") - Lenovo ThinkPad T450s
  - Device design
  - Documentation
  - Research
- "Chlorodifluoromethane" ("R22") - Lenovo ThinkPad T430s
  - Planning
- [No Codename] - Apple iPhone XR
  - Social media promotion
  - Research
  - Communications
- "Tetrahydrocannabinol" - ASUS Zenfone 9
  - Documentation
  - Communications
  - Research
  - Remote internet access

### Servers

- "Levoamphetamine" - HP ProLiant BL460c G8
  - File storage host (Nextcloud)
  - Planning (MediaWiki)
  - DNS server
- "Promethazine" - Supermicro X8SIE
  - File storage
- "Dextromethorphan" - Supermicro X8SIE
  - Router
  - Remote access host

### Other

- [No Codename] - Texas Instruments TI-Nspire CX
  - Formula calculation
- "Dimethylheptylpyran" - Flipper Zero FZ.1
  - Device debugging

## Locations

MediaCow Touch 2 was developed in the following locations:

- Atlantic Beach, North Carolina, United States
- Bramwell, West Virginia, United States
- Fort Myers Beach, Florida, United States
- Fort Myers, Florida, United States
- Midlothian, Virginia, United States - Including:
  - Brightpoint Community College Midlothian Eliades and Trailblazer buildings
- Orlando, Florida, United States
- Pocahontas, West Virginia, United States
- Richmond, Virginia, United States
  - The Pace Center (VCU)
  - Qimonda Atrium in VCU Engineering Hall
- Sylvan Beach, New York, United States

90+% of development was done in Midlothian, Virginia. 

This list excludes any work done from aircraft, which was an Airbus A320 for both the departing and return flights from Orlando, Florida during the August 2024 trip to the Fort Myers Beach area.

## Individuals and Organizations 
The project's codename and a major part of the theme is based off from L'Hommeblanc of Paris, France who I knew online since October 2020. He had this role in the project since its original planning stages in early 2021.

This project was made possible by LattePanda where hardware and documentation was provided.

### Hardware
These organizations and individuals have provided hardware for me to use for development.

- LattePanda
- CrashSys

### Technical Support
Organizations that provided guides, datasheets and other technical support documents that were used in development:

- Adafruit
- Advantech
- Altium
- Analog Devices (including Linear Technology Corporation and Maxim Integrated)
- Congatec
- Crystalfontz
- CTS
- Delta Electronics
- Diodes Incorporated
- ECS
- Flipper Devices
- Foxconn
- Fuzhou Rockchip
- Infineon Technologies (including Cypress Technology and Qimonda)
- Innolux Display
- Intel
- ISSI
- JST
- LOTES
- Lumissil
- MediaTek
- Micron Technology
- Molex
- Monolithic Power Systems
- Nexperia
- NXP
- Onsemi
- Richtek
- Samsung Electro-Mechanics
- Samsung Electronics
- Silergy
- SINOVOIP Banana Pi
- SiTime
- STMicroelectronics
- Sunplus Technology
- Tempo Semiconductor (including IDT and SigmaTel)
- Texas Instruments
- Tibbo Technology
- Toradex
- Toshiba/KIOXIA
- Vishay (including Siliconix and General Semiconductor)
- Winbond Electronics
- Xi'an Aerosemi Technology
- YAGEO

## Inspiration
MediaCow Touch 2's design and hardware had inspiration from the following products:

- Ainol NOVO7 Paladin
  - Overall physical design inspiration
- Apple iPhone 6S
  - Display selection
- Apple iPhone XR 
  - Display selection
- ASUS Chromebook Flip C100P
  - Some inspiration for original Rockchip-based MediaCow Touch 2 idea
  - Display selection
- ASUS Zenfone 9 AI2202
  - USB Type-C feature inspiration, specifically USB PD capabilities
- Banana Pi BPI-F2P/BPI-F2S
  - Circuit design reference
- Flipper Devices Flipper Zero FZ.1
  - LED controller ideas
- HP ZBook Studio G3 15
  - USB Type-C feature inspiration
  - Display selection
  - CPU cooling ideas
- HP(E) ProLiant BL460c G8, BladeSystem C3000 chassis, ProLiant DL380 G7
  - Inlet temperature sensor idea
- LattePanda Mu Full Carrier
  - Circuit design reference
- LattePanda Mu Lite Carrier
  - Circuit design reference
- Lenovo 100e Chromebook 2nd Gen (11.6" Intel)
  - Status LED idea
  - USB Type-C feature ideas
- Lenovo ThinkPad T430s
  - Battery layout ideas
- Lenovo ThinkPad T450s
  - Battery layout ideas
- Matterport Pro2
  - Battery layout ideas
- Microsoft Surface series
  - Overall physical design inspiration
- Microsoft Zune series
  - Original inspiration for MediaCow
- Nintendo Switch (2017)
  - Display selection
  - USB Type-C Power Delivery ideas
- Positivo BGH Y210
  - Camera placement idea
- Samsung Chromebook XE500C13
  - Display size comparison
  - Status LED idea
- Samsung Galaxy S7 SM-G930F
  - Status LED idea
- Samsung Galaxy Tab3 10.1 P5210
  - Used as an example of an x86-based tablet
- Supermicro H13SAE-MF
  - Socketed BIOS SPI flash idea
  - TPM module pinout
- Valve Steam Deck
  - Overall physical design inspiration
  - Device usage ideas