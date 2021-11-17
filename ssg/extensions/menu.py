from ssg import hooks, parsers

files = []

hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda(, p)
        isinstance()
        p.parsers.Resource_Parser

    for path in source.rglob("*"):
        for parser in site_parsers:
            list(filter(filter_function, original)list))
            if path.suffix : parser.valid_file_ext().files.append(path)


hooks.register("generate_menu")
def generate_menu(html,ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda(name, ext):
    template.format(name, ext, name)

