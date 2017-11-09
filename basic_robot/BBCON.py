__author__ = 'clauswrm'
from basic_robot import Arbitrator

class BBCON:

	def __init__(self):
		self.behaviors = []
		self.active_behaviors = []
		self.sensobs = []
		self.motobs = []
		self.arbitrator = Arbitrator()

	def add_behaivor(self, behavior):
		self.behaviors.append(behavior)

	def add_sensob(self, sensob):
		self.sensobs.append(sensob)

	def activate_behavior(self, behavior):
		if behavior not in self.active_behaviors:
			self.active_behaviors.append(behavior)

	def deactivate_behavior(self, behavior):
		if behavior in self.active_behaviors:
			self.active_behaviors.remove(behavior)

	def run_one_timestep(self):
		"""
		Updates all sensobs
		Updates all behaviors
		Invoke arbitrator
		Upade motobs
		Wait
		Reset sensobs
		"""