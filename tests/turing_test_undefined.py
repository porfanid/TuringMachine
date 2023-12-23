import unittest
from turing_machine_utils import create_turing_machine


class TestTuringMachineUndefined(unittest.TestCase):
    def test_undefined(self):
        undefined_tape = ['0', '1', '1', '1', '0']
        states = ['q0', 'q1', 'accept', 'discard']
        transition_rules = {
            ('q0', '1'): ('q0', '0', 'R'),
            ('q1', '0'): ('accept', '0', 'L'),
            ('q1', '1'): ('discard', '1', 'L'),
        }

        result = create_turing_machine(undefined_tape, states, transition_rules)
        self.assertEqual(result, 0)
