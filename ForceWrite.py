# ForceWrite - (attempt to) overwrite a read-only file writing
import sublime, sublime_plugin
import os, stat

class ForceWrite(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    if view.is_dirty():
        fileName = view.file_name()
        fileAttr = os.stat(fileName).st_mode
        if (not fileAttr & stat.S_IWRITE):
            if(sublime.ok_cancel_dialog('The file is read-only. Overwrite?', 'Overwrite')):
                try:
                  os.chmod(fileName, fileAttr | stat.S_IWRITE)
                except OSError:
                  print("Error: Unable to add owner write permissions. File unsaved.");

