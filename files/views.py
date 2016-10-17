from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Document
from .forms import DocumentForm

@login_required
def list(request):
	# handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'], user=request.user)
			newdoc.save()

			return HttpResponseRedirect(reverse('leader_board'))
	else:
		form = DocumentForm()
	documents = Document.objects.filter(user__id=request.user.id) # filter()

	return render(request, 'files/list.html', {'documents': documents,
												   'form': form})
