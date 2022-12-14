import os
from collections.abc import Callable
from libqtile import qtile, bar, layout, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle floating window"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch rofi "),
    Key([mod], "q", lazy.spawn("rofi -show power"), desc="Launch rofi power"),
    Key(['control', "shift"], "l", lazy.spawn("slock"), desc="Launch slock"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "1234567890"]
def go_to_group(name: str) -> Callable:
    def _inner(qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return

        if name in '12345':
            qtile.focus_screen(0)
            qtile.groups_map[name].cmd_toscreen()
        elif name in '6789':
            qtile.focus_screen(1)
            qtile.groups_map[name].cmd_toscreen()
        elif name in '0':
            qtile.focus_screen(2)
            qtile.groups_map[name].cmd_toscreen()

    return _inner

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.function(go_to_group(i.name)),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

groups.append(ScratchPad('scratchpad', [
    DropDown("term", "alacritty", width=0.5, y=0.3, x=0.25),
    DropDown("files", "alacritty -e nnn -d -C", width=0.5, y=0.3, x=0.25),
    DropDown("mixer", "pavucontrol", width=0.5, y=0.3, x=0.25),
    DropDown("bitwarden", "bitwarden-desktop", width=0.5, y=0.3, x=0.25)
    ]))

keys.extend([
    Key(["control"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key(["control"], "2", lazy.group["scratchpad"].dropdown_toggle("files")),
    Key(["control"], "3", lazy.group["scratchpad"].dropdown_toggle("mixer")),
    Key(["control"], "4", lazy.group["scratchpad"].dropdown_toggle("bitwarden")),
    ])

colors = {
    "rosewater": "#f4dbd6",
    "white": "#fff",
    "flamingo"    : "#f0c6c6",
    "pink"        : "#f5bde6",
    "mauve"       : "#c6a0f6",
    "red"         : "#ed8796",
    "maroon"      : "#ee99a0",
    "peach"       : "#f5a97f",
    "yellow"      : "#eed49f",
    "green"       : "#a6da95",
    "teal"        : "#8bd5ca",
    "sky"         : "#91d7e3",
    "sapphire"    : "#7dc4e4",
    "blue"        : "#8aadf4",
    "lavender"    : "#b7bdf8",
    "text"        : "#cad3f5",
    "subtext1"    : "#b8c0e0",
    "subtext0"    : "#a5adcb",
    "overlay2"    : "#939ab7",
    "overlay1"    : "#8087a2",
    "overlay0"    : "#6e738d",
    "surface2"    : "#5b6078",
    "surface1"    : "#494d64",
    "surface0"    : "#363a4f",
    "base"        : "#24273a",
    "mantle"      : "#1e2030",
    "crust"       : "#181926"
}
layout_theme = {"border_width": 1,
                "margin": 8,
                "border_focus": colors["sapphire"],
                "border_normal": colors["base"],
               }
layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


def init_widgets_list_main(visible_groups):
    separator = widget.Sep(
            linewidth = 0,
            padding = 6,
            )

    pipe = widget.TextBox(
            text = '|',
            font = "Iosevka Bold",
            foreground = '474747',
            padding = 2,
            fontsize = 14)

    widgets_list = [
        separator,
        widget.Image(
            filename  = '~/.config/qtile/icons/qtile.png',
            margin = 5,
        ),
        widget.Spacer(
            length = 20,
        ),
        widget.GroupBox(
            font = "Iosevka Bold",
            fontsize = 11,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 7,
            borderwidth = 2,
            active = colors["mauve"],
            inactive = colors["white"],
            rounded = False,
            highlight_color = colors["mantle"],
            highlight_method = "line",
            this_current_screen_border = colors["red"],
            other_current_screen_border = colors["sapphire"],
            visible_groups = visible_groups,
        ),
        widget.Prompt(),
        separator,
        widget.Spacer(),
        widget.Systray(
            padding = 5
        ),
        separator,
        widget.CheckUpdates(
            update_interval = 1800,
            distro = "Arch_checkupdates",
            display_format = "{updates} ",
            foreground = colors["peach"],
            colour_have_updates = colors["peach"],
            colour_no_updates = colors["peach"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
            padding = 5,
        ),
        widget.TextBox(
            text = '',
            font = "Iosevka Bold",
            fontsize = 40,
            foreground = colors["sapphire"],
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn(os.path.expanduser("~/scripts/keyboard-leyout.sh"))
            },
        ),
        widget.KeyboardLayout(
            foreground = colors["sapphire"],
        ),
        widget.Spacer(
            length = 20,
        ),
        widget.Clock(
            foreground = colors["blue"],
            format = "%H:%M",
        ),
        widget.CurrentLayoutIcon(
            padding = 0,
            scale = 0.6,
            custom_icon_paths = [
                os.path.expanduser("~/.config/qtile/icons/"),
            ],
        ),
 
        widget.Image(
            filename = '~/.config/qtile/icons/power.png',
            margin = 5,
            mouse_callbacks  = {
                'Button1': lambda: qtile.cmd_spawn('rofi -show power')
            }
        ),
    ]
    return widgets_list

def init_widgets_list_secondary(visible_groups):
    separator = widget.Sep(
            linewidth = 0,
            padding = 6,)

    pipe = widget.TextBox(
            text = '|',
            font = "Iosevka Bold",
            foreground = '474747',
            padding = 2,
            fontsize = 14)

    widgets_list = [
        separator,
        widget.GroupBox(
            font = "Iosevka Bold",
            fontsize = 11,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 7,
            borderwidth = 2,
            active = colors["mauve"],
            inactive = colors["white"],
            rounded = False,
            highlight_color = colors["mantle"],
            highlight_method = "line",
            this_current_screen_border = colors["red"],
            other_current_screen_border = colors["sapphire"],
            visible_groups = visible_groups,
        ),
        pipe,
    ]
    return widgets_list

def init_screen(widgets):
    screen = Screen(
        top=bar.Bar(
            widgets=widgets,
            size=40,
            margin = [12, 12, 12, 12],
            background = colors["base"],
        ),
        wallpaper='~/.config/qtile/icons/catppuccin-arch.png',
        wallpaper_mode="fill",
    )
    return screen

screens = [
    init_screen(init_widgets_list_main(["1", "2", "3", "4", "5"])),
    init_screen(init_widgets_list_secondary(["6", "7", "8", "9"])),
    init_screen(init_widgets_list_secondary(["0"]))
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = colors["sapphire"],
    border_normal = colors["base"],
    margin = 12,
    border_width = 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
