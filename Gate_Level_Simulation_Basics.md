# Gate Level Simulation Basics

## Inertial delay model

Propagate only those signals to output after the input signals have remained unchanged for a time period equal to or greater than propagation delay of the model.

惯性延迟考虑了电路中存在大量的分布电容，信号在电路中传输，存在对电容的充放电效应。当输入较小宽度的脉冲将会被滤除，即不允许所有宽度小于指定延迟的脉冲通过电路单元。能够让对应输出有变化的最小脉冲宽度即为惯性延迟，是所有电子器件都存在的一种延迟特性。因此，为了使器件对输入信号的的变化产生响应，信号变化后要维持足够长的时间。在仿真过程中， 该延迟用于模拟元件延迟，一般元语、门单元、开关单元、连续赋值等中的延迟在模拟时均为惯性延迟。

## Transport delay model

Propagate all signals to an output after any input signal changes.

传输延迟一般为输入信号变化到输出信号变化的时间， 不会对输入信号进行滤除处理，所以传输延迟是一种绝对延迟，这种延迟类似于物理传输线的延迟，在仿真中用于模拟连线延迟。

## Global Pulse Control

- pulse_r:	to set the pulse reject limit for both module path delays and interconnect delays.
- pulse_e: to set the pulse error limit for both module path delays and interconnect delays.
- -pulse_r and -pulse_e: module path delays
- -pulse_int_r and -pulse_int_e: interconnect delays
- 0 <= Error_Percent & Reject_Percent <= 100
- Reject_percent <= Error_percent

