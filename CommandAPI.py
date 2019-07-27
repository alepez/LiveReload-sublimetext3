#!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import LiveReload
import webbrowser
import os


class LiveReloadTest(sublime_plugin.ApplicationCommand):

    def run(self):
        path = os.path.join(sublime.packages_path(), 'LiveReload', 'web')
        file_name = os.path.join(path, 'test.html')
        webbrowser.open_new_tab("file://"+file_name)


class LiveReloadHelp(sublime_plugin.ApplicationCommand):

    def run(self):
        webbrowser.open_new_tab('https://github.com/alepez/LiveReload-sublimetext3#using'
                                )


class LiveReloadEnablePluginCommand(sublime_plugin.ApplicationCommand):

    def on_done(self, index):
        if not index is -1:
            LiveReload.Plugin.togglePlugin(index)

    def run(self):
        sublime.active_window().show_quick_panel(LiveReload.Plugin.listPlugins(),
                self.on_done)


class LiveReloadConfigPluginCommand(sublime_plugin.ApplicationCommand):
    def run(self, plugin=None, operation="noop"):
        if not isinstance(plugin, str):
            return

        plugin_names = [p.__name__ for p in LiveReload.Plugin.plugins]
        # print("Available plugins: ", plugin_names)

        try:
            index = plugin_names.index(plugin)
        except ValueError:
            sublime.error_message("Plugin not found: " + plugin)
            return

        p = LiveReload.Plugin.getPlugin(plugin)

        if (
            operation == "toggle"
            or (operation == "enable" and not p.isEnabled)
            or (operation == "disable" and p.isEnabled)
        ):
            LiveReload.Plugin.togglePlugin(index)
