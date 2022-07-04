import argparse
from tree_sitter import Language, Parser

def parse_args():
    parser = argparse.ArgumentParser(description="CFEngine policy formatter")
    parser.add_argument("files", nargs="*", help="Files to format")
    return parser.parse_args()


def get_parser():
    Language.build_library('build/my-languages.so', ['tree-sitter-cfengine'])
    CFENGINE_LANGUAGE = Language('build/my-languages.so', 'CFEngine')

    parser = Parser()
    parser.set_language(CFENGINE_LANGUAGE)
    return parser

def main():
    args = parse_args()

    parser = get_parser()
    for file in args.files:
        with open(file, mode="rb") as f:
            buffer = f.read()
            tree = parser.parse(buffer)
            root = tree.root_node
            print(root.sexp())
