#!/usr/bin/env python3
"""Password Generator"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Python Password Generator",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    return parser.parse_args()


# --------------------------------------------------

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nouns = ["apple", "bycicle", "car", "Dakota", "eggplant"]

def main():
    """Main function"""

    args = get_args()

    password_length = int(input("How should your password be? ") or "6")

    
    
    
# --------------------------------------------------
if __name__ == '__main__':
    main()