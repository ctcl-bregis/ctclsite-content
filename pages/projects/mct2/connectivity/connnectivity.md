This page covers physical connectivity provided by the device. For details on network and wireless, see [Network](../network/).

## Overview
The following connectors are to be present:

- 2x USB Type-C with Power Delivery sink/source up to 20v
- 2x USB 3.x Type-A
- 2x USB 2.0 Type-A
- 1x Full-size HDMI
- 1x RJ-45 Ethernet
- 1x 3.5mm headphone audio out
- 1x 3.5mm microphone audio in

Note: The use of a full-size HDMI connector is subject to change


## TCP
Both TCP ports provided by the N100 are to be used for USB Type-C. **DisplayPort** alternate mode is to be supported on both USB Type-C ports.

Each TCP port uses a USB 3.2 and USB 2.0 link.

USB Power Delivery is to be controlled by [SMEC](../smec/).

## USB

### USB 2.0

| Port    | Purpose    |
| ------- | ---------- |
| USB2 1  | TCP Port 0 |
| USB2 2  | TCP Port 1 |
| USB2 3  |            |
| USB2 4  |            |
| USB2 5  |            |
| USB2 6  |            |
| USB2 7  |            |
| USB2 8  |            |

## HSIO
The carrier board is to make use of all of the High-Speed IO (HSIO) provided by the N100.

| Port    | Purpose    | PCIe Device | N100 PCIe Controller |
| ------- | ---------- | ----------- | -------------------- |
| HSIO 0  | TCP Port 0 | N/A         | Controller #1        |
| HSIO 1  | TCP Port 1 | N/A         | Controller #1        |
| HSIO 2  | M.2 Key E  | 1           | Controller #1        |
| HSIO 3  | M.2 Key B  | 2           | Controller #1        |
| HSIO 6  | Ethernet   | 3           | Controller #2        |
| HSIO 8  | M.2 Key M  | 4           | Controller #3        |
| HSIO 9  | M.2 Key M  | 4           | Controller #3        |
| HSIO 10 | M.2 Key M  | 4           | Controller #3        |
| HSIO 11 | M.2 Key M  | 4           | Controller #3        |

The first two HSIO lanes are used as USB 3.2 connected to the two USB Type-C ports. 

## HDMI
A single HDMI port is to be provided utilizing the Digital Display Interface (DDI) of the N100.
