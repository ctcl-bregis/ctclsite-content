


## ARM Cortex-A7 Cores
SMEC would run either a customized FreeBSD, OpenBSD or Linux image. Likely the latter, Linux, would be used as development resources are already provided by Sunplus/Tibbo for Linux.

## ARM926 Core
The ARM926 core is independent from the ARM Cortex-A7 cores. It may run FreeRTOS or bare-metal code for system functions. The ARM926 core shall be active it all times.

## Programming Language
Firmware used on SMEC may be written in Rust due to its efficiency along with memory safety.
