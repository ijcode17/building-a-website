from odoo import http

from odoo.addons.website_sale.controllers.main import WebsiteSale


class Academy(http.Controller):
    @http.route("/academy/academy/", auth="public", website=True)
    def index(self, **kw):
        Teachers = http.request.env["academy.teachers"]
        return http.request.render(
            "academy.index",
            {
                "teachers": Teachers.search([]),
            },
        )

    @http.route("/academy/<name>", auth="public", website=True)
    def teacher(self, name):
        return "<h1>{}</h1>".format(name)

    @http.route("/academy/<model('academy.teachers'):teacher>", auth="public", website=True)
    def model_teacher(self, teacher):
        return http.request.render("academy.biography", {"teacher": teacher})


class WebsiteSaleInherit(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search="", min_price=0.0, max_price=0.0, ppg=False, **post):
        print("Inherit shop")
        res = super().shop(
            page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg, **post
        )
        import ipdb

        ipdb.set_trace()
        res.qcontext["search"] = "Mouse"
        res.qcontext["categories"] = res.qcontext["categories"].sorted(key=lambda r: r.name)
        return res
