import unittest
from turing_machine_utils import create_turing_machine


class TestTuringMachineDiscard(unittest.TestCase):
    def test_discard(self):
        tape = ['0', '1', '1', '1', '0']
        states = ['q0', 'q1', 'accept', 'discard']
        transition_rules = {
            ('q0', '0'): ('q1', '1', 'R'),
            ('q0', '1'): ('q0', '1', 'R'),
            ('q1', '0'): ('discard', '0', 'L'),
            ('q1', '1'): ('q1', '1', 'R'),
        }

        result = create_turing_machine(tape, states, transition_rules)
        self.assertEqual(result, -1)

