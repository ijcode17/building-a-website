{
    "name": "Academy B&F",
    "version": "16.0.1.0.0",
    "author": "Vauxoo",
    "category": "Website",
    "license": "LGPL-3",
    "depends": [
        "website_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/academy_teachers_menus.xml",
        "views/academy_teachers_views.xml",
        "views/views.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "academy/static/src/js/animal.js",
            "academy/static/src/js/dog.js",
            "academy/static/src/js/hamster.js",
            "academy/static/src/js/counter.js",
            "academy/static/src/js/demo_rpc.js",
            "academy/static/src/js/academy_tour.js",
        ]
    },
    "application": True,
    "installable": True,
}
