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


## Negative hold time

Negative hold time is generally seen where a delay is already added in the datapath inside the flop.

Assume the flop which foundry gives us a library part has ports named as CLK-port, Data-port. Now treat this as a wrapper. Inside this we have the real flop whose ports are CLK-in, Data-in. CLK-port is connected directly to CLK-in, Data-port goes through some delay element (either buffer of routing whatever) to Data-in.  So, even if the actual flop has hold requirement of say 0.2ns, if the data delay element value is 0.5ns,  the library will give specs as -0.3ns HOLD requirement for the above flop. This signifies even if the data chagnes 0.3ns before CLK, it can be still latched as the actual flop will still meet 0.2ns HOLD. (data changes after 0.2ns from clk change)



## Negative Gate Delay

In the context of a cell or circuit, change in the input pins state could cause a change in ouput pin. Signal is said to have reached a point of no return in the transition, once it crosses a certain threshold. These thresholds are predetermined for the circuit. They could be different for the rise and fall transition, input and ouput pin of a circuit or standard cell. 

The difference in time from the input reaching 50% of the final value of the transition to that of the output is termed as propagation delay. It seems a bit absurd to have negative value of propagation delay as it provides a misinterpretation of the the effect happening before the cause. Common sense says that the ouput should only change after input. However, under certain special cases, it is possible to have negative delay. In most of such cases, we have one or more of the following conditions:

 	1.	A high drive strenth transitor.
 	2.	Slow transition at the input.
 	3.	Small load at the output.

Under all of the above mentioned conditions, the ouput is expected to transition faster than the input signal, and can result in negative propagation delay. 

