import sublime, sublime_plugin

FILEENDING = ".tem"

class TemplViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        import os, codecs
        from . import helper

        data = helper.render(self.view)
        x = helper.newViewWithContent(data, edit)

class TemplFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        import os, codecs
        from . import helper
        
        if not self.view.file_name().endswith(FILEENDING):
            sublime.error_message("File is not an Template (Filending must be '"+FILEENDING+"')")
            return
        newFileName = os.path.splitext(self.view.file_name())[0]
        try:
            f = codecs.open(newFileName, "w", "utf-8")
            data = helper.render(self.view)
            f.write(data)
            f.close()
            sublime.status_message("Template saved to '%s'"%newFileName)
            self.view.window().open_file(newFileName)
        except Exception as ex:
            sublime.error_message(str(ex))
        