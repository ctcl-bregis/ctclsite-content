Power usage is one of the main concerns with using the SP7021 over a common microcontroller such as the STM32L496. 

## Downclocking and Core Usage
The CPU cores in the SP7021 would be downclocked to use less power.

Also, Cortex-A7 cores are may be shut down when they are not used. Certain functions may be dedicated to specific cores, for example: SMEC would dedicate audio processing from microphones and from the system to one core while processing for driving the side-mounted display would be dedicated to another core. 

## PMIC
The SP7021 contains multiple buck converters intended to be used with a 3.3v input though in MediaCow Touch 2 and also the related [SP7021-Block](/projects/sp7021_sbc/), these buck converters are left unused and all voltages are provided by an external PMIC. This increases complexity though it allows for digital control of the voltages.




