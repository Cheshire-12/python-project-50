from gendiff.engine import generate_diff
from gendiff.parser import get_parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()