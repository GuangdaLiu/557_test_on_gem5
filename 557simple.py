import time
import m5
from m5.objects import *

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'atomic'
system.mem_ranges = [AddrRange('8GB')]

system.cpu = AtomicSimpleCPU()

system.membus = SystemXBar()

system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports
system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]

system.mem_ctrl.port = system.membus.mem_side_ports

binary = './static_xz_r'

# for gem5 V21 and beyond, uncomment the following line
system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = [binary, './smallf.tar.xz', '1', '12eff5edf0b5994e554f5210e043b59518234486281a4c9830eb5e8edb14d65ebf9d0f66b9659e4b6db7b0dc458129a60d77e7a750b7b34ef67b02229ef6588e', '100', '300', '3']
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()
print("Beginning simulation!!")
ts = time.time()
exit_event = m5.simulate()
te = time.time()
print(f'Running {binary} in {te-ts}s')
print('Exiting @ tick {} because {}'
      .format(m5.curTick(), exit_event.getCause()))
      