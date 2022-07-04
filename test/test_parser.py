from cfmt.main import get_parser

def test_basic_bundle():
    parser = get_parser()
    buffer = bytes("bundle agent my_bundle { }", "utf8")
    tree = parser.parse(buffer)
    assert tree.root_node.sexp() == "test"