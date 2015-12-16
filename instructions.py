#List of NES commands and what they do (WIP)

def ADC(cpu, source):
    """
    Add value to A with carry
    """
    

    return None, 0


def AND(cpu, source):
    """
    'AND' memory with Accumulator
    """
    
    return None, 0


def ASL(cpu, source):
    """
    Shift left one bit
    """
    
    return value, 0


def BCC(cpu, source):
    """
    Branch if carry flag is *not* set
    """
    
    return None, extra_cycle


def BCS(cpu, source):
    """
    Branch if carry flag is set
    """

    return None, extra_cycle


def BEQ(cpu, source):
    """
    Branch if result was zero
    """
    
    return None, extra_cycle


def BIT(cpu, source):
    """
    Compare bits
    """
    
    return None, 0


def BMI(cpu, source):
    """
    Branch if result was negative
    """
    
    return None, extra_cycle


def BNE(cpu, source):
    """
    Branch if result was *not* zero
    """
    
    return None, extra_cycle


def BPL(cpu, source):
    """
    Branch if result was positive
    """
    
    return None, extra_cycle


def BRK(cpu, *args):
    """
    Request a maskable interrupt (IRQ)
    """
    cpu.set_status('break', True)
    cpu.IRQ.value = "I"


def BVC(cpu, source):
    """
    Branch if overflow flag is *not* set
    """
    
    return None, extra_cycle


def BVS(cpu, source):
    """
    Branch if overflow flag is set
    """
    
    return None, extra_cycle


def CLC(cpu, *args):
    """
    Clear carry status flag
    """
    
    return None, 0


def CLD(cpu, *args):
    """
    Clear decimal status flag
    """
    
    return None, 0


def CLI(cpu, *args):
    """
    Clear interrupt status flag
    """
    
    return None, 0


def CLV(cpu, *args):
    """
    Clear overflow status flag
    """
    
    return None, 0


def CMP(cpu, source):
    """
    Compare accumulator with value
    """
    
    return None, 0


def CPX(cpu, source):
    """
    Compare X-register with value
    """
    
    return None, 0


def CPY(cpu, source):
    """
    Compare Y-register with value
    """
    
    return None, 0


def DEC(cpu, source):
    """
    Decrement memory
    """
    
    return value, 0


def DEX(cpu, *args):
    """
    Decrement X-register
    """
    
    return None, 0


def DEY(cpu, *args):
    """
    Decrement Y-register
    """
    
    return None, 0


def EOR(cpu, source):
    """
    XOR value with accumulator
    """
    
    return None, 0


def INC(cpu, source):
    """
    Increment memory
    """
    
    return value, 0


def INX(cpu, *args):
    """
    Increment X-register
    """
    
    return None, 0


def INY(cpu, *args):
    """
    Increment Y-register
    """
    
    return None, 0


def JMP(cpu, source):
    """
    Jump to a location in memory
    """
    
    return None, 0


def JSR(cpu, source):
    """
    Jump to a location in memory and store the return address on the stack
    """
    
    return None, 0


def LDA(cpu, source):
    """
    Load a value into the accumulator
    """
    
    return None, 0


def LDX(cpu, source):
    """
    Load a value into the X-register
    """
    
    return None, 0


def LDY(cpu, source):
    """
    Load a value into the Y-register
    """
    
    return None, 0


def LSR(cpu, source):
    """
    Shift right one bit
    """
    
    return value, 0


def NOP(*args):
    """
    No operation
    """
    return None, 0


def ORA(cpu, source):
    """
    'OR' memory with Accumulator
    """
    
    return None, 0


def PHA(cpu, *args):
    """
    Push the accumulator onto the stack
    """
    
    return None, 0


def PHP(cpu, *args):
    """
    Push the status register onto the stack
    """
    
    return None, 0


def PLA(cpu, *args):
    """
    Pop the accumulator from the stack
    """
    
    return None, 0


def PLP(cpu, *args):
    """
    Pop the status register from the stack
    """
    
    return None, 0


def ROL(cpu, source):
    """
    Rotate value one bit left
    """
    
    return value, 0


def ROR(cpu, source):
    """
    Rotate value one bit right
    """
    
    return value, 0


def RTI(cpu, *args):
    """
    Return from interrupt
    """
    
    return None, 0


def RTS(cpu, *args):
    """
    Return from subroutine
    """
    
    return None, 0


def SBC(cpu, source):
    """
    Subtract with carry
    """
    
    return None, 0


def SEC(cpu, *args):
    """
    Set carry status flag
    """
    
    return None, 0


def SED(cpu, *args):
    """
    Set decimal status flag
    """
    
    return None, 0


def SEI(cpu, *args):
    """
    Set interrupt ignore status flag
    """
    
    return None, 0


def STA(cpu, *args):
    """
    Store accumulator value in memory location
    """
    return cpu.registers['a'].read(), 0


def STX(cpu, *args):
    """
    Store X-register value in memory
    """
    return cpu.registers['x'].read(), 0


def STY(cpu, *args):
    """
    Store Y-register value in memory
    """
    return cpu.registers['y'].read(), 0


def TAX(cpu, *args):
    """
    Transfer accumulator to X-register
    """
    
    return None, 0


def TAY(cpu, *args):
    """
    Transfer accumulator to Y-register
    """
    
    return None, 0


def TSX(cpu, *args):
    """
    Transfer stack pointer to X-register
    """
    
    return None, 0


def TXA(cpu, *args):
    """
    Transfer X-register to accumulator
    """
    
    return None, 0


def TXS(cpu, *args):
    """
    Transfer X-register to stack pointer
    """
    
    return None, 0


def TYA(cpu, *args):
    """
    Transfer Y-register to accumulator
    """
    
    return None, 0
