Voor een diepgaande tutorial voor django: https://docs.djangoproject.com/en/4.2/intro/tutorial01/

Commands: 
installeer django: pip install django
Start app:		 py manage.py runserver
Verander port: 	 py manage.py runserver {port of ip}
app template: 	 py manage.py startapp {naam app}


Files:
mysite\mysite:			in deze map kan je alles vinden om instellingen te wijzigen die gelden voor heel de applicatie 
mysite\polls\static\images:	voor images
mysite\polls\static\polls:	voor css frontend
mysite\polls\templates\polls: voor html frontend
mysite\polls\admin.py:		hier kan je extra lijsten toevoegen net zoals question(met de question lijst wordt er een nieuwe pagina gemaakt voor elke question) 
mysite\polls\apps.py:		app config
mysite\polls\models.py:		db models van de vragen
mysite\polls\tests.py:		mocht er iemand zin hebben om testen te schrijven
mysite\polls\urls.py:		url path's
mysite\polls\views.py: 		pagina's


Urls: 
http://127.0.0.1:8000/polls/		Hoofdpagina
http://127.0.0.1:8000/polls/{nr}	specifieke pagina genummerd als in de lijst question
http://127.0.0.1:8000/admin/		admin pagina (ww: admin pw: admin email: admin@mail.com)