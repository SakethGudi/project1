states :[
     'Maharashtra':'MH',
	 'Telangana' :'TS' ,
	 'Karnataka' :'KR',
	 'Kerala' :'KL',
	 'Tamil Nadu':'TN' ]
Cities:[
    'MH' :'Mumbai',
    'TS':'Hyderabad',	
	'KR':'Bengaluru']
Cities['KL']:'Trivandrum'
Cities['TN']:'Chennai'
print("_"*10)
print("MH Has :", Cities['MH'])
print("TS Has :", Cities['TS'])

print("_"*10)
print("Maharashtra's abrreviaton is :", states['Maharashtra'])
print("Tamil Nadu's abrreviaton is:", states['Tamil Nadu'])

print("_"*10)
print("Kerala has :", Cities[states['Kerala']])
print("Karnataka has :", Cities[states['Karnataka']])

print("_"*10)
for state, abbrev in states.items():
        print ("%s is abbreviated %s" % (state, abbrev))
	
print( '- ' * 10)
for state, abbrev in states.items():
        print ("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))	
	