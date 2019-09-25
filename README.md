# `oerp2odoo` Command Line Tool

This tool is designed to help migrate custom modules from OpenERP (primarily v7)
to Odoo 12+. It may be useful for conversions between other versions too -
contributions welcome!

# Usage

We recommend first running python's `2to3` command line utility first:

```
2to3 -wn module_dir   # update all code in module_dir
```

then:

```
oerp2odoo <module_path>
```

# License

MIT