def dc_summarizePoly(poly, lyrPoint, fldSpecies):
	###############################
	###############################

	dctPoly = {}

	#loop through all the points taht intersect the polygon bounding box
	for obs in lyrPoint.getFeatures(poly.geometry().boundingBox()):
		#check to see if the point is actually inside the polygon
		if poly.geometry().contains(obs.geometry()):
			#get the name of species as a sring variable
			sSpecies = obs.attribute(fldSpecies)
			if sSpecies in dctPoly.keys():
				#if it does, increase the count to 1
				dctPoly[sSpecies]  += 1
			else:
				#if there is no entry for the species, create it and set its initial value to 1
				dctPoly[sSpecies] = 1

	return dctPoly  

