from model import *
from app import *

with app.app_context():
	pdb.create_all()

	phy_cat  = Category(title="Physics");
	chem_cat = Category(title="Chemistry");
	math_cat = Category(title="Math");

	pdb.session.add(phy_cat);
	pdb.session.add(chem_cat);
	pdb.session.add(math_cat);
	pdb.session.commit();

	exit()

