{
    "name": "Vauxoo Theme Tutorial",
    "description": "A theme tutorial for Odoo 16.0",
    "version": "16.0.1.0.0",
    "author": "Vauxoo",
    "category": "Theme/Creative",
    "license": "LGPL-3",
    "depends": [
        "website",
    ],
    "data": [
        "views/image_gallery.xml",
        "views/snippets.xml",
        "views/layout.xml",
        "views/pages.xml",
    ],
    "assets": {"web.assets_frontend": ["theme_tutorial/static/src/scss/main.scss"]},
    "installable": True,
}
