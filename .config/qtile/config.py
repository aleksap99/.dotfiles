#import os
from collections.abc import Callable
from libqtile import qtile, bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
#terminal = guess_terminal()
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
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
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
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.function(go_to_group(i.name)),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

def init_widgets_list_main(visible_groups):
    separator = widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0])
    pipe = widget.TextBox(
            text = '|',
            font = "Iosevka Bold",
            background = colors[0],
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
            padding_x = 3,
            borderwidth = 3,
            active = colors[2],
            inactive = colors[7],
            rounded = False,
            highlight_color = colors[1],
            highlight_method = "line",
            this_current_screen_border = colors[6],
            this_screen_border = colors [4],
            other_current_screen_border = colors[6],
            other_screen_border = colors[4],
            foreground = colors[2],
            background = colors[0],
            visible_groups = visible_groups,
        ),
        separator, 
        pipe,
#             widget.CurrentLayoutIcon(
#                      custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
#                      foreground = colors[2],
#                      background = colors[0],
#                      padding = 0,
#                      scale = 0.7
#                      ),
        widget.CurrentLayout(
            foreground = colors[2],
            background = colors[0],
            padding = 5
        ),
        pipe,
        widget.Prompt(),
        widget.WindowName(
            foreground = colors[6],
            background = colors[0],
            padding = 0
        ),
        widget.Systray(
            background = colors[0],
            padding = 5
        ),
        separator,
#       widget.Net(
#           interface = "enp34s0",
#           format = 'Net: {down} ↓↑ {up}',
#           foreground = colors[3],
#           background = colors[0],
#           padding = 5,
#           decorations=[
#               BorderDecoration(
#                   colour = colors[3],
#                   border_width = [0, 0, 2, 0],
#                   padding_x = 5,
#                   padding_y = None,
#               )
#           ],
#       ),
#       separator,
#       widget.ThermalSensor(
#           foreground = colors[4],
#           background = colors[0],
#           threshold = 90,
#           fmt = 'Temp: {}',
#           padding = 5,
#           decorations=[
#               BorderDecoration(
#                   colour = colors[4],
#                   border_width = [0, 0, 2, 0],
#                   padding_x = 5,
#                   padding_y = None,
#               ),
#           ],
#       ),
#       separator, 
        widget.CheckUpdates(
            update_interval = 1800,
            distro = "Arch_checkupdates",
            display_format = "{updates} ↓",
            foreground = colors[5],
            colour_have_updates = colors[5],
            colour_no_updates = colors[5],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
            padding = 5,
            background = colors[0],
            decorations=[
                BorderDecoration(
                    colour = colors[5],
                    border_width = [0, 0, 2, 0],
                    padding_x = 5,
                    padding_y = None,
                )
            ],
        ),
#       widget.Memory(
#           foreground = colors[9],
#           background = colors[0],
#           mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
#           fmt = 'Mem: {}',
#           padding = 5,
#           decorations=[
#               BorderDecoration(
#                   colour = colors[9],
#                   border_width = [0, 0, 2, 0],
#                   padding_x = 5,
#                   padding_y = None,
#               )
#           ],
#       ),
#       widget.Volume(
#           foreground = colors[7],
#           background = colors[0],
#           fmt = 'Vol: {}',
#           padding = 5,
#           decorations=[
#               BorderDecoration(
#                   colour = colors[7],
#                   border_width = [0, 0, 2, 0],
#                   padding_x = 5,
#                   padding_y = None,
#               )
#           ],
#       ),
        widget.KeyboardLayout(
            foreground = colors[8],
            background = colors[0],
            fmt = 'Keyboard: {}',
            padding = 5,
            decorations=[
                BorderDecoration(
                    colour = colors[8],
                    border_width = [0, 0, 2, 0],
                    padding_x = 5,
                    padding_y = None,
                )
            ],
        ),
        widget.Clock(
            foreground = colors[6],
            background = colors[0],
            format = "%A, %B %d - %H:%M ",
            decorations=[
                BorderDecoration(
                    colour = colors[6],
                    border_width = [0, 0, 2, 0],
                    padding_x = 5,
                    padding_y = None,
                )
            ],
        ),

    ]
    return widgets_list

def init_widgets_list_secondary(visible_groups):
    separator = widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0])
    pipe = widget.TextBox(
            text = '|',
            font = "Iosevka Bold",
            background = colors[0],
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
            padding_x = 3,
            borderwidth = 3,
            active = colors[2],
            inactive = colors[7],
            rounded = False,
            highlight_color = colors[1],
            highlight_method = "line",
            this_current_screen_border = colors[6],
            this_screen_border = colors [4],
            other_current_screen_border = colors[6],
            other_screen_border = colors[4],
            foreground = colors[2],
            background = colors[0],
            visible_groups = visible_groups,
        ),
        pipe,
        widget.WindowName(
            foreground = colors[6],
            background = colors[0],
            padding = 0
        ),
    ]
    return widgets_list

def init_screen(widgets):
    screen = Screen(
        top=bar.Bar(
            widgets=widgets,
            size=22,
        ),
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
#floating_layout = layout.Floating(
#    float_rules=[
#        # Run the utility of `xprop` to see the wm class and name of an X client.
#        *layout.Floating.default_float_rules,
#       Match(wm_class="confirmreset"),  # gitk
#       Match(wm_class="makebranch"),  # gitk
#       Match(wm_class="maketag"),  # gitk
#       Match(wm_class="ssh-askpass"),  # ssh-askpass
#       Match(title="branchdialog"),  # gitk
#       Match(title="pinentry"),  # GPG key password entry
#    ]
#)
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
