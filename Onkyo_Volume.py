#!/usr/bin/env python3
import sys
from eiscp import eISCP

REC_IP = '192.168.28.35'

def main():
    try:
        step = int(sys.argv[1])
    except (IndexError, ValueError):
        step = 5  # Standard: +5 Schritte

    with eISCP(REC_IP) as receiver:
        if step > 0:
            for _ in range(step):
                receiver.raw('MVLUP')
        elif step < 0:
            for _ in range(abs(step)):
                receiver.raw('MVLDOWN')

if __name__ == '__main__':
    main()