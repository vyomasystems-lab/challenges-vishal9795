# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    I1 = 3
    SEL1 = 1 

    #input driving
    dut.inp1.value = I1
    dut.sel.value = SEL1

    await Timer(2, units='ns') 

    assert dut.out.value == I1(SEL1),f" muxout is incorrect:{dut.X.value}! = 3"
    
    @cocotb.test()
async def mux_randomised_test(dut):
    """Test for mux 2 random numbers multiple times"""

    for i in range(5):

        I1 = random.randint(0, 15)
        SEL1 = random.randint(0, 15)

        dut.inp1.value = I1
        dut.sel.value = SEL1

        await Timer(2, units='ns')
        
        dut._log.info(f'I1={I1:05} SEL1={SEL1:05} model={I1(SEL1):05} DUT={int(dut.out.value):05}')
        assert dut.out.value == I1(SEL1), "Randomised test failed with: {I1}({SEL1}) = {OUT}".format(
            A=dut.inp1.value, sel=dut.sel.value, out=dut.out.value)


