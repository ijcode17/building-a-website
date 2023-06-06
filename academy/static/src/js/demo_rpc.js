odoo.define("academy.demo_rpc", function (require) {
    "use strict";

    var core = require("web.core"),
        Widget = require("web.Widget"),
        rpc = require("web.rpc");

    require("web.dom_ready");
    var RpcButton = Widget.extend({
        // self: this,
        events: {
            "click .rpc-button": "_onClick",
        },
        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.options = _.extend(options || {}, {});
        },
        _onClick: function (e) {
            console.log("Clicked");
            rpc.query({
                route: "/academy/search_teacher",
                params: {
                    teacher_id: this.$el.data("teacher-id"),
                },
            }).then(function (teachers_found) {
                console.log(teachers_found);
            });
            // rpc.query({
            //   model: 'academy.teachers',
            //   method: 'search_read',
            //   args: [[['id', '=', this.$el.data('teacher-id')]], ['biography']]
            // }).then(function (data){
            //   if(data.length){
            //     $('.biography').html(data[0].biography)
            //   }
            // })
        },
    });

    if (!$(".rpc-container").length) {
        return $.Deferred().reject("DOM doesn't contain '.rpc-container'");
    }

    $(".rpc-container").each(function (idx) {
        var $elem = $(this);
        var button = new RpcButton(null, $elem.data());
        button.attachTo($elem);
    });
    return RpcButton;
});
