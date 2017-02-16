	def export_models(self):
		data = self.model_arrays.get()[0]
		vp = data['vp'].T.astype(np.float32).tofile('model.vp')
		vs = data['vs'].T.astype(np.float32).tofile('model.vs')
		rho = (data['den']*1000).T.astype(np.float32).tofile('model.rho')
		qp = data['qp'].T.astype(np.float32).tofile('model.qp')
		qs = data['qs'].T.astype(np.float32).tofile('model.qs')