from gendiff.parser import get_parser
from gendiff.engine import generate_diff

def main():
    parser = get_parser()
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)

if __name__ == '__main__':
    main()