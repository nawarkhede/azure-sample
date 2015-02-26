from django.http import HttpResponse
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import lxml
def index(request):
	return HttpResponse("""
	
	<!DOCTYPE html>
	<html>
	<head>
	  <title>Hello Azure - from Python Django</title>
	</head>

	<body>

	  <h1>Hello Azure - from Python Django</h1>
	  <h4>Clone at <a href=' https://github.com/nawarkhede/vsplcrepo'> https://github.com/nawarkhede/vsplcrepo</a></h4>

	  <p>Sample Azure django project. With pre-installed third party libraries which are not available on pip. </p>

	</body>

	</html>
	
	""")