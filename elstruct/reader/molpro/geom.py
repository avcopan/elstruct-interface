from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib


def block(head_string, foot_string, string):
    head_pattern = rep.escape(head_string)
    foot_pattern = rep.escape(foot_string)
    block_pattern = rep.capturing(
        head_pattern + rep.one_or_more(relib.ANY_CHAR, greedy=False) +
        foot_pattern)
    return ref.last_capture(block_pattern, string)


if __name__ == '__main__':
    STRING = open('output.dat').read()
    print(block('Current geometry', '***********', STRING))
