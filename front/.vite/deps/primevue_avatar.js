import {
  script
} from "./chunk-FRCWHNZ6.js";
import "./chunk-OFFNAEAN.js";
import {
  BaseStyle
} from "./chunk-6VXE72DV.js";
import {
  createBlock,
  createCommentVNode,
  createElementBlock,
  mergeProps,
  normalizeClass,
  openBlock,
  renderSlot,
  resolveDynamicComponent,
  toDisplayString
} from "./chunk-YJZCKX3S.js";
import "./chunk-DZZM6G22.js";

// node_modules/primevue/avatar/style/index.mjs
var theme = function theme2(_ref) {
  var dt = _ref.dt;
  return "\n.p-avatar {\n    display: inline-flex;\n    align-items: center;\n    justify-content: center;\n    width: ".concat(dt("avatar.width"), ";\n    height: ").concat(dt("avatar.height"), ";\n    font-size: ").concat(dt("avatar.font.size"), ";\n    background: ").concat(dt("avatar.background"), ";\n    border-radius: ").concat(dt("avatar.border.radius"), ";\n}\n\n.p-avatar-image {\n    background: transparent;\n}\n\n.p-avatar-circle {\n    border-radius: 50%;\n}\n\n.p-avatar-circle img {\n    border-radius: 50%;\n}\n\n.p-avatar-icon {\n    font-size: ").concat(dt("avatar.font.size"), ";\n}\n\n.p-avatar img {\n    width: 100%;\n    height: 100%;\n}\n\n.p-avatar-lg {\n    width: ").concat(dt("avatar.lg.width"), ";\n    height: ").concat(dt("avatar.lg.width"), ";\n    font-size: ").concat(dt("avatar.lg.font.size"), ";\n}\n\n.p-avatar-lg .p-avatar-icon {\n    font-size: ").concat(dt("avatar.lg.font.size"), ";\n}\n\n.p-avatar-xl {\n    width: ").concat(dt("avatar.xl.width"), ";\n    height: ").concat(dt("avatar.xl.width"), ";\n    font-size: ").concat(dt("avatar.xl.font.size"), ";\n}\n\n.p-avatar-xl .p-avatar-icon {\n    font-size: ").concat(dt("avatar.xl.font.size"), ";\n}\n\n.p-avatar-group {\n    display: flex;\n    align-items: center;\n}\n\n.p-avatar-group .p-avatar + .p-avatar {\n    margin-left: ").concat(dt("avatar.group.offset"), ";\n}\n\n.p-avatar-group .p-avatar {\n    border: 2px solid ").concat(dt("avatar.group.border.color"), ";\n}\n");
};
var classes = {
  root: function root(_ref2) {
    var props = _ref2.props;
    return ["p-avatar p-component", {
      "p-avatar-image": props.image != null,
      "p-avatar-circle": props.shape === "circle",
      "p-avatar-lg": props.size === "large",
      "p-avatar-xl": props.size === "xlarge"
    }];
  },
  label: "p-avatar-label",
  icon: "p-avatar-icon"
};
var AvatarStyle = BaseStyle.extend({
  name: "avatar",
  theme,
  classes
});

// node_modules/primevue/avatar/index.mjs
var script$1 = {
  name: "BaseAvatar",
  "extends": script,
  props: {
    label: {
      type: String,
      "default": null
    },
    icon: {
      type: String,
      "default": null
    },
    image: {
      type: String,
      "default": null
    },
    size: {
      type: String,
      "default": "normal"
    },
    shape: {
      type: String,
      "default": "square"
    },
    ariaLabelledby: {
      type: String,
      "default": null
    },
    ariaLabel: {
      type: String,
      "default": null
    }
  },
  style: AvatarStyle,
  provide: function provide() {
    return {
      $pcAvatar: this,
      $parentInstance: this
    };
  }
};
var script2 = {
  name: "Avatar",
  "extends": script$1,
  inheritAttrs: false,
  emits: ["error"],
  methods: {
    onError: function onError(event) {
      this.$emit("error", event);
    }
  }
};
var _hoisted_1 = ["aria-labelledby", "aria-label"];
var _hoisted_2 = ["src", "alt"];
function render(_ctx, _cache, $props, $setup, $data, $options) {
  return openBlock(), createElementBlock("div", mergeProps({
    "class": _ctx.cx("root"),
    "aria-labelledby": _ctx.ariaLabelledby,
    "aria-label": _ctx.ariaLabel
  }, _ctx.ptmi("root")), [renderSlot(_ctx.$slots, "default", {}, function() {
    return [_ctx.label ? (openBlock(), createElementBlock("span", mergeProps({
      key: 0,
      "class": _ctx.cx("label")
    }, _ctx.ptm("label")), toDisplayString(_ctx.label), 17)) : _ctx.$slots.icon ? (openBlock(), createBlock(resolveDynamicComponent(_ctx.$slots.icon), {
      key: 1,
      "class": normalizeClass(_ctx.cx("icon"))
    }, null, 8, ["class"])) : _ctx.icon ? (openBlock(), createElementBlock("span", mergeProps({
      key: 2,
      "class": [_ctx.cx("icon"), _ctx.icon]
    }, _ctx.ptm("icon")), null, 16)) : _ctx.image ? (openBlock(), createElementBlock("img", mergeProps({
      key: 3,
      src: _ctx.image,
      alt: _ctx.ariaLabel,
      onError: _cache[0] || (_cache[0] = function() {
        return $options.onError && $options.onError.apply($options, arguments);
      })
    }, _ctx.ptm("image")), null, 16, _hoisted_2)) : createCommentVNode("", true)];
  })], 16, _hoisted_1);
}
script2.render = render;
export {
  script2 as default
};
//# sourceMappingURL=primevue_avatar.js.map
