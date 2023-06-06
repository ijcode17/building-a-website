from odoo.tests import common


class TestUiTeachers(common.HttpCase):
    @common.at_install(False)
    @common.post_install(True)
    def test_01_admin_teachers_tour(self):
        self.start_tour(
            "/",
            "odoo.__DEBUG__.services['web_tour.tour'].run('tour_show_biographies')",
            "odoo.__DEBUG__.services[web_tour.tour].tours.tour_show_biographies.ready",
            login="admin",
        )
