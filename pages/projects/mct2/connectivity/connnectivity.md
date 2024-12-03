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

## USB


## HSIO
The carrier board is to make use of all of the High-Speed IO (HSIO) provided by the N100.

| Port    | Purpose    | PCIe Device | N100 PCIe Controller |
| ------- | ---------- | ----------- | -------------------- |
| HSIO 0  | USB 3.2    | N/A         | Controller #1        |
| HSIO 1  | USB 3.2    | N/A         | Controller #1        |
| HSIO 2  | M.2 Key E  | 1           | Controller #1        |
| HSIO 3  | M.2 Key B  | 2           | Controller #1        |
| HSIO 6  | Ethernet   | 3           | Controller #2        |
| HSIO 8  | M.2 Key M  | 4           | Controller #3        |
| HSIO 9  | M.2 Key M  | 4           | Controller #3        |
| HSIO 10 | M.2 Key M  | 4           | Controller #3        |
| HSIO 11 | M.2 Key M  | 4           | Controller #3        |

The first two HSIO lanes are used as USB 3.2 connected to the two USB Type-C ports. 




