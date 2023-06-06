odoo.define("academy.hamster", function (require) {
    "use strict";

    var Animal = require("academy.animal");

    var DanceMixin = {
        dance: function () {
            console.log("Danciiiiing!!!!");
        },
    };

    var Hamster = Animal.extend(DanceMixin, {
        sleep: function () {
            console.log("Sleeeeep!!!!");
        },
    });

    var hamster = new Hamster();
    hamster.dance();
    hamster.move();
    hamster.sleep();
});
