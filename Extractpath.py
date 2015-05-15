# -*- coding: utf-8 -*-

import re
import sublime
import sublime_plugin


class ExtractpathCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        reg = self.view.sel()[0]

        line = self.view.line(reg)
        line_text = self.view.substr(line)

        try:

            filename = re.findall("[/a-zA-Z0-9_\-\.]+\.html", line_text)[0]
            self.view.window().run_command('show_overlay', {'overlay': 'goto', 'show_files': True, 'text': filename})

        except Exception as e:
            sublime.status_message('error: {}'.format(str(e)))

