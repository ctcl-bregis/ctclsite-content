Power management is one of the more complex parts of the project. Power regulators are expected to dominate the amount of ICs (integrated circuits; chips) used in the design.

## Overview
As a tablet computer, MediaCow Touch 2 contains a rechargeable battery pack.

MediaCow Touch 2 would charge off from USB Type-C Power Delivery that is supported by both USB Type-C ports present.

## LattePanda Mu
The LattePanda supports a wide voltage input of 9v to 20v, this allows the module to be powered directly off from system power that could be anywhere between 12v (worst case) and 20v.

## Voltage Supplies

### System Power - VSYS
System Power is the main supply that is directly from the battery or USB Type-C ports. Worst case voltage for the battery is 12v. Power from USB Type-C is expected to be 20v.

This supply is always available while the system is powered on or off.

### SMEC input voltage - SMEC_5V
