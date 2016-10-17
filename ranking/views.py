from django.shortcuts import render


from files.models import Document


def leader_board(request):
	records = Document.objects.all()
	return render(request, 'ranking/leader_board.html', {'records': records})
