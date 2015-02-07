from dwell import db

class city(Document):
	structure = {
		'name':unicode,
		'spr_temp':unicode,
		'sum_temp':unicode,
		'aut_temp':unicode,
		'win_temp':unicode,
		
	}
	validators={
		'name':max_length(50),
		'spr_temp': max_length(4),
		'sum_temp': max_length(4),
		'aut_temp': max_length(4),
		'win_temp': max_length(4)

	}
	use_dot_notation = True
	def _repr_(self):
		return '<City %r>' % (self.name)
	connection.register([City])
	

