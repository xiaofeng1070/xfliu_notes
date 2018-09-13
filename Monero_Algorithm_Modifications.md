# Monero algorithm updates: 

## Shuffle and add modificaiton (Sep 2018)

Crypotonight is memory-intensive in terms of memory latency, but not bandwidth. Modern CPUs use 64-byte wide cache lines, but Cryptonight only loads/sotres 16 bytes at a time, so 75% of available CPU cache bandwidth is wasted. ASICs are optimized for these 16 byte wide memory accesses, so they always use 100% of whatever memory they have. 

The idea is to do something computationally light and safe with the other 48 bytes of the same cache line (which is loaded in L1 cache anyway) on each step. Shuffle modification, as can be guessed by its name, treats these 48 bytes as 3 16-byte elements, shuffles them and performans 6x64-bit interger additions on them to make sure ASIC can't do it via simple rewiring. 

The actual shuffle and add logic has 4 different cases depending on where in the 64-byte line the AES round is performed. 

The shuffle modification makes Cryptonight 4 times more demanding for memory bandwidth, making ASIC/FPGA 4 times slower*. At the same time, CPU/GPU performance stays almost the same because this bandiwdth is already there, it's just not used yet. Shuffle can also be done in parallel with existing Cryptonight caculations.

*The 4 times slowdown applies only to devices (ASIC/FPGA) that use external memory for storing the scratchpad and saturate this memory's bandwidth. Devices that use on-chip memory have no problems with bandwidth, but they'll still have to do 4 times more memory reads/writes, so they'll be also become somewhat slower.



## Integer math modification (Sep 2018)

It adds one 64:32 bit integer division and one 64 bit integer square root per iteration.

Adding integer division and integer square roots to the main loop ramps up the complexity of ASIC/FPGA and silicon area needed to be implement it, so they'll be much less efficient with the same transistor budget and/or power consumption. Most common hardware implementations of division and square roots require a lot of clock cycles of latency: at least 8 cycles for 64:32 bit division and the same 8 cycles for 64 bit square root. These latencies are achieved for the best and fastest hardware implementations I could find. And the way this modification is made ensures that division and square root from the same main loop iteration can't be done in parallel, so their latencies add up making it staggering 16 cycles per iteration in the best case, comparing to 1 cycle per iteration in the original Crytonight. Even though this latency can be hidden in pipelined implementation, it will require A LOT of logical elements/silicon area to implement. Hiding the latency will also require many parallel scratchpads which will be a strong factor for hardware with on-chip memory. They just don't have enough memory to hide the latency entirely. 

Good news for CPU and GPU is that division and square roots can be added to the main loop in such a way that their latency is completely hidden, so again there is almost no slowdown. 



## Performance (Sep 2018)

ASIC/FPGA which use external memory for scratchpad will get 4 times slower due to increased bandwidth usage. ASIC/FPGA which use on-chip memory for scratchpad will get ~15 times slower because of high latencies introduced with division and square root calculations: they just don't have enough on-chip memory to hide these latencies with many parallel Cryptonight calculations. 



They target different classes of ASICs/FPGAs. Shuffle mod targets devices with external memory, making them 4 times slower. Integer math mod target devices with on-chip memory, making them 8~10 times slower because of hight division and square root latency. They work best together. Remove one mod, and you will enable an efficient ASIC/FPGA again - either with on-chip SRAM or with HMB external memory. 



Leaving just 1 square root won't make it easier for FPGA. The point of having a square root is that they'll still need to implement it and waste space on chip for it and this it has high computation latency.  





