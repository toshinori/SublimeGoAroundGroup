import sublime, sublime_plugin
import os.path

class GoAroundGroupCommand(sublime_plugin.WindowCommand):
  def run(self, movement):
    active_group = self.window.active_group()
    next_group = self.window.active_group() + movement

    if next_group == self.window.num_groups():
      next_group = 0
    elif next_group < 0:
      next_group = self.window.num_groups() - 1

    self.window.focus_group(next_group)

class GoAroundNextGroupCommand(GoAroundGroupCommand):
  def run(self):
    super(GoAroundNextGroupCommand, self).run(1)


class GoAroundPreviousGroupCommand(GoAroundGroupCommand):
  def run(self):
    super(GoAroundPreviousGroupCommand, self).run(-1)
